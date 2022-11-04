import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import numpy as np
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image


from teste_variaveis import *

# CARREGANDO OS DADOS:
@st.cache(allow_output_mutation=True)
def get_data( path_brasil ):
    df = pd.read_csv( path_brasil )
    return df

def get_data_comentarios( path_comentarios ):
    df_com = pd.read_csv( path_comentarios )
    return df_com


def transforma_dados(df):
    df['count'] = np.where(df['id_comentario'] == 2, 0, 1)

    df['autor_comentario'] = df['autor_comentario'].replace(np.nan, 'Nulo')
    df['autor_resposta'] = df['autor_resposta'].replace(np.nan, 'Nulo')

    df_comentario = df[df['autor_comentario'] != 'Nulo']
    df_comentario = df_comentario[['post_order', 'data_comentario', 'texto_comentario',
                                   'autor_comentario', 'likes_comentario', 'count']]

    df_resposta = df[df['autor_resposta'] != 'Nulo']
    df_resposta = df_resposta[['post_order', 'data_resposta', 'texto_resposta',
                               'autor_resposta', 'likes_resposta', 'count']]
    return df_comentario, df_resposta

def status(df):
    if df['autor_resposta'] != 'Nulo':
        return "comentário com resposta"
    elif (df['autor_comentario'] != 'Nulo') & (df['autor_resposta'] == 'Nulo'):
        return "comentário sem resposta"
    else:
        return "nao sei"


df = get_data(path_brasil)
df_com = get_data_comentarios(path_comentarios)
df_comentario, df_resposta = transforma_dados(df_com)
df_com["status"] = df_com.apply(status, axis=1)

### GRAFICO INDICADOR - MÉTRICAS GLOBAIS, LIKES E COMENTÁRIOS
# DADOS DE ENTRADA:
df_metricas = df.describe().reset_index()
# GRAFICO 1:
num_publi = 16
seguidores = 858
senguindo = 1089
#GRÁFICO 2:
num_post_like = df_metricas["likes"].iloc[0]
soma_post_like = int(df['likes'].sum())
media_post_like = df_metricas["likes"].iloc[1]
min_post_like = df_metricas["likes"].iloc[3]
max_post_like = df_metricas["likes"].iloc[7]
#GRÁFICO 3:
soma_post_comments = int(df['comments'].sum())
media_post_comments = df_metricas["comments"].iloc[1]
min_post_comments = df_metricas["comments"].iloc[3]
max_post_comments = df_metricas["comments"].iloc[7]

# CONFIGURANDO GRAFICO INDICADOR 1 -  METRICAS GLOBAIS
figA1 = go.Figure()
figA1.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=num_publi,
    title={"text": "<span style='font-size:14px;color:black'>Publicações:</span>"},
    domain = {'y': [0, 1], 'x': [0.25, 0.5]}))
figA1.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=seguidores,
    title={"text": "<span style='font-size:14px;color:black'>Seguidores:</span>"},
    domain = {'y': [0, 1], 'x': [0.5, 0.75]}))
figA1.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=senguindo,
    title={"text": "<span style='font-size:14px;color:black'>Seguindo:</span>"},
    domain = {'y': [0, 1], 'x': [0.75, 1]}))
figA1.update_layout(title="Geral ",title_font_color='black',title_font_size=20,
                     title_x=0.03, title_xanchor='left',
                     title_y=0.5, title_yanchor='middle',
    paper_bgcolor="#F8F8FF", height=70, margin=dict(l=10, r=10, b=10, t=30),
    grid={'rows': 1, 'columns': 3})

# CONFIGURANDO GRAFICO INDICADOR 2 -  METRICAS LIKES
figA2 = go.Figure()
figA2.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=soma_post_like,
    title={"text": "<span style='font-size:14px;color:black'>Total:</span>"},
    domain = {'y': [0, 1], 'x': [0.2, 0.4]}))
figA2.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=media_post_like,
    title={"text": "<span style='font-size:14px;color:black'>Média:</span>"},
    domain = {'y': [0, 1], 'x': [0.4, 0.6]}))
figA2.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=min_post_like,
    title={"text": "<span style='font-size:14px;color:black'>Mínimo:</span>"},
    domain = {'y': [0, 1], 'x': [0.6, 0.8]}))
figA2.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=max_post_like,
    title={"text": "<span style='font-size:14px;color:black'>Máximo:</span>"},
    domain = {'y': [0, 1], 'x': [0.8, 1]}))
