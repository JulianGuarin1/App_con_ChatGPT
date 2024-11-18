import streamlit as st
import pandas as pd

# Inicialización de datos
if "materias" not in st.session_state:
    st.session_state.materias = pd.DataFrame(
        columns=["Nombre", "Calificación", "Créditos", "Tipología"]
    )

# Función para calcular PAPA
def calcular_papa(data):
    if data.empty:
        return 0.0
    total_ponderado = (data["Calificación"] * data["Créditos"]).sum()
    total_creditos = data["Créditos"].sum()
    return total_ponderado / total_creditos if total_creditos > 0 else 0.0

# Registro de materias
def registrar_materia():
    st.subheader("Registro de Materias")
    nombre = st.text_input("Nombre de la materia:")
    calificacion = st.number_input("Calificación (0.0 - 5.0):", min_value=0.0, max_value=5.0, step=0.1)
    creditos = st.number_input("Número de créditos:", min_value=1, step=1)
    tipologia = st.selectbox("Tipología:", ["Obligatoria", "Optativa", "Libre Elección"])
    
    if st.button("Agregar Materia"):
        nueva_materia = {
            "Nombre": nombre,
            "Calificación": calificacion,
            "Créditos": creditos,
            "Tipología": tipologia,
        }
        st.session_state.materias = pd.concat(
            [st.session_state.materias, pd.DataFrame([nueva_materia])],
            ignore_index=True,
        )
        st.success("Materia agregada exitosamente.")

# Visualización de resultados
def mostrar_resultados():
    st.subheader("Resultados")
    
    # Mostrar materias registradas
    st.write("Materias registradas:")
    st.dataframe(st.session_state.materias)
    
    # Calcular PAPA global
    papa_global = calcular_papa(st.session_state.materias)
    st.write(f"**PAPA Global:** {papa_global:.2f}")
    
    # Calcular PAPA por tipología
    for tipo in ["Obligatoria", "Optativa", "Libre Elección"]:
        data_tipo = st.session_state.materias[st.session_state.materias["Tipología"] == tipo]
        papa_tipo = calcular_papa(data_tipo)
        st.write(f"**PAPA {tipo}:** {papa_tipo:.2f}")

# Interfaz principal
st.title("Cálculo de PAPA")
menu = st.sidebar.selectbox(
    "Menú",
    ["Registrar Materias", "Ver Resultados"],
)

if menu == "Registrar Materias":
    registrar_materia()
elif menu == "Ver Resultados":
    mostrar_resultados()

# Pie de página
st.sidebar.markdown("---")
st.sidebar.markdown("### Hecho por Julian Guarín")
# Agregar mensaje en el pie de página

