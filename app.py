import streamlit as st
st.title("Calculadora de ecuación lineal")

st.write("Ecuación: y = a*x + b")

# Inputs
a = st.number_input("Valor de a", value=1.0)
x = st.number_input("Valor de x", value=0.0)
b = st.number_input("Valor de b", value=0.0)

# Cálculo
y = a * x + b

st.write(f"Resultado: y = {y}")
