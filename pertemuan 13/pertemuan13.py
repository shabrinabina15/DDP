import streamlit as st

# st.write("Hello Word")
home = st.Page("./pages/dashboard.py", title="Home")
nabung = st.Page("./pages/nabung.py", title="Nabung")

pg = st.navigation({
    "dashboard" : [home],
    "nabung" : [nabung],
})

if "nabung" not in st.session_state:
    st.session_state['nabung'] = []

pg.run()