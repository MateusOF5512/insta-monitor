# Importação de Bibliotecas:

from teste_plots import *
from teste_variaveis import *
from plots_brasil import *
import streamlit as st

## - Topo e Rodapé da Aplicação:
def topo():
    st.markdown(html_title, unsafe_allow_html=True) #Explorador de Dados Abertos
    st.markdown(""" <style>
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)
    return None

def rodape():
    st.markdown(html_rodape, unsafe_allow_html=True) # ---- by: mateus
    return None

config={"displayModeBar": True,
        "displaylogo": False,
        'modeBarButtonsToRemove': ['zoom2d', 'toggleSpikelines',
                                   'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d',
                                   'hoverClosestCartesian', 'hoverCompareCartesian']}

def brasil1():
    col1A, col2A, col3A, col4A, col5A = st.columns([50, 520, 60, 520, 50])
    with col1A:
        st.text("")
    with col2A:
        st.markdown(html_card_header_AA1, unsafe_allow_html=True)  # Descrição Inicial
        st.plotly_chart(figA1, use_container_width=True, config=config)  # GRÁFICO DE BARRA HORIZONTAL
        st.plotly_chart(figA2, use_container_width=True, config=config)  # GRÁFICO DE BARRA HORIZONTAL
        st.plotly_chart(figA3, use_container_width=True, config=config)  # GRÁFICO DE BARRA HORIZONTAL
    with col3A:
        st.text("")
    with col4A:
        st.markdown(html_card_header_ABB, unsafe_allow_html=True)  # Links importantes
        st.plotly_chart(figA4, use_container_width=True, config=config)  # GRÁFICO DE BARRA HORIZONTAL
    with col5A:
        st.text("")


    col1A, col2A, col3A, col4A, col5A = st.columns([50, 520, 60, 520, 50])
    with col1A:
        st.text("")
    with col2A:
        st.markdown(html_card_header_BA, unsafe_allow_html=True)  # Descrição Inicial
        st.plotly_chart(figB1, use_container_width=True, config=config) # GRÁFICO DE BARRA HORIZONTAL
    with col3A:
        st.text("")
    with col4A:
        st.markdown(html_card_header_BB, unsafe_allow_html=True)  # Links importantes
        st.plotly_chart(figB2, use_container_width=True, config=config)  # GRÁFICO DE BARRA HORIZONTAL
    with col5A:
        st.text("")

    st.write("")

    col1A, col2A, col3A, col4A, col5A = st.columns([50, 520, 60, 520, 50])
    with col1A:
        st.text("")
    with col2A:
        st.markdown(html_card_header_CC, unsafe_allow_html=True)  # Descrição Inicial
        st.plotly_chart(figC1, use_container_width=True, config=config)  # GRÁFICO DE BARRA HORIZONTAL
    with col3A:
        st.text("")
    with col4A:
        st.markdown(html_card_header_CA, unsafe_allow_html=True)  # Descrição Inicial
        st.plotly_chart(figC2, use_container_width=True, config=config)  # GRÁFICO DE BARRA HORIZONTAL
    with col5A:
        st.text("")

    st.write("")

    col1A, col2A, col3A, col4A, col5A = st.columns([50, 520, 60, 520, 50])
    with col1A:
        st.text("")
    with col2A:
        st.markdown(html_card_header_CA, unsafe_allow_html=True)  # Descrição Inicial
        st.dataframe(df)  # GRÁFICO DE BARRA HORIZONTAL
    with col3A:
        st.text("")
    with col4A:
        st.markdown(html_card_header_CC, unsafe_allow_html=True)  # Descrição Inicial
        st.pyplot(figD1)  # GRÁFICO DE BARRA HORIZONTAL
    with col5A:
        st.text("")

    st.markdown("""---""")
    st.write("")
    return None

