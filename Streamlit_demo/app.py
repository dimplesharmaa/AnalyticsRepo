import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon= ":tada:", layout="wide")


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/f9a4362d-9a3a-4cfd-9656-3ebfa999ac4f/N7KjkzJmCg.json")

# HEADER #
with st.container():
    st.subheader("Hi, I am Dimple :wave:")
    st.title("A Data Analyst from India")
    st.write("I am passionate about finding ways to use python and VBA to be more efficient")
    st.write("[Learn more >](https://www.linkedin.com/in/dimple-s/)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.subheader("(I don't do anything :joy: )")
        st.write("######")
        st.write( 
            """
            I work as a Data analyst at Criteo. 
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key ='coding')
