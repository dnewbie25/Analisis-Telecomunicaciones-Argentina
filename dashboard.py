# Importar las librerías necesarias
import pandas as pd
import streamlit as st

# Configurar el título del dashboard
st.title("Dashboard de Ingresos y Usuarios de Servicios de TV e Internet en Argentina")

# Cargar los datos
tecnologias_df = pd.read_csv("EDA_CSV_Limpios/tecnologías_2023.csv")
ingresos_tv_df = pd.read_csv("EDA_CSV_Limpios/ingresos_anuales_TV.csv")
ingresos_internet_df = pd.read_csv("EDA_CSV_Limpios/ingresos_hasta_2023.csv")

# Graficar Ingresos de TV
st.subheader("Ingresos de TV")
ingresos_tv_df["Total TV"] = ingresos_tv_df["Ingresos_TV_suscripcion_miles"] + ingresos_tv_df["Ingresos_TV_satelital_miles"]
st.line_chart(ingresos_tv_df["Total TV"])

# Graficar Ingresos de Internet
st.subheader("Ingresos de Internet")
ingresos_anuales_internet = ingresos_internet_df.groupby("Año").agg({"Ingresos (miles de pesos)": "sum"}).reset_index()
st.line_chart(ingresos_anuales_internet.set_index('Año')["Ingresos (miles de pesos)"])

# Graficar Provincias con Mayor Número de Usuarios
st.subheader("Provincias con Mayor Número de Usuarios")
tecnologias_df["Total Usuarios"] = tecnologias_df[['ADSL','Cablemodem','Fibra óptica','Wireless','Otros']].sum(axis=1)  # Sumar todas las tecnologías
top_provincias = tecnologias_df[["Provincia", "Total Usuarios"]].sort_values(by="Total Usuarios", ascending=False).head(10)
st.bar_chart(top_provincias.set_index("Provincia")["Total Usuarios"])

# Graficar Tecnología más Usada de Internet en Argentina
st.subheader("Tecnología más Usada de Internet en Argentina")
uso_tecnologia = tecnologias_df.drop(columns=["Provincia","Total Usuarios"]).sum().sort_values(ascending=False)
st.bar_chart(uso_tecnologia)

# Sección de KPIs
st.sidebar.header("Análisis de Crecimiento Anual")

# KPI para Crecimiento de Ingresos de TV
st.sidebar.subheader("Crecimiento de Ingresos de TV")
ingresos_tv_df["Crecimiento"] = ingresos_tv_df["Total TV"].pct_change() * 100
crecimiento_promedio_tv = ingresos_tv_df["Crecimiento"].mean()
st.sidebar.metric("Crecimiento Promedio Anual de TV (%)", f"{crecimiento_promedio_tv:.2f}%", delta="5% Anual" if crecimiento_promedio_tv > 5 else "Menor al 5%")

# KPI para Crecimiento de Ingresos de Internet
st.sidebar.subheader("Crecimiento de Ingresos de Internet")
ingresos_internet_df["Crecimiento"] = ingresos_anuales_internet["Ingresos (miles de pesos)"].pct_change() * 100
crecimiento_promedio_internet = ingresos_internet_df["Crecimiento"].mean()
st.sidebar.metric("Crecimiento Promedio Anual de Internet (%)", f"{crecimiento_promedio_internet:.2f}%", delta="10% Anual" if crecimiento_promedio_internet > 10 else "Menor al 10%")

# Mensaje final en el dashboard
st.write("Análisis completo de los ingresos y usuarios de servicios en Argentina.")