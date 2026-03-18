import streamlit as st

import pandas as pd

from utils.data_manager import DataManager
from utils.login_manager import LoginManager

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/addition_calculator.py", title="Plus_Rechner", icon=":material/info:")
pg_third = st.Page("views/Knopf_Druck.py", title="Klick-Zähler", icon=":material/info:")
pg_fourth = st.Page("views/umrechner.py", title="Kilogramm-Newton Rechner", icon=":material/info:")
pg = st.navigation([pg_home, pg_second, pg_third, pg_fourth])
pg.run()

data_manager = DataManager(fs_protocol="webdav", fs_root_folder="BMLD_App_DB")
login_manager = LoginManager(data_manager)

login_manager.login_register()

if "data_df" not in st.session_state:
    st.session_state["data_df"] = data_manager.load_user_data(
        "data.csv",
        initial_value=pd.DataFrame(columns=["Zeitpunkt", "Kilogramm", "Newton"])
    )
    st.session_state["username"]