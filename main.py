"""
Created on Tue Feb 8 2022

@author: ZekAI Developper Team
"""

import streamlit as st
from PIL import Image
# import cv2
# import numpy as np

def main():
    config()
    styling()
    welcome()
    import_image()

def config():
    st.set_page_config(page_title = 'ZekAI | Yazı Etiketleme',
                       page_icon = 'https://avatars.githubusercontent.com/u/97012715?v=4')
    # hide_streamlit_components()

def welcome():
    st.title("Yazı Etiketleme")

def load_image(raw_image):
    img = Image.open(raw_image)
    return img

def import_image():
    raw_image = st.file_uploader("Lütfen bir resim seçiniz.",
                            type = ['jpg', 'jpeg', 'png'])

    if raw_image:
        img = load_image(raw_image)
        st.image(img)
        st.write('Seçilen resimi onaylıyor musunuz?')
        st.button("Onayla", on_click = labeling())

def labeling():
    st.image('data/input/01.jpeg')
    label = st.text_input(label = "Üstteki resimde ne yazıyor?")
    pass

def hide_streamlit_components():
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)

def styling():
    st.markdown(""" <style>
    body {text-align: center;}
    </style> """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()