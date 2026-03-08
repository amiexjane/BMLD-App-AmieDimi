import streamlit as st

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/addition_calculator.py", title="Plus_Rechner", icon=":material/info:")
pg_third = st.Page("views/Knopf_Druck.py", title="Klick-Zähler", icon=":material/info:")
pg_fourth = st.Page("views/umrechner.py", title="Kilogramm-Newton Rechner", icon=":material/info:")
pg = st.navigation([pg_home, pg_second, pg_third, pg_fourth])
pg.run()
