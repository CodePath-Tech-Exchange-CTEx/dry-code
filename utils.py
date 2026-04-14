import streamlit as st

def init_session_state():
    if st.session_state.get("logged_in") == None:
        st.session_state["logged_in"] = False

def login():
    st.session_state.logged_in = True

def logout():
    st.session_state.logged_in = False

def render_sidebar():
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)
    st.sidebar.write("This site is copyright Fake Company LLC Inc., 2024")

def render_company_info():
    with st.expander("Company Info"):
        st.write("""
            Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
        """)

def render_links():
    with st.expander("Links"):
        st.markdown("""
            [Google](https://google.com)

            [Gemini](https://gemini.google.com)

            [Streamlit Docs](https://docs.streamlit.io/)
        """)