"""
Created on Tue Feb 8 2022

@author: ZekAI Developper Team
"""

import streamlit as st
from src.multiapp import MultiApp
from src import home, labeling, how


# Set up app's title and favicon
st.set_page_config(page_title = 'ZekAI | Yazı Etiketleme',
                    page_icon = 'https://avatars.githubusercontent.com/u/97012715?v=4',
                    initial_sidebar_state = "collapsed")

app = MultiApp()

st.markdown("""
# Yazı Etiketleme
""")

#All the pages
app.add_app("Anasayfa", home.main)
app.add_app("Etiketleme", labeling.main)
app.add_app("Yardım", how.main)

# The main app
app.run()