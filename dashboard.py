import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Configuración el título del dashboard y estilo "wide"
st.set_page_config(layout="wide")
st.title("Dashboard de Ingresos y Usuarios de Servicios de TV e Internet en Argentina")

# Carga de los datos
tecnologias_df = pd.read_csv("EDA_CSV_Limpios/tecnologías_2023.csv")
ingresos_tv_df = pd.read_csv("EDA_CSV_Limpios/ingresos_anuales_TV.csv")
ingresos_internet_df = pd.read_csv("EDA_CSV_Limpios/ingresos_hasta_2023.csv")
internet_penetration_df = pd.read_csv("EDA_CSV_Limpios/penetracion_hasta_2023.csv")
tv_penetration_df = pd.read_csv("EDA_CSV_Limpios/penetracion_anual_prov_TV.csv")

# Grafica de Ingresos de TV
st.subheader("Ingresos de TV")
ingresos_tv_df["Total TV"] = ingresos_tv_df["Ingresos_TV_suscripcion_miles"] + ingresos_tv_df["Ingresos_TV_satelital_miles"]
ingresos_tv_df.rename(columns={"Ingresos_TV_suscripcion_miles":"Ingresos TV por Suscripción","Ingresos_TV_satelital_miles":"Ingresos TV Satelital"}, inplace=True)
st.bar_chart(ingresos_tv_df[["Año","Ingresos TV por Suscripción","Ingresos TV Satelital"]], x='Año', color=['#fd6b21','#0649fc'], y_label="Ingresos (miles de pesos)", x_label="Año")

# Grafica de Ingresos de Internet
st.subheader("Ingresos de Internet")
ingresos_internet_df["Año"] = ingresos_internet_df["Año"].astype(int)
ingresos_anuales_internet = ingresos_internet_df.groupby("Año").agg({"Ingresos (miles de pesos)": "sum"}).reset_index()
st.line_chart(ingresos_anuales_internet, y="Ingresos (miles de pesos)",x="Año", color='#fd6b21')

# Grafica de Provincias con Mayor Número de Usuarios de Internet
st.subheader("Provincias con Mayor Número de Usuarios de Internet")
tecnologias_df["Total Usuarios"] = tecnologias_df[['ADSL','Cablemodem','Fibra óptica','Wireless','Otros']].sum(axis=1)  # Sumar todas las tecnologías
top_provincias_agrupadas = tecnologias_df[["Provincia", "Total Usuarios"]].groupby("Provincia").sum().head(10).reset_index()
st.bar_chart(top_provincias_agrupadas, x="Provincia", horizontal=True, x_label="Número Total de Usuarios")

# Grafica de Provincias con Mayor Número de Usuarios de TV

# Grafica de Tecnología más Usada de Internet en Argentina
st.subheader("Tecnología más Usada de Internet en Argentina")
uso_tecnologia = tecnologias_df.drop(columns=["Provincia","Total Usuarios"]).sum()
print(tecnologias_df)
st.bar_chart(uso_tecnologia, x_label="Total Usuarios", y_label="Tecnología Usada", horizontal=True)

# Gráfico 1: Evolución de la Penetración de Internet
st.subheader("Evolución de la Penetración de Internet en Argentina (2014 - 2023)")
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(internet_penetration_df['Periodo'], internet_penetration_df['Accesos por cada 100 hogares'], label='Accesos por cada 100 hogares', marker='o')
ax1.plot(internet_penetration_df['Periodo'], internet_penetration_df['Accesos por cada 100 hab'], label='Accesos por cada 100 habitantes', marker='s')

# Configuración de etiquetas y título
ax1.set_title("Evolución de la Penetración de Internet en Argentina (2014 - 2023)")
ax1.set_xlabel("Periodo")
ax1.set_ylabel("Accesos")
ax1.legend()
ax1.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Gráfico 2: Penetración de TV por Provincia
st.subheader(f"Penetración de TV por Provincia (Año {tv_penetration_df.iloc[-1, 0]})")
tv_penetration_latest_year = tv_penetration_df.iloc[-1, 1:]  # Última fila, excluyendo columna 'Año'
tv_penetration_latest_year.sort_values(ascending=False, inplace=True)  # Ordenar de mayor a menor

