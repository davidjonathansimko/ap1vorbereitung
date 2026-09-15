import streamlit as st
import streamlit.components.v1 as components

# Seitenkonfiguration (wichtig: muss ganz oben stehen)
st.set_page_config(page_title="IT-Trainer", layout="wide", page_icon="💻")

# 1. Navigation in der linken Seitenleiste erstellen
st.sidebar.title("Navigation")
auswahl = st.sidebar.radio(
    "Wählen Sie ein Tool aus:",
    ["Netzplan-Trainer", "IP-Subnetting"]
)

# 2. Inhalt basierend auf der Auswahl steuern
if auswahl == "Netzplan-Trainer":
    st.title("🕸️ Ultimativer Netzplan-Trainer & Generator")

    # Hier wird Ihre bestehende Netzplan HTML-Datei geladen
    try:
        with open("netzplan-dynamisch.html", "r", encoding="utf-8") as f:
            html_netzplan = f.read()
        components.html(html_netzplan, height=900, scrolling=True)
    except FileNotFoundError:
        st.error("Die Datei 'netzplan-dynamisch.html' wurde nicht gefunden. Bitte prüfen Sie den Pfad.")

elif auswahl == "IP-Subnetting":
    st.title("🔢 IP-Subnetting Trainer")

    # Hier wird Ihre bestehende Subnetting HTML-Datei geladen
    try:
        with open("ip-subnetting.html", "r", encoding="utf-8") as f:
            html_subnetting = f.read()
        components.html(html_subnetting, height=900, scrolling=True)
    except FileNotFoundError:
        st.error("Die Datei 'ip-subnetting.html' wurde nicht gefunden. Bitte prüfen Sie den Pfad.")
