import streamlit as st

# Inicialización de datos de trivia
if "preguntas" not in st.session_state:
    st.session_state.preguntas = [
        {
            "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
            "opciones": ["Tierra", "Júpiter", "Saturno", "Marte"],
            "respuesta": "Júpiter",
        },
        {
            "pregunta": "¿En qué año fue lanzado el primer iPhone?",
            "opciones": ["2005", "2007", "2010", "2012"],
            "respuesta": "2007",
        },
        {
            "pregunta": "¿Quién escribió 'Cien años de soledad'?",
            "opciones": ["Mario Vargas Llosa", "Gabriel García Márquez", "Pablo Neruda", "Jorge Luis Borges"],
            "respuesta": "Gabriel García Márquez",
        },
        {
            "pregunta": "¿Cuál es la fórmula química del agua?",
            "opciones": ["H2O", "CO2", "O2", "H2"],
            "respuesta": "H2O",
        },
        {
            "pregunta": "¿Qué país ganó la Copa Mundial de Fútbol en 2018?",
            "opciones": ["Brasil", "Alemania", "Francia", "Argentina"],
            "respuesta": "Francia",
        },
    ]
    st.session_state.puntaje = 0
    st.session_state.indice_actual = 0
    st.session_state.estado_pregunta = "esperando_respuesta"  # Estados: "esperando_respuesta", "respuesta_mostrada"

# Función para mostrar una pregunta
def mostrar_pregunta():
    pregunta_actual = st.session_state.preguntas[st.session_state.indice_actual]
    st.subheader(f"Pregunta {st.session_state.indice_actual + 1}")
    st.write(pregunta_actual["pregunta"])
    opcion_seleccionada = st.radio(
        "Selecciona una opción:",
        pregunta_actual["opciones"],
        key=f"pregunta_{st.session_state.indice_actual}",
    )

    # Estado: esperando respuesta
    if st.session_state.estado_pregunta == "esperando_respuesta":
        if st.button("Responder"):
            if opcion_seleccionada == pregunta_actual["respuesta"]:
                st.success("¡Correcto!")
                st.session_state.puntaje += 1
            else:
                st.error(f"Incorrecto. La respuesta correcta es: {pregunta_actual['respuesta']}")
            st.session_state.estado_pregunta = "respuesta_mostrada"

    # Estado: respuesta mostrada
    elif st.session_state.estado_pregunta == "respuesta_mostrada":
        if st.button("Siguiente"):
            st.session_state.indice_actual += 1
            st.session_state.estado_pregunta = "esperando_respuesta"

# Función para mostrar el resultado final
def mostrar_resultado():
    st.subheader("¡Trivia finalizada!")
    st.write(f"Tu puntaje final es: {st.session_state.puntaje} de {len(st.session_state.preguntas)}")
    st.balloons()
    if st.button("Reiniciar Trivia"):
        st.session_state.puntaje = 0
        st.session_state.indice_actual = 0
        st.session_state.estado_pregunta = "esperando_respuesta"

# Interfaz principal
st.title("Trivia Interactiva 🌟")
st.sidebar.markdown("### Hecho por Julian Guarín")
st.sidebar.markdown("---")

if st.session_state.indice_actual < len(st.session_state.preguntas):
    mostrar_pregunta()
else:
    mostrar_resultado()



# Agregar mensaje en el pie de página
st.markdown("---")
st.markdown("### Hecho por Julian Guarín")
