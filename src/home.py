import streamlit as st
from PIL import Image

from src import labeling


# Main configurations
def main():
    "Call the main necessary functions"
    style()
    home_page()

def style():
    "Add additional CSS"
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Home Page
def home_page():
    "Open the home page"
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
        st.button("Onayla", on_click = labeling.main)


# Start the app
if __name__ == "__main__":
    main()