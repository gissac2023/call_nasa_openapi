import streamlit as st
import os
import requests

# load api key from environment variable
api_key = os.getenv("nasa_api_key")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
# get infos from api
response = requests.get(url)
content = response.json()
# date
date = content['date']
explanation = content['explanation']
# get the picture from the dataframe
picture_url = content['hdurl']
pic_response = requests.get(picture_url)
picture_content = pic_response.content
with open("image.jpg", "wb") as file:
    file.write(picture_content)
# add streamlit page
st.set_page_config(page_title="Today's Universe",
                   page_icon="🧊")
# add page content
st.markdown("<h1 style='text-align: center; color: grey;'>Today's Universe</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center; color: black;'>{date}</h2>", unsafe_allow_html=True)
st.image("./image.jpg")
st.info(explanation)