figA2.update_layout(title="Likes ",title_font_color='black',title_font_size=18,
                     title_x=0.03, title_xanchor='left',
                     title_y=0.5, title_yanchor='middle',
    paper_bgcolor="#F8F8FF", height=70, margin=dict(l=1, r=1, b=1, t=30),
    grid={'rows': 1, 'columns': 4})

# CONFIGURANDO GRAFICO INDICADOR 3 -  METRICAS COMENTÁRIOS
figA3 = go.Figure()
figA3.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#8A2BE2",
    value=soma_post_comments,
    title={"text": "<span style='font-size:14px;color:black'>Total:</span>"},
    domain = {'y': [0, 1], 'x': [0.2, 0.4]}))
figA3.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#8A2BE2",
    value=media_post_comments,
    title={"text": "<span style='font-size:14px;color:black'>Média:</span>"},
    domain = {'y': [0, 1], 'x': [0.4, 0.6]}))
figA3.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#8A2BE2",
    value=min_post_comments,
    title={"text": "<span style='font-size:14px;color:black'>Mínimo:</span>"},
    domain = {'y': [0, 1], 'x': [0.6, 0.8]}))
figA3.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#8A2BE2",
    value=max_post_comments,
    title={"text": "<span style='font-size:14px;color:black'>Máximo:</span>"},
    domain = {'y': [0, 1], 'x': [0.8, 1]}))
figA3.update_layout(title="Comentários",title_font_color='black',title_font_size=18,
                     title_x=0.03, title_xanchor='left',
                     title_y=0.5, title_yanchor='middle',
    paper_bgcolor="#F8F8FF", height=70, margin=dict(l=1, r=1, b=0, t=30),
    grid={'rows': 1, 'columns': 4})


### GRAFICO 2 - PIZZA -
im1 = Image.open("publicacao.jpeg")
im2 = Image.open("like.png")
im3 = Image.open("comentario.png")

df_type = df.groupby('type').agg('sum')
GraphImage_count = df_type["count"].iloc[1]
GraphSidecar_count = df_type["count"].iloc[0]

GraphImage_likes = df_type["likes"].iloc[1]
GraphImage_comments = df_type["comments"].iloc[1]
GraphSidecar_likes = df_type["likes"].iloc[0]
GraphSidecar_comments = df_type["comments"].iloc[0]

labels = ['Imagem Única', "Imagens Coleção"]
colors = ['#8A2BE2', '#483D8B']
figA4 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]],
                      subplot_titles=['Publicações', 'Likes', 'Comentários', ])

figA4.add_trace(go.Pie(labels=labels, name="Publicações",
                       values=[GraphImage_count, GraphSidecar_count],
                       textinfo='none', showlegend=True,
                       domain={'y': [0, 1], 'x': [0, 0.3]},
                       marker=dict(colors=colors, line=dict(color='#000010', width=2))))

figA4.add_trace(go.Pie(labels=labels, name="Likes",
                       values=[GraphImage_likes, GraphSidecar_likes],
                       textinfo='none', showlegend=True,
                       domain={'y': [0, 1], 'x': [0.35, 0.65]},
                       marker=dict(colors=colors, line=dict(color='#000010', width=2))))
figA4.add_trace(go.Pie(labels=labels, name="Comentários",
                       values=[GraphImage_comments, GraphSidecar_comments],
                       textinfo='none', showlegend=True,
                       domain={'y': [0, 1], 'x': [0.7, 1]},
                       marker=dict(colors=colors, line=dict(color='#000010', width=2))))

figA4.update_traces(hole=.8, hoverinfo="label+name+percent+value",
                    hovertemplate="</br><b>Publicação:</b> %{label} " +
                                  "</br><b>Quantidade:</b>  %{value}" +
                                  "</br><b>Proporção:</b>  %{percent}")
figA4.update_layout(autosize=True,
                   height=270, margin=dict(l=10, r=10, b=2, t=40),
                   legend=dict(font_size=14, orientation="h", yanchor="top",
                               y=-0.05, xanchor="center", x=0.5),
                   paper_bgcolor="#F8F8FF", font={'size': 20})

figA4.add_layout_image(dict(source=im1, xref="paper", yref="paper", x=0.095, y=0.65,
                          sizex=0.3, sizey=0.3))
figA4.add_layout_image(dict(source=im2, xref="paper", yref="paper", x=0.445, y=0.65,
                          sizex=0.3, sizey=0.3))
