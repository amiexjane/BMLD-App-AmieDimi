import streamlit as st
from functions.addition import add

st.title("Addition")

st.write("Hier ist mein Rechner")

with st.form("addition_form"):
    nummer_1 = st.number_input("Nummer1")
    nummer_2 = st.number_input("Nummer2")
    resultat = add(nummer_1, nummer_2)

    submit = st.form_submit_button("Berechnen")

    if submit: 
        resultat = add(nummer_1, nummer_2)
        st.write(resultat)
