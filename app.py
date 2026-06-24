import requests
import pandas as pd
import streamlit as st

st.title("🌍 Country Info App")

country = st.text_input("Enter Country", "India")

if st.button("Search"):

    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        if len(data) > 0:

            country_data = data[0]

            info = [{
                "Country": country_data["name"]["common"],
                "Region": country_data["region"],
                "Population": country_data["population"]
            }]

            df = pd.DataFrame(info)

            st.dataframe(df)

        else:
            st.error("No country found")

    else:
        st.error("Country not found")
