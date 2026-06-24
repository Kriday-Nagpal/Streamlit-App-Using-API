import requests
import streamlit as st

st.set_page_config(page_title="Fact Generator")

st.title("🧠 Random Fact Generator")

if st.button("Generate Fact"):

    response = requests.get(
        "https://uselessfacts.jsph.pl/api/v2/facts/random"
    )

    fact = response.json()

    st.subheader("Did You Know?")
    st.write(fact["text"])
