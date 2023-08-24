import streamlit as st
from PIL import Image
st.title('Papers, Please ')
st. header("Es un juego donde tienes que sellar pasaportes y detener gente")
st.write("Puedes elegir en que bando jugar")

image = Image.open('pp.jpg')
st.image(image, caption="Logo")

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)


                      


