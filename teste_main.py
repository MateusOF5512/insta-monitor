# BIBLIOTECAS USADAS

import streamlit as st

st.set_page_config(page_title="App Instagram Scrape", page_icon=":mag_right:", layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

from teste_pages import *
from pages_brasil import *


# APLICAÇÃO
topo()

tab1, tab2 = st.tabs(["@ortiz_mateus_", "@vtrbrasil"])
with tab1:
    parte1()

with tab2:
    brasil1()




rodape()