figA4.add_layout_image(dict(source=im3, xref="paper", yref="paper", x=0.75, y=0.65,
                          sizex=0.3, sizey=0.3))


### GRAFICO 5 - BARRA -
df_week = df.groupby('weekday').agg('mean')
df_week_soma = df.groupby('weekday').agg('sum')

values = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
y_like = [df_week['likes'][0], df_week['likes'][1], df_week['likes'][2], df_week['likes'][3],
          df_week['likes'][4], df_week['likes'][5], df_week['likes'][6]]
y_comments = [df_week['comments'][0], df_week['comments'][1], df_week['comments'][2], df_week['comments'][3],
              df_week['comments'][4], df_week['comments'][5], df_week['comments'][6]]
y_num = [df_week_soma['count'][0], df_week_soma['count'][1], df_week_soma['count'][2], df_week_soma['count'][3],
         df_week_soma['count'][4], df_week_soma['count'][5], df_week_soma['count'][6]]
y_num_soma = [df_week_soma['likes'][0], df_week_soma['likes'][1], df_week_soma['likes'][2], df_week_soma['likes'][3],
              df_week_soma['likes'][4], df_week_soma['likes'][5], df_week_soma['likes'][6]]
y_num_comments = [df_week_soma['comments'][0], df_week_soma['comments'][1], df_week_soma['comments'][2], df_week_soma['comments'][3],
                  df_week_soma['comments'][4], df_week_soma['comments'][5], df_week_soma['comments'][6]]

figB1 = go.Figure()
figB1.add_trace(go.Bar(
    name='Likes', x=values, y=y_like, text=y_num_soma,
    hovertemplate="</br><b>Média de Likes:</b> %{y:.2f}" +
                   "</br><b>Total de Likes:</b> %{text}",
    textposition='none', marker_color=['#4B0082', '#4B0082', '#4B0082', '#4B0082',
                                       '#4B0082', '#4B0082', '#4B0082']
))
figB1.add_trace(go.Bar(
    name='Comentários', x=values, y=y_comments, text=y_num_comments,
    hovertemplate="</br><b>Média de Comentários:</b> %{y:.2f}" +
                   "</br><b>Total de Comentários:</b> %{text}",
    textposition='none', marker_color=['#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF',
                                       '#00FFFF', '#00FFFF', '#00FFFF']
))
figB1.add_trace(go.Bar(
    name='Publicações', x=values, y=y_num,
    hovertemplate="</br><b>Total de Publicações:</b> %{y}",
    textposition='none', marker_color=['#FFA07A', '#FFA07A', '#FFA07A', '#FFA07A',
                                       '#FFA07A', '#FFA07A', '#FFA07A']
))
figB1.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=11, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=200, barmode='stack', margin=dict(l=1, r=1, b=1, t=1), autosize=True, hovermode="x")
figB1.update_yaxes(
    title_text="Número de Interações",title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')


### GRAFICO 6 - LINHA -
df_day = df.groupby('dates').agg('sum').reset_index()

figB2 = go.Figure()
figB2.add_trace(go.Scatter(
    x=df_day['dates'], y=df_day['likes'],
    name='Likes', mode='lines',  hovertemplate=None, xhoverformat="%d %b %y",
    line=dict(width=1, color='#4169E1'), stackgroup='one'))

figB2.add_trace(go.Scatter(
    x=df_day['dates'], y=df_day['comments'],
    name='Comentários', mode='lines', hovertemplate=None, xhoverformat="%d %b %y",
    line=dict(width=1, color='#D70270'), stackgroup='two'))

figB2.add_trace(go.Scatter(
    x=df_day['dates'], y=df_day['count'],
    name='Publicações', mode='lines', hovertemplate=None, xhoverformat="%d %b %y",
    line=dict(width=1, color='#FFA07A'), stackgroup='three'))

figB2.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=12, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=220, hovermode="x unified", margin=dict(l=1, r=1, b=1, t=1))
figB2.update_xaxes(
    rangeslider_visible=True)