fig2, ax2 = plt.subplots(figsize=(14, 7))
tv_penetration_latest_year.plot(kind='bar', color='skyblue', ax=ax2)

# Configuración de etiquetas y título
ax2.set_title(f"Penetración de TV por Provincia (Año {tv_penetration_df.iloc[-1, 0]})")
ax2.set_xlabel("Provincia")
ax2.set_ylabel("Penetración por cada 100 habitantes")
plt.xticks(rotation=90)
ax2.grid(axis='y')
st.pyplot(fig2)

# # Sección de KPIs
st.sidebar.header("Análisis de Crecimiento Anual")


# Definir el año base y el último año
base_year = internet_penetration_df['Año'].min()
latest_year = internet_penetration_df['Año'].max()

# Calcular la penetración de Internet en el año base y en el último año disponible
internet_base_penetration = internet_penetration_df[internet_penetration_df['Año'] == base_year]['Accesos por cada 100 hogares'].mean()
internet_latest_penetration = internet_penetration_df[internet_penetration_df['Año'] == latest_year]['Accesos por cada 100 hogares'].mean()

# Calcular el porcentaje de incremento en la penetración de Internet
internet_growth = ((internet_latest_penetration - internet_base_penetration) / internet_base_penetration) * 100

# Meta de incremento de penetración de Internet (en porcentaje)
internet_target = 15  # Meta de incremento en 15%

# Calcular la penetración de TV en el año base y en el último año disponible
tv_base_penetration = tv_penetration_df.iloc[0, 1:].mean()  # Primera fila (año base), promedio de todas las provincias
tv_latest_penetration = tv_penetration_df.iloc[-1, 1:].mean()  # Última fila (año más reciente), promedio de todas las provincias

# Calcular el porcentaje de incremento en la penetración de TV
tv_growth = ((tv_latest_penetration - tv_base_penetration) / tv_base_penetration) * 100

# Meta de incremento de penetración de TV (en porcentaje)
tv_target = 10  # Meta de incremento en 10%

# Crear una sección de KPIs en Streamlit
st.sidebar.title("KPIs de Penetración de Internet y TV en Argentina")

# Presentación consistente de los KPIs
col1, col2 = st.columns(2)

# KPI para Crecimiento de Ingresos de TV
with col1:
    st.sidebar.subheader("Crecimiento de Ingresos de TV")
    st.sidebar.metric(label="Meta de Crecimiento Anual (%)", value=5)
    st.sidebar.metric(label="Crecimiento Real (%)", value=f"{tv_growth:.2f}%")
    if tv_growth >= 5:
        st.sidebar.success("¡Meta alcanzada! 🎉")
    else:
        st.sidebar.warning("Meta no alcanzada.")

# KPI para Crecimiento de Ingresos de Internet
with col2:
    st.sidebar.subheader("Crecimiento de Ingresos de Internet")
    st.sidebar.metric(label="Meta de Crecimiento Anual (%)", value=10)
    st.sidebar.metric(label="Crecimiento Real (%)", value=f"{internet_growth:.2f}%")
    if internet_growth >= 10:
        st.sidebar.success("¡Meta alcanzada! 🎉")
    else:
        st.sidebar.warning("Meta no alcanzada.")

# Incremento de Penetración de Internet
st.sidebar.subheader(f"Incremento de Penetración de Internet ({base_year} - {latest_year})")
st.sidebar.metric(label="Meta de Crecimiento de Internet (%)", value=internet_target)
st.sidebar.metric(label="Crecimiento Real (%)", value=f"{internet_growth:.2f}%")

if internet_growth >= internet_target:
    st.sidebar.success("¡Meta alcanzada! 🎉")
else:
    st.sidebar.warning("Meta no alcanzada.")

# Incremento de Penetración de TV
st.sidebar.subheader(f"Incremento de Penetración de TV ({base_year} - {latest_year})")
st.sidebar.metric(label="Meta de Crecimiento de TV (%)", value=tv_target)
st.sidebar.metric(label="Crecimiento Real (%)", value=f"{tv_growth:.2f}%")

if tv_growth >= tv_target:
    st.sidebar.success("¡Meta alcanzada! 🎉")
else:
    st.sidebar.warning("Meta no alcanzada.")