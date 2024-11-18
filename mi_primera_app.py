import streamlit as st

# Título de la aplicación
st.title("Mi primera app")

# Autor
st.markdown("Esta app fue elaborada por **Julian Guarin**.")

# Entrada del usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Salida personalizada
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