figB2.update_yaxes(
    title_text="Número de Interações", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

###

df_day = df.groupby(['weekday', 'Turno']).agg('sum').reset_index()
df_day = df_day[['weekday', 'Turno', 'likes', 'comments', 'inter', 'count']]

dom_1 = 0; dom_2 = df_day["inter"].iloc[0]; dom_3=0; dom_4=0
seg_1=0; seg_2=0; seg_3=df_day["inter"].iloc[1]; seg_4=0
ter_1=0; ter_2=0; ter_3=df_day["inter"].iloc[2]; ter_4=df_day["inter"].iloc[4]
qua_1=df_day["inter"].iloc[3]; qua_2 = df_day["inter"].iloc[4]; qua_3=0; qua_4 = 0
qui_1=0; qui_2=df_day["inter"].iloc[5]; qui_3=0; qui_4=0
sex_1=0; sex_2 = df_day["inter"].iloc[7]; sex_3 = df_day["inter"].iloc[6]; sex_4=0
sab_1 = df_day["inter"].iloc[8]; sab_2 = df_day["inter"].iloc[10]; sab_3 = df_day["inter"].iloc[9]; sab_4=0

matriz_i = [[dom_4, seg_4, ter_4, qua_4, qui_4, sex_4, sab_4],
          [dom_3, seg_3, ter_3, qua_3, qui_3, sex_3, sab_3],
          [dom_2, seg_2, ter_2, qua_2, qui_2, sex_2, sab_2],
          [dom_1, seg_1, ter_1, qua_1, qui_1, sex_1, sab_1]]

dom_1 = 0; dom_2 = df_day["count"].iloc[0]; dom_3=0; dom_4=0
seg_1=0; seg_2=0; seg_3=df_day["count"].iloc[1]; seg_4=0
ter_1=0; ter_2=0; ter_3=df_day["count"].iloc[2]; ter_4=df_day["count"].iloc[4]
qua_1=df_day["count"].iloc[3]; qua_2 = df_day["count"].iloc[4]; qua_3=0; qua_4 = 0
qui_1=0; qui_2=df_day["count"].iloc[5]; qui_3=0; qui_4=0
sex_1=0; sex_2 = df_day["count"].iloc[7]; sex_3 = df_day["count"].iloc[6]; sex_4=0
sab_1 = df_day["count"].iloc[8]; sab_2 = df_day["count"].iloc[10]; sab_3 = df_day["count"].iloc[9]; sab_4=0

matriz_c = [[dom_4, seg_4, ter_4, qua_4, qui_4, sex_4, sab_4],
          [dom_3, seg_3, ter_3, qua_3, qui_3, sex_3, sab_3],
          [dom_2, seg_2, ter_2, qua_2, qui_2, sex_2, sab_2],
          [dom_1, seg_1, ter_1, qua_1, qui_1, sex_1, sab_1]]

figC1 = go.Figure(data=go.Heatmap(
                   z=matriz_c, name="",text=matriz_c,
                   x=['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                   y=['Madrugada', 'Noite', 'Tarde', 'Manhã'],
                   texttemplate="%{text}",
                   hovertemplate="</br><b>Dia:</b> %{x}"+
                                 "</br><b>Turno:</b> %{y}"+
                                 "</br><b>Publicações:</b> %{z}",
                   colorscale='Portland'))
figC1.update_layout(autosize=True,
                   height=200, margin=dict(l=1, r=10, b=10, t=15),
                   paper_bgcolor="#F8F8FF", font={'size': 12})



figC2 = go.Figure(data=go.Heatmap(
                   z=matriz_i, name="", text=matriz_i,
                   x=['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                   y=['Madrugada', 'Noite', 'Tarde', 'Manhã'],
                   texttemplate="%{text}",
                   hovertemplate="</br><b>Dia:</b> %{x}"+
                                 "</br><b>Turno:</b> %{y}"+
                                 "</br><b>Interações:</b> %{z}",
                   colorscale='Portland'))
figC2.update_layout(autosize=True,
                   height=200, margin=dict(l=1, r=10, b=10, t=15),
                   legend=dict(font_size=12, orientation="h", yanchor="top",
                               y=-0.05, xanchor="center", x=0.5),
                   paper_bgcolor="#F8F8FF", font={'size': 12})



words = ' '.join(df['text'])

figC3, ax = plt.subplots()
wordcloud = WordCloud(
                    height=200,
                    min_font_size=8,
                    scale=2.5,
                    background_color='#F9F9FA',
                    max_words=50,
                    min_word_length=2).generate(words)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off') # to off the axis of x and



### -------------------------------------



df_metricas = df_com.describe().reset_index()

# Comentarios metricas:
TOTAL_C = df_metricas["likes_comentario"].iloc[0]
MEDIA_C = int(TOTAL_C /15)
TOTAL_LIKES_C = df_com["likes_comentario"].sum()
MEDIA_LIKES_C = df_metricas["likes_comentario"].iloc[1]
# Respostas metricas:
TOTAL_R = df_metricas["likes_resposta"].iloc[0]
MEDIA_R = int(TOTAL_R /15)
TOTAL_LIKES_R = df_com["likes_resposta"].sum()
MEDIA_LIKES_R = df_metricas["likes_resposta"].iloc[1]
#GRÁFICO 3:

figD1 = go.Figure()
figD1.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=TOTAL_C,
    title={"text": "<span style='font-size:14px;color:black'>Total:</span>"},
    domain = {'y': [0, 1], 'x': [0, 0.25]}))
figD1.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=MEDIA_C,
    title={"text": "<span style='font-size:14px;color:black'>Média:</span>"},
    domain = {'y': [0, 1], 'x': [0.25, 0.5]}))
