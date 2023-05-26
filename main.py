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
print(content['date'])
print(content)
print(content['explanation'])

# get the picture from the dataframe
picture_url = content['hdurl']
pic_response = requests.get(picture_url)
picture_content = pic_response.content
print(picture_content)
with open("image.jpg", "wb") as file:
    file.write(picture_content)

#st.set_page_config(page_title="Today's Universe",
#                   page_icon="🧊", layout="centred")

#st.header("Today's Universe")


