"""
Created on Tue Feb 8 2022

@author: ZekAI Developper Team
"""


import streamlit as st
from PIL import Image
import cv2
import numpy as np


# Set up app's title and favicon
st.set_page_config(page_title = 'ZekAI | Yazı Etiketleme',
                    page_icon = 'https://avatars.githubusercontent.com/u/97012715?v=4',
                    initial_sidebar_state = "collapsed")


# Main configurations
def main():
    "Call the main necessary functions"
    style()
    home_page()
    sidebar()

def sidebar():
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

def style():
    "Add additional CSS"
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Home Page
def home_page():
    "Open the home page"
    st.title("Yazı Etiketleme")
    import_image()

def load_image(raw_image):
    "Load image with PIL library"
    img = Image.open(raw_image)
    return img

def import_image():
    "Show the image loader"
    raw_image = st.file_uploader("Lütfen bir resim seçiniz:",
                            type = ['jpg', 'jpeg', 'png'])

    if raw_image:
        img = load_image(raw_image)
        st.image(img)
        st.write('Seçilen resimi onaylıyor musunuz?')
        st.button("Onayla", on_click = labeling)


# Labeling Page
def labeling():
    "Show the images and ask the user for a label"
    st.title("Yazı Etiketleme")
    st.image('data/input/01.jpeg')
    label = st.text_input(label = "Üstteki resimde ne yazıyor?")
    pass


# Start the app
if __name__ == "__main__":
    main()