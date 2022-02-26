import numpy as np
import cv2
import random
import sqlite3
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

def main():
    config()
    upload_image()


def config():
    # Set up app's title and favicon
    st.set_page_config(page_title = 'ZekAI | Veri Tabanı Güncelleme',
                    page_icon = 'https://avatars.githubusercontent.com/u/97012715?v=4',
                    initial_sidebar_state = "collapsed")

    #Add additional CSS
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Header
    st.markdown("""
    # Veri Tabanı Güncelleme
    """)

def insert_blob(image):
    try:
        connection = sqlite3.connect("raw_images.db")
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS handwritten
                        (image BLOB NOT NULL)""")
        cursor.execute("""INSERT INTO handwritten
                        (image) VALUES (?)""", (image,))
        connection.commit()
        cursor.close()
        st.success("Resim başarıyla veri tabanına kaydedilmiştir.")

    except sqlite3.Error as error:
        st.error("Failed to insert image into the database.", error)

    finally:
        if connection:
            connection.close()


def upload_image():
    uploaded_image = st.file_uploader("Lütfen bir resim seçiniz:",
                            type = ['jpg', 'jpeg', 'png'])

    if uploaded_image:
        st.image(uploaded_image)
        st.write('Seçilen resimi onaylıyor musunuz?')
        confirm = st.button("Onayla")

        if confirm:
            #convert to binary for uploading into the database
            binary_image = uploaded_image.read()
            insert_blob(binary_image)

            #convert to numpy array for processing with opencv
            image = Image.open(uploaded_image)
            image = np.array(image)
            word_detect(image)



def word_detect(image):
    """Crop words from text detected in an image."""

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
    cv2.rectangle(
                  image,
                  (0, 0),
                  (image.shape[1], image.shape[0]),
                  (255, 255, 255),
                  15
                )
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    t, thresh = cv2.threshold(img_gray, 210, 255, cv2.THRESH_BINARY)
    img_erode = cv2.erode(thresh, kernel, iterations = 2)
    morph = cv2.morphologyEx(img_erode, cv2.MORPH_OPEN, np.ones((7, 8)))
    contours, hierarchy = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:
        x, y, w, hierarchy = cv2.boundingRect(contour)

        if w > 35 and w < 440:
            cv2.drawContours(morph, [contour], -1, (0, 0, 0), -1)


    contours_2, hierarchy_2 = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    sort_contours_2 = sorted(contours_2, key=lambda a: cv2.boundingRect(a)[0])
    bBoxes = []
    img2 = image.copy()

    for c1 in sort_contours_2:
        x1, y1, w1, hierarchy_2 = cv2.boundingRect(c1)

        if w1 > 20 and w1 < 500:
            box = image[y1:y1+hierarchy_2, x1:x1+w1]
            bBoxes.append(box)
            cv2.rectangle(img2, (x1, y1), (x1 + w1, y1 + hierarchy_2), 
                          (random.randint(0, 255), random.randint(0, 255),
                          random.randint(0, 255)), 2)

    for i in bBoxes:
        displayed_image = st.image(i)
        label = st.text_input("Resimde ne yazıyor?")
        next_image = st.button("Atla")

        if not label:
            break
    



if __name__ == "__main__":
    main()