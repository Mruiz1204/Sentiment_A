from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from deep_translator import GoogleTranslator

try:
    _icon = Image.open('logo_mr.png')
except Exception:
    _icon = "😊"
st.set_page_config(page_title="Análisis de Sentimiento · Miguel Ruiz", page_icon=_icon, layout="centered")

# ---- Estilo personalizado: paleta azul petróleo + terracota (Miguel Ruiz) ----
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Inter:wght@300;400;600&display=swap');
    .stApp {
        background: linear-gradient(135deg, #1b3a4b 0%, #14303d 100%);
        color: #e8eef0;
        font-family: 'Inter', sans-serif;
    }
    .stApp, .stApp p, .stApp li, .stApp span, .stApp label,
    .stMarkdown, [data-testid="stCaptionContainer"],
    [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] * {
        color: #e8eef0 !important;
    }
    h1, h2, h3, h4 { font-family: 'Montserrat', sans-serif !important; color: #e07a5f !important; }
    .stTextInput input, .stTextArea textarea {
        background-color: #f3f6f7 !important; color: #14303d !important;
    }
    input::placeholder, textarea::placeholder { color: #5c7079 !important; }
    [data-testid="stNotification"] * { color: #14303d !important; }
    section[data-testid="stSidebar"] { background: #12272f; }
    section[data-testid="stSidebar"] * { color: #e8eef0 !important; }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 { color: #e07a5f !important; }
    div[data-testid="stExpander"] { border: 1px solid #2a4b57 !important; border-radius: 10px !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h2 style=\"font-family:'Montserrat', sans-serif; font-weight:700; color:#f2cc8f; margin-bottom:0;\">Miguel Ruiz</h2>", unsafe_allow_html=True)
st.title('Análisis de Sentimiento 😊😐😔')
image = Image.open('emoticones.jpg')
st.image(image)
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write(
        "**Polaridad:** indica si el sentimiento expresado en el texto es positivo, negativo o neutral. "
        "Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral."
    )
    st.write(
        "**Subjetividad:** mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo "
        "(hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo."
    )

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:
        trans_text = GoogleTranslator(source="es", target="en").translate(text)
        blob = TextBlob(trans_text)
        polaridad = round(blob.sentiment.polarity, 2)
        subjetividad = round(blob.sentiment.subjectivity, 2)
        st.write('Polaridad: ', polaridad)
        st.write('Subjetividad: ', subjetividad)
        if polaridad > 0.0:
            st.write('Es un sentimiento Positivo 😊')
        elif polaridad < 0.0:
            st.write('Es un sentimiento Negativo 😔')
        else:
            st.write('Es un sentimiento Neutral 😐')
