import streamlit as st

st.title(" Kilogramm ➔ Newton Umrechner")
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

