import streamlit as st
from PIL import Image
import cv2
import numpy as np

from src import home

def main():
    home.style()
    labeling_page()


# Labeling Page
def labeling_page():
    "Show the images and ask the user for a label"
    st.image('data/input/01.jpeg')
    label = st.text_input(label = "Üstteki resimde ne yazıyor?")
    pass    

if __name__ == "__main__":
    main()