figD1.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=TOTAL_LIKES_C,
    title={"text": "<span style='font-size:14px;color:black'>Média de Likes:</span>"},
    domain = {'y': [0, 1], 'x': [0.5, 0.75]}))
figD1.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=MEDIA_LIKES_C,
    title={"text": "<span style='font-size:14px;color:black'>Máx de Likes:</span>"},
    domain = {'y': [0, 1], 'x': [0.75, 1]}))
figD1.update_layout(
    paper_bgcolor="#F8F8FF", height=70, margin=dict(l=10, r=10, b=10, t=30),
    grid={'rows': 1, 'columns': 3})




figD2 = go.Figure()
figD2.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=TOTAL_R,
    title={"text": "<span style='font-size:14px;color:black'>Total:</span>"},
    domain = {'y': [0, 1], 'x': [0, 0.25]}))
figD2.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=MEDIA_R,
    title={"text": "<span style='font-size:14px;color:black'>Média:</span>"},
    domain = {'y': [0, 1], 'x': [0.25, 0.5]}))
figD2.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=TOTAL_LIKES_R,
    title={"text": "<span style='font-size:14px;color:black'>Total de Likes:</span>"},
    domain = {'y': [0, 1], 'x': [0.5, 0.75]}))
figD2.add_trace(go.Indicator(
    mode="number",
    number_font_size=30,
    number_font_color="#483D8B",
    value=MEDIA_LIKES_R,
    title={"text": "<span style='font-size:14px;color:black'>Média de Likes:</span>"},
    domain = {'y': [0, 1], 'x': [0.75, 1]}))
figD2.update_layout(
    paper_bgcolor="#F8F8FF", height=70, margin=dict(l=10, r=10, b=10, t=30),
    grid={'rows': 1, 'columns': 3})




###############################################################################################


### AA2 - GRÁFICO PIZZA - Proporção por Tipo de Postagem
# Selecionado os dados para plotagem:
df_status = df_com["status"].value_counts().reset_index()
com_resposta = df_status["status"].iloc[1]
sem_resposta = df_status["status"].iloc[0]
im3 = Image.open("respostas.png")

# Plotagem do Gráfico de Pizza
figD3 = go.Figure(data=[go.Pie(labels=['Comentários com Resposta', "Comentários sem Resposta"],
                     values=[com_resposta, sem_resposta],
                     textinfo='none', showlegend=True,
                     marker=dict(colors=['#8A2BE2', '#483D8B'],
                                 line=dict(color='#000010', width=2))
                            )])
figD3.update_traces(hole=.8, hoverinfo="label+name+percent+value",
                    hovertemplate="</br><b>Publicação:</b> %{label} " +
                                  "</br><b>Quantidade:</b>  %{value}" +
                                  "</br><b>Proporção:</b>  %{percent}")
figD3.update_layout(height=200, margin=dict(l=1, r=1, b=10, t=40),
                  legend=dict(font_size=14, orientation="h", yanchor="top",
                               y=1.25, xanchor="center", x=0.5),
                  paper_bgcolor="#F8F8FF", font={'size': 16})

figD3.add_layout_image(dict(source=im3, xref="paper", yref="paper", x=0.45, y=0.7,
                          sizex=0.4, sizey=0.4))

################################################################################

df_post_comentario = df_comentario.groupby(['post_order']).agg('sum').reset_index()
df_post_resposta = df_resposta.groupby(['post_order']).agg('sum').reset_index()

values = df_post_comentario['post_order']
y_comentario = df_post_comentario['count']
y_resposta = df_post_resposta['count']

