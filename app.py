import streamlit as st

# ----------------------------------------
# CONFIGURACIÓN INICIAL
# ----------------------------------------

st.set_page_config(page_title="Proyecto Módulo 1", layout="centered")

# Inicializar lista de actividades en memoria
if "actividades" not in st.session_state:
    st.session_state.actividades = []

# ----------------------------------------
# MENÚ LATERAL
# ----------------------------------------

menu = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ----------------------------------------
# HOME
# ----------------------------------------

if menu == "Home":

    st.title("Proyecto Módulo 1 – Fundamentos de Programación")

    st.write("**Nombre del estudiante:** TU NOMBRE COMPLETO")
    st.write("**Curso:** Especialización en Python for Analytics")
    st.write("**Módulo:** Módulo 1 – Python Fundamentals")
    st.write("**Año:** 2026")

    st.write("""
    Esta aplicación integra los conceptos fundamentales de programación en Python:
    - Variables
    - Condicionales
    - Listas y Diccionarios
    - Funciones
    - Programación Funcional
    - Programación Orientada a Objetos (POO)

    La aplicación permite gestionar actividades financieras y evaluar su desempeño.
    """)

    st.write("**Tecnologías utilizadas:**")
    st.write("- Python")
    st.write("- Streamlit")

# ----------------------------------------
# EJERCICIO 1 – VARIABLES Y CONDICIONALES
# ----------------------------------------

elif menu == "Ejercicio 1":

    st.title("Ejercicio 1 – Verificador de Presupuesto")

    presupuesto = st.number_input("Ingrese el presupuesto:", min_value=0.0)
    gasto = st.number_input("Ingrese el gasto:", min_value=0.0)

    if st.button("Evaluar Presupuesto"):

        diferencia = presupuesto - gasto

        if gasto <= presupuesto:
            st.success("✅ El gasto está dentro del presupuesto.")
        else:
            st.warning("⚠️ El presupuesto ha sido excedido.")

        st.write(f"Diferencia: {diferencia}")

# ----------------------------------------
# EJERCICIO 2 – LISTAS Y DICCIONARIOS
# ----------------------------------------

elif menu == "Ejercicio 2":

    st.title("Ejercicio 2 – Registro de Actividades")

    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo de actividad", ["Marketing", "Operaciones", "Finanzas", "Otro"])
    presupuesto = st.number_input("Presupuesto", min_value=0.0)
    gasto_real = st.number_input("Gasto Real", min_value=0.0)

    if st.button("Agregar Actividad"):

        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }

        st.session_state.actividades.append(actividad)
        st.success("Actividad agregada correctamente")

    if st.session_state.actividades:

        st.subheader("Lista de Actividades")
        st.dataframe(st.session_state.actividades)

        st.subheader("Estado de Actividades")

        for act in st.session_state.actividades:
            if act["gasto_real"] <= act["presupuesto"]:
                st.write(f"{act['nombre']} → Dentro del presupuesto")
            else:
                st.write(f"{act['nombre']} → Presupuesto excedido")

# ----------------------------------------
# EJERCICIO 3 – FUNCIONES Y PROGRAMACIÓN FUNCIONAL
# ----------------------------------------

elif menu == "Ejercicio 3":

    st.title("Ejercicio 3 – Cálculo de Retorno Esperado")

    def calcular_retorno(actividad, tasa, meses):
        return actividad["presupuesto"] * tasa * meses

    tasa = st.slider("Seleccione la tasa", 0.0, 1.0, 0.1)
    meses = st.number_input("Número de meses", min_value=1)

    if st.button("Calcular Retornos"):

        if st.session_state.actividades:

            retornos = list(
                map(
                    lambda act: {
                        "nombre": act["nombre"],
                        "retorno_esperado": calcular_retorno(act, tasa, meses)
                    },
                    st.session_state.actividades
                )
            )

            for r in retornos:
                st.write(f"{r['nombre']} → Retorno esperado: {r['retorno_esperado']}")

        else:
            st.warning("No hay actividades registradas.")

# ----------------------------------------
# EJERCICIO 4 – PROGRAMACIÓN ORIENTADA A OBJETOS
# ----------------------------------------

elif menu == "Ejercicio 4":

    st.title("Ejercicio 4 – Programación Orientada a Objetos")

    class Actividad:

        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        def mostrar_info(self):
            return f"{self.nombre} ({self.tipo}) - Presupuesto: {self.presupuesto}, Gasto: {self.gasto_real}"

    if st.session_state.actividades:

        objetos = [
            Actividad(
                act["nombre"],
                act["tipo"],
                act["presupuesto"],
                act["gasto_real"]
            )
            for act in st.session_state.actividades
        ]

        for obj in objetos:

            st.write(obj.mostrar_info())

            if obj.esta_en_presupuesto():
                st.success("Cumple el presupuesto")
            else:
                st.warning("No cumple el presupuesto")

    else:
        st.warning("No hay actividades registradas.")