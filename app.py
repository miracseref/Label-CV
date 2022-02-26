"""
Created on Tue Feb 8 2022

@author: ZekAI Developper Team
"""

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import sqlite3


# Set up app's title and favicon
st.set_page_config(page_title = 'ZekAI | Yazı Etiketleme',
                   page_icon = 'https://avatars.githubusercontent.com/u/97012715?v=4',
                   initial_sidebar_state = "collapsed")

                    
#Add additional CSS
with open('src/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("""
# Yazı Etiketleme
""")

tabs = ["Anasayfa", "Yardım"]

page = st.sidebar.radio("Sekmeler", tabs)

if page == "Anasayfa":
    pass

elif page == "Yardım":
    st.write("Yazı etiketleme uygulaması nasıl kullanılır?")