figE1 = go.Figure()
figE1.add_trace(go.Bar(
    name='Comentários', x=values, y=y_comentario,
    hovertemplate="</br><b>Comentários:</b> %{y:.2f}",
    textposition='none', marker_color=('#4B0082')
))
figE1.add_trace(go.Bar(
    name='Respostas', x=values, y=y_resposta,
    hovertemplate="</br><b>Respostas:</b> %{y:.2f}",
    textposition='none', marker_color=('#4B0011')
))

figE1.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=12, orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
    height=200, barmode='group', margin=dict(l=2, r=2, b=2, t=2), autosize=True, hovermode="x")
figE1.update_yaxes(
    title_text="Comentários", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')
figE1.update_xaxes(
    title_text="Ordem das Publicações", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=20, showgrid=False)


y_comentario = df_post_comentario['likes_comentario']
y_resposta = df_post_resposta['likes_resposta']


figE2 = go.Figure()
figE2.add_trace(go.Bar(
    name='Likes Comentários', x=values, y=y_comentario,
    hovertemplate="</br><b>Comentários:</b> %{y:.2f}",
    textposition='none', marker_color=('#4B0082')
))
figE2.add_trace(go.Bar(
    name='Likes Respostas', x=values, y=y_resposta,
    hovertemplate="</br><b>Respostas:</b> %{y:.2f}",
    textposition='none', marker_color=('#4B0011')
))

figE2.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=11, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=200, barmode='group', margin=dict(l=1, r=1, b=1, t=1), autosize=True, hovermode="x")
figE2.update_yaxes(
    title_text="Likes",title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')
figE2.update_xaxes(
    title_text="Ordem das Publicações",title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=20, showgrid=False)


###########################################################################

df_autor_respos = df_resposta.groupby(['autor_resposta']).agg('sum').reset_index()
df_autor_respos = df_autor_respos.sort_values('count', ascending=False)

df_autor_comen = df_comentario.groupby(['autor_comentario']).agg('sum').reset_index()
df_autor_comen = df_autor_comen.sort_values('count', ascending=False)[:10]

values = df_autor_comen['autor_comentario']
y_count = df_autor_comen['count']
y_likes = df_autor_comen['likes_comentario']


figF1 = go.Figure()
figF1.add_trace(go.Bar(
    name='Comentários', x=values, y=y_count,
    hovertemplate="</br><b>Comentários:</b> %{y:.2f}",
    textposition='none', marker_color=('#4B0082')
))
figF1.add_trace(go.Bar(
    name='Likes Comentários', x=values, y=y_likes,
    hovertemplate="</br><b>Respostas:</b> %{y:.2f}",
    textposition='none', marker_color=('#4B0011'),
))

figF1.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=11, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=200, barmode='group', margin=dict(l=20, r=2, b=2, t=1), autosize=True, hovermode="x")
figF1.update_yaxes(
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')
figF1.update_xaxes(
    tickfont=dict(family='Sans-serif', size=8), nticks=20, showgrid=False)

values = df_autor_respos['autor_resposta']
y_count = df_autor_respos['count']
y_likes = df_autor_respos['likes_resposta']

figF2 = go.Figure()
figF2.add_trace(go.Bar(
    name='Respostas', x=values, y=y_count,
    hovertemplate="</br><b>Comentários:</b> %{y:.2f}",
    textposition='none', marker_color=('#4B0082')
))
figF2.add_trace(go.Bar(
    name='Likes Respostas', x=values, y=y_likes,
    hovertemplate="</br><b>Respostas:</b> %{y:.2f}",
    textposition='none', marker_color=('#4B0011')
))
figF2.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=11, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=200, barmode='group', margin=dict(l=20, r=1, b=1, t=1), autosize=True, hovermode="x")
figF2.update_yaxes(
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')
figF2.update_xaxes(
    tickfont=dict(family='Sans-serif', size=9), nticks=20, showgrid=False)




###############################################################################

words = ' '.join(df_comentario['texto_comentario'])

figG1, ax = plt.subplots()
wordcloud = WordCloud(
                    width=500,
                    height=300,
                    min_font_size=10,
                    scale=2.5,
                    background_color='#F9F9FA',
                    colormap='plasma',
                    max_words=50,
                    min_word_length=2,
                        ).generate(words)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off') # to off the axis of x and


words = ' '.join(df_resposta['texto_resposta'])

figG2, ax = plt.subplots()
wordcloud = WordCloud(
                    height=250,
                    min_font_size=10,
                    scale=2.5,
                    background_color='#F9F9FA',
                    max_words=50,
                    min_word_length=2,
                        ).generate(words)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off') # to off the axis of x and

