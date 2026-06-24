import requests
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Country Info App")

st.title("🌍 Country Info App")

country = st.text_input("Enter Country", "India")

if st.button("Search"):

    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()[0]

        country_info = [{
            "Country": data["name"]["common"],
            "Capital": data["capital"][0],
            "Region": data["region"],
            "Population": data["population"]
        }]

        df = pd.DataFrame(country_info)

        st.dataframe(df)

    else:
        st.error("Country not found")
