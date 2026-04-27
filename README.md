import streamlit as st
import math

st.title("Ecuación cuadrática")

st.write("Ecuación: ax² + bx + c = 0")

a = st.number_input("a", value=1.0)
b = st.number_input("b", value=0.0)
c = st.number_input("c", value=0.0)

discriminante = b**2 - 4*a*c

if discriminante >= 0:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    st.write(f"Soluciones: x1 = {x1}, x2 = {x2}")
else:
    st.write("No hay soluciones reales")
