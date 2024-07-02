import streamlit as st

pg = st.navigation([
    st.Page("site/00-Home.py", icon=":material/home:"),
    st.Page("site/01-User_Guide.py", icon=":material/developer_guide:"),
    st.Page("site/02-Upload_Photo.py", icon=":material/upload_file:"),
    st.Page("site/03-Information.py", icon=":material/lightbulb:"),
    st.Page("site/04-About_Us.py", icon=":material/group:"),
])

pg.run()
