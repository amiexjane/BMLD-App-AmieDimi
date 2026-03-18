from utils.data_manager import DataManager 

from datetime import datetime

import pandas as pd
import streamlit as st

st.title(" Kilogramm ➔ Newton Umrechner")

data_manager = DataManager(fs_protocol="webdav", fs_root_folder="BMLD_App_DB")

if "data_df" not in st.session_state:
    st.session_state["data_df"] = data_manager.load_app_data(
        "data.csv",
        initial_value=pd.DataFrame(columns=["Zeitpunkt", "Kilogramm", "Newton"])
    )
st.divider()
st.caption ("Gib eine Masse in Kilogramm ein oder benutze den Slider")

Kilogramm = st.slider("Slider:", min_value=0.0, max_value=100.0, step=0.1)

Kilogramm = st.number_input(" Kilogramm eingeben:", min_value=0.0, max_value=100.0, value=Kilogramm, step=0.1)

newton = Kilogramm * 9.80665

st.divider ()

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Kilogramm", value=f"{Kilogramm:.1f} kg")

with col2:
    st.metric(label="Newton", value=f"{newton:.4f} N")

st.divider()

st.info("⚠️ Diese Umrechnung gilt nur auf der Erde! Die Gravitationsbeschleunigung beträgt 9.80665 m/s² – auf dem Mond oder anderen Planeten wäre das Ergebnis anders.")

if st.button("Zur Tabelle hinzufügen"):
    neue_zeile = pd.DataFrame([{
        "Zeitpunkt": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "Kilogramm": Kilogramm,
        "Newton": newton
    }])

    st.session_state["data_df"] = pd.concat(
        [st.session_state["data_df"], neue_zeile],
        ignore_index=True
    )
    data_manager.save_user_data(st.session_state["data_df"], "data.csv")
    st.subheader("Verlauf")
st.dataframe(st.session_state["data_df"], use_container_width=True)

if st.button("Verlauf löschen"):
    st.session_state["data_df"] = pd.DataFrame(columns=["Zeitpunkt", "Kilogramm", "Newton"])
    data_manager.save_app_data(st.session_state["data_df"], "data.csv")
    
st.divider()
st.subheader("📊 Verlauf")
st.dataframe(st.session_state["data_df"], use_container_width=True)