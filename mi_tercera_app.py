import streamlit as st
import pandas as pd
import datetime as dt

# Inicialización de variables
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Fecha", "Categoría", "Tipo", "Monto", "Descripción"]
    )

if "presupuestos" not in st.session_state:
    st.session_state.presupuestos = {}

if "metas" not in st.session_state:
    st.session_state.metas = {}


# Función para registrar ingresos/gastos
def registrar_transaccion():
    st.subheader("Registrar Ingresos/Gastos")
    fecha = st.date_input("Fecha", dt.date.today())
    categoria = st.selectbox("Categoría", ["Alimentos", "Transporte", "Entretenimiento", "Ahorro", "Otros"])
    tipo = st.radio("Tipo", ["Ingreso", "Gasto"])
    monto = st.number_input("Monto", min_value=0.0, step=0.01)
    descripcion = st.text_input("Descripción")
    
    if st.button("Registrar"):
        nueva_fila = {"Fecha": fecha, "Categoría": categoria, "Tipo": tipo, "Monto": monto, "Descripción": descripcion}
        st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([nueva_fila])], ignore_index=True)
        st.success("Transacción registrada exitosamente.")


# Función para configurar presupuestos
def configurar_presupuesto():
    st.subheader("Configurar Presupuesto")
    categoria = st.selectbox("Categoría", ["Alimentos", "Transporte", "Entretenimiento", "Ahorro", "Otros"])
    presupuesto = st.number_input(f"Presupuesto para {categoria}:", min_value=0.0, step=0.01)

    if st.button("Guardar presupuesto"):
        st.session_state.presupuestos[categoria] = presupuesto
        st.success(f"Presupuesto para {categoria} configurado en {presupuesto:.2f}.")


# Función para configurar metas de ahorro
def configurar_metas():
    st.subheader("Configurar Metas de Ahorro")
    meta = st.number_input("Monto de la meta de ahorro:", min_value=0.0, step=0.01)
    fecha_limite = st.date_input("Fecha límite para la meta", dt.date.today())

    if st.button("Guardar meta"):
        st.session_state.metas = {"meta": meta, "fecha_limite": fecha_limite}
        st.success(f"Meta de ahorro configurada: {meta:.2f} antes de {fecha_limite}.")


# Función para generar reportes
def generar_reporte():
    st.subheader("Reportes Semanales y Mensuales")
    periodo = st.radio("Selecciona el periodo:", ["Semanal", "Mensual"])
    
    hoy = dt.date.today()
    if periodo == "Semanal":
        inicio_periodo = hoy - dt.timedelta(days=7)
    else:
        inicio_periodo = hoy.replace(day=1)

    df_periodo = st.session_state.data[
        (st.session_state.data["Fecha"] >= pd.Timestamp(inicio_periodo)) &
        (st.session_state.data["Fecha"] <= pd.Timestamp(hoy))
    ]

    st.write("Transacciones del periodo seleccionado:")
    st.dataframe(df_periodo)

    if st.session_state.presupuestos:
        st.write("Diferencias entre lo presupuestado y lo real:")
        resumen = df_periodo.groupby("Categoría")["Monto"].sum()
        diferencias = {
            cat: st.session_state.presupuestos.get(cat, 0) - resumen.get(cat, 0)
            for cat in st.session_state.presupuestos
        }
        st.write(pd.DataFrame(diferencias.items(), columns=["Categoría", "Diferencia"]))

    if st.session_state.metas:
        ahorros = df_periodo[df_periodo["Categoría"] == "Ahorro"]["Monto"].sum()
        st.write(f"Ahorros acumulados en este periodo: {ahorros:.2f}")
        st.write(
            f"Diferencia para alcanzar la meta: {st.session_state.metas['meta'] - ahorros:.2f}"
        )


# Interfaz principal
st.title("App de Finanzas Personales")
menu = st.sidebar.selectbox(
    "Menú",
    ["Registrar Ingresos/Gastos", "Configurar Presupuestos", "Configurar Metas", "Generar Reportes"],
)

if menu == "Registrar Ingresos/Gastos":
    registrar_transaccion()
elif menu == "Configurar Presupuestos":
    configurar_presupuesto()
elif menu == "Configurar Metas":
    configurar_metas()
elif menu == "Generar Reportes":
    generar_reporte()
