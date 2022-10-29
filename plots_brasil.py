import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import numpy as np
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from teste_variaveis import *

# CARREGANDO OS DADOS:
@st.cache(allow_output_mutation=True)
def get_data( path_brasil ):
    df = pd.read_csv( path_brasil )
    return df

def tratamento_dados(df):
    df['likes']=np.where(df['likes'] == -1, 1, 0) #Convertendo likes -1 para zero
    df['count']=np.where(df['likes'] == 2, 0, 1)
    df = df.astype({"count": np.dtype("int64")})
    df = df.astype({"likes": np.dtype("int64")})
    df['type'].replace('GraphSidecar', 'Coleção de Imagens', inplace = True) #Convertendo nome dos tipo de publicação
    df['type'].replace('GraphImage', 'Imagem Única', inplace = True) #Convertendo nome dos tipo de publicação
    df['inter'] = df['likes'] + df['comments']
    df['dates'] = pd.to_datetime(df['time']).dt.date #Coletando apenas a data da coluna time
    df['weekday'] = pd.to_datetime(df['time']).apply(lambda x: x.weekday()) #Coletando o Dia da Semana da coluna time
    df['Hour'] = pd.to_datetime(df['time']).dt.hour #Coletando a hora da publicação
    conditions = [
        (df['Hour'] >= 6) & (df['Hour'] <= 12),
        (df['Hour'] >= 12) & (df['Hour'] <= 18),
        (df['Hour'] >= 18) & (df['Hour'] <= 24),
        (df['Hour'] >= 0) & (df['Hour'] <= 6)]
    values = ['Manhã', 'Tarde', 'Noite', 'Madrugada']
    df['Turno'] = np.select(conditions, values)

    return df

df = get_data(path_brasil)
df = tratamento_dados(df)

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

df_type = df.groupby('type').agg('sum')
GraphImage_count = df_type["count"].iloc[1]
GraphSidecar_count = df_type["count"].iloc[0]

GraphImage_likes = 1
GraphImage_comments = df_type["comments"].iloc[1]
GraphSidecar_likes = 1
GraphSidecar_comments = df_type["comments"].iloc[0]

labels = ['Imagem Única', "Imagens Coleção"]
colors = ['#8A2BE2', '#483D8B']
figA4 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]],
                       subplot_titles=['Publicações:', 'Likes:', 'Comentários:'])

figA4.add_trace(go.Pie(labels=labels, name="Publicações",
                       values=[GraphImage_count, GraphSidecar_count],
                       textinfo='none', showlegend=True,
                       marker=dict(colors=colors, line=dict(color='#000010', width=2))), 1, 1)

figA4.add_trace(go.Pie(labels=labels, name="Likes",
                       values=[GraphImage_likes, GraphSidecar_likes],
                       textinfo='none', showlegend=True,
                       marker=dict(colors=colors, line=dict(color='#000010', width=2))), 1, 2)

figA4.add_trace(go.Pie(labels=labels, name="Comentários",
                       values=[GraphImage_comments, GraphSidecar_comments],
                       textinfo='none', showlegend=True,
                       marker=dict(colors=colors,
                                   line=dict(color='#000010', width=2))), 1, 3)

figA4.update_traces(hole=.4, hoverinfo="label+name+percent+value",
                    hovertemplate="</br><b>Publicação:</b> %{label} " +
                                  "</br><b>Quantidade:</b>  %{value}" +
                                  "</br><b>Proporção:</b>  %{percent}")
figA4.update_layout(autosize=True,
                   height=270, margin=dict(l=20, r=20, b=20, t=30),
                   legend=dict(font_size=14, orientation="h", yanchor="top",
                               y=-0.05, xanchor="center", x=0.5),
                   paper_bgcolor="#F8F8FF", font={'size': 20})


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
                   z=matriz_c, name="",
                   x=['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                   y=['Madrugada', 'Noite', 'Tarde', 'Manhã'],
                   hovertemplate="</br><b>Dia:</b> %{x}"+
                                 "</br><b>Turno:</b> %{y}"+
                                 "</br><b>Publicações:</b> %{z}",
                   colorscale='Portland'))
figC1.update_layout(autosize=True,
                   height=200, margin=dict(l=1, r=10, b=10, t=15),
                   paper_bgcolor="#F8F8FF", font={'size': 12})



figC2 = go.Figure(data=go.Heatmap(
                   z=matriz_i, name="",
                   x=['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                   y=['Madrugada', 'Noite', 'Tarde', 'Manhã'],
                   hovertemplate="</br><b>Dia:</b> %{x}"+
                                 "</br><b>Turno:</b> %{y}"+
                                 "</br><b>Interações:</b> %{z}",
                   colorscale='Portland'))
figC2.update_layout(autosize=True,
                   height=200, margin=dict(l=1, r=10, b=10, t=15),
                   legend=dict(font_size=12, orientation="h", yanchor="top",
                               y=-0.05, xanchor="center", x=0.5),
                   paper_bgcolor="#F8F8FF", font={'size': 12})



### --------------------------------------
figD1 = plt.subplots()
wordcloud = WordCloud(height=384, background_color='#F9F9FA',
                      min_font_size=8, scale=2.5,
                      regexp=r"[a-zA-z#&]+", max_words=30, min_word_length=4
                      ).generate(' '.join(df['text']))
plt.imshow(wordcloud) # image show
plt.axis('off') # to off the axis of x and y












