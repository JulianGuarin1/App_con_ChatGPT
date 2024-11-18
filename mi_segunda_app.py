import streamlit as st

# Título de la app
st.title("Conversor de Unidades")

# Menú de selección principal
categoria = st.selectbox(
    "Selecciona una categoría de conversión:",
    [
        "Temperatura",
        "Longitud",
        "Peso/Masa",
        "Volumen",
        "Tiempo",
        "Velocidad",
        "Área",
        "Energía",
        "Presión",
        "Tamaño de Datos",
    ],
)

# Funciones de conversión
if categoria == "Temperatura":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Celsius a Fahrenheit",
            "Fahrenheit a Celsius",
            "Celsius a Kelvin",
            "Kelvin a Celsius",
        ],
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Celsius a Fahrenheit":
        resultado = valor * 9 / 5 + 32
    elif conversion == "Fahrenheit a Celsius":
        resultado = (valor - 32) * 5 / 9
    elif conversion == "Celsius a Kelvin":
        resultado = valor + 273.15
    elif conversion == "Kelvin a Celsius":
        resultado = valor - 273.15
    st.write(f"Resultado: {resultado}")

elif categoria == "Longitud":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Pies a metros",
            "Metros a pies",
            "Pulgadas a centímetros",
            "Centímetros a pulgadas",
        ],
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Pies a metros":
        resultado = valor * 0.3048
    elif conversion == "Metros a pies":
        resultado = valor / 0.3048
    elif conversion == "Pulgadas a centímetros":
        resultado = valor * 2.54
    elif conversion == "Centímetros a pulgadas":
        resultado = valor / 2.54
    st.write(f"Resultado: {resultado}")

elif categoria == "Peso/Masa":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Libras a kilogramos",
            "Kilogramos a libras",
            "Onzas a gramos",
            "Gramos a onzas",
        ],
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Libras a kilogramos":
        resultado = valor * 0.453592
    elif conversion == "Kilogramos a libras":
        resultado = valor / 0.453592
    elif conversion == "Onzas a gramos":
        resultado = valor * 28.3495
    elif conversion == "Gramos a onzas":
        resultado = valor / 28.3495
    st.write(f"Resultado: {resultado}")

elif categoria == "Volumen":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Galones a litros",
            "Litros a galones",
            "Pulgadas cúbicas a centímetros cúbicos",
            "Centímetros cúbicos a pulgadas cúbicas",
        ],
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Galones a litros":
        resultado = valor * 3.78541
    elif conversion == "Litros a galones":
        resultado = valor / 3.78541
    elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
        resultado = valor * 16.3871
    elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
        resultado = valor / 16.3871
    st.write(f"Resultado: {resultado}")

# Agrega las demás categorías de forma similar (Tiempo, Velocidad, Área, Energía, Presión, Tamaño de Datos)
