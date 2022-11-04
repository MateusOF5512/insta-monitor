# BIBLIOTECAS USADAS

import streamlit as st
from PIL import Image

im = Image.open("instagram.png")
st.set_page_config(page_title="Instagram Monitor", page_icon=im, layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

from teste_pages import *
from pages_brasil import *


# APLICAÇÃO
topo()

tab1, tab2 = st.tabs(["@vtrbrasil", "@ortiz_mateus_"])
with tab1:
    brasil1()
    comentarios()

with tab2:
    parte1()




rodape()



