import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Netzplan-Trainer", layout="wide")

st.title("Ultimativer Netzplan-Trainer & Generator")

# Falls Sie Ihr bestehendes HTML direkt anzeigen lassen möchten:
with open("netzplan-dynamisch.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# HTML in Streamlit rendern (Höhe anpassen falls nötig)
components.html(html_code, height=800, scrolling=True)
