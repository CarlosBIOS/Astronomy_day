import streamlit as st
import requests
from os import getenv
from datetime import datetime

url = f'https://api.nasa.gov/planetary/apod?api_key={getenv('Nasa_api_key')}&date={datetime.now().strftime('%Y-%m-%d')}'
response = requests.get(url)
# response.content está em bytes, mas posso usar o json para dicionário

if response.status_code == 200:
    data = response.json()

    image_request = requests.get(data['url'])
    with open('photo_of_day.jpg', 'wb') as file:
        file.write(image_request.content)

    st.title(data['title'])
    st.image('photo_of_day.jpg')
    st.write(data['explanation'])
    print(data)
else:
    print("Erro:", response.status_code)
