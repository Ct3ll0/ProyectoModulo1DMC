import streamlit as st

st.title("Proyecto módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

st.image("pythonlogo.png")
st.sidebar.image("dmclogo.png")

modulo=st.sidebar.selectbox("Elija un módulo",["Módulo Listas","Módulo Array","Módulo funciones"]

if modulo == "Módulo Listas":
                            
  valor_inicial=st.number_input("Ingrese el valor inicial",value=0)
  valor_final=st.number_input("Ingrese el valor final",value=1)
  
  lista_numerica=list(range(valor_inicial,valor_final))
  
  st.write(lista_numerica)

elif modulo == "Módulo Array":
  st.write("Estás en el módulo de arreglos")

else:
  st.write("Estás en el módulo de funciones")
