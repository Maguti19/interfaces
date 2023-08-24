import streamlit as st
from PIL import Image
st.title('Papers, Please ')
st. header("Es un juego donde tienes que sellar pasaportes y detener gente")
st.write("Puedes elegir en que bando jugar")

image = Image.open('pp.jpg')
st.image(image, caption="Logo")

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos dos columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Arstotzka")
  st.write("Seguir en el pais")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('correcto')

with col2:
  st.subheader("Ezic")
  modo = st.radio("Escapar del pais", ('tren', 'avion', 'pies'))
  if modo == 'tren':
    st.write('Llegaras rápido a tu destino')
  if modo == 'avion':
    st.write('Llegaras mucho más rápido pero sera caro')
  if modo == 'pies':
    st.write('lo lograras...')
    
st.subheader("visado de pasaporte")
if st.button('aprobado'):
    st.write('Bienvenido a Arstotzka')
else:
  st.write('Denegado')
  

st.subheader("selectbox")
in_mod = st.selectbox(
  "selecciona la modalidad",
  ("Audio", "Visual", "Haptico"),
)
if in_mod == "Audio":
  set_mod = "BOOOOOOOM"
elif in_mod == "Visual":
  set_mod = "Denegado"
elif in_mod == "Haptico":
  set_mod = "Bomba"
st.write("La acción es:" , set_mod)


with st.sidebar:
  st.subheader("Configura la modalidad")
  mod_radio = st.radio(
    "Escoge la modalidad a usar",
    ("Francotirador", "Bomba", "Tranquilizante")
  )
                      


