import streamlit as st
import joblib
import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
ruta_modelo = os.path.join(base_dir, "svr_model-auto.joblib")
model = joblib.load(ruta_modelo)

st.title("Calculadora de Precio de Autos")

st.markdown("""
Esta herramienta estima el precio de un auto según sus características.
""")


engine_size = st.number_input("Tamaño del motor", 50, 300, help="Motores más grandes suelen durar mas y son mas potentes")
horsepower = st.number_input(" Potencia (HP)", 50, 300)
compression_ratio = st.number_input(" Compresión del motor", 7.0, 25.0)
length = st.number_input(" Largo del auto", 140.0, 220.0)
peak_rpm = st.number_input(" Revoluciones máximas (RPM)", 4000, 7000)
wheel_base = st.number_input(" Distancia entre ejes", 80.0, 120.0)
width = st.number_input(" Ancho del auto", 60.0, 80.0)

if st.button("Calcular precio"):
    datos = {
        "engine-size": engine_size,
        "horsepower": horsepower,
        "compression-ratio": compression_ratio,
        "length": length,
        "peak-rpm": peak_rpm,
        "wheel-base": wheel_base,
        "width": width
    }

    columnas = model.feature_names_in_
    X = pd.DataFrame([[datos[col] for col in columnas]], columns=columnas)

    pred = model.predict(X)
    precio = pred[0]

    
    tipo_cambio = 17
    precio_mxn = precio * tipo_cambio

    st.success(f" Precio estimado: ${precio_mxn:,.0f} MXN")

    st.caption(f"Tipo de cambio aproximado: 1 USD = {tipo_cambio} MXN")

    
    if precio_mxn < 200000:
        st.info(" Auto económico")

    elif precio_mxn < 500000:
        st.success(" Precio medio")

    else:
        st.warning(" Auto de gama alta")