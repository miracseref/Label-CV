"""
Created on Tue Feb 8 2022

@author: ZekAI Developper Team
"""

import numpy as np
import streamlit as st
import sqlite3
import cv2
import random


# Set up app's title and favicon
st.set_page_config(page_title = 'ZekAI | Yazı Etiketleme',
                   page_icon = 'https://avatars.githubusercontent.com/u/97012715?v=4',
                   initial_sidebar_state = "collapsed")

                    
#Add additional CSS
# with open('src/style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("""
# Yazı Etiketleme
""")

tabs = ["Anasayfa", "Yardım"]

page = st.sidebar.radio("Sekmeler", tabs)

if page == "Anasayfa":
    image = cv2.imread("data/input/01.jpeg")
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 210, 255, cv2.THRESH_BINARY)
    img_erode = cv2.erode(thresh, kernel, iterations = 2)
    morph = cv2.morphologyEx(img_erode, cv2.MORPH_OPEN, np.ones((7, 8)))
    contours, hierarchy = cv2.findContours(morph,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        if w > 35 and w < 440:
            cv2.drawContours(morph, [contour], -1, (0, 0, 0), -1)

    contours_2, hierarchy_2 = cv2.findContours(morph,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)
    sort_contours_2 = sorted(contours_2, key=lambda a: cv2.boundingRect(a)[0])
    bBoxes = []
    img2 = image.copy()

    for c1 in sort_contours_2:
        x1, y1, w1, h1 = cv2.boundingRect(c1)

        if w1 > 20 and w1 < 500:
            box = image[y1:y1+h1, x1:x1+w1]
            bBoxes.append(box)
            cv2.rectangle(img2, (x1, y1), (x1 + w1, y1 + h1), 
                          (random.randint(0, 255), random.randint(0, 255),
                          random.randint(0, 255)), 2)

    for i in bBoxes:
        displayed_image = st.image(i)
        label = st.text_input("Resimde ne yazıyor?")
        next_image = st.button("Atla")

        if not label:
            break
    

elif page == "Yardım":
    st.write("Yazı etiketleme uygulaması nasıl kullanılır?")