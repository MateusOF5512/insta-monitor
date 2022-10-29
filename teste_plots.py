import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import numpy as np
from plotly.subplots import make_subplots
import plotly.express as px

from teste_variaveis import *

# CARREGANDO OS DADOS:
@st.cache(allow_output_mutation=True)
def get_data( path ):
    df = pd.read_csv( path )
    return df



# CARREGANDO BASE DE DADOS PARA ALIMENTAÇÃO DOS GRÁFICOS
df = get_data(path)

num_publi = 44
seguidores = 633
senguindo = 516

figAA1 = go.Figure()
figAA1.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#483D8B",
    value=num_publi,
    title={"text": "<span style='font-size:14px;color:black'>Publicações:</span>"},
    domain={'row': 1, 'column': 1}))
figAA1.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#483D8B",
    value=seguidores,
    title={"text": "<span style='font-size:14px;color:black'>Seguidores:</span>"},
    domain={'row': 1, 'column': 3}))
figAA1.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#483D8B",
    value=senguindo,
    title={"text": "<span style='font-size:14px;color:black'>Seguindo:</span>"},
    domain={'row': 1, 'column': 5}))
figAA1.update_layout(
    paper_bgcolor="#F8F8FF", height=110, margin=dict(l=1, r=1, b=0, t=25),
    grid={'rows': 1, 'columns': 7})

df_metricas = df.describe().reset_index()
num_post_like = df_metricas["likes"].iloc[0]
soma_post_like = int(df['likes'].sum())
media_post_like = df_metricas["likes"].iloc[1]
min_post_like = df_metricas["likes"].iloc[3]
max_post_like = df_metricas["likes"].iloc[7]

figAA = go.Figure()
figAA.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#483D8B",
    value=soma_post_like,
    title={"text": "<span style='font-size:14px;color:black'>Total:</span>"},
    domain={'row': 1, 'column': 1}))
figAA.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#483D8B",
    value=media_post_like,
    title={"text": "<span style='font-size:14px;color:black'>Média:</span>"},
    domain={'row': 1, 'column': 3}))
figAA.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#483D8B",
    value=min_post_like,
    title={"text": "<span style='font-size:14px;color:black'>Mínimo:</span>"},
    domain={'row': 1, 'column': 5}))
figAA.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#483D8B",
    value=max_post_like,
    title={"text": "<span style='font-size:14px;color:black'>Máximo:</span>"},
    domain={'row': 1, 'column': 7}))
figAA.update_layout(
    paper_bgcolor="#F8F8FF", height=80, margin=dict(l=1, r=1, b=0, t=25),
    grid={'rows': 1, 'columns': 9})


soma_post_comments = int(df['comments'].sum())
media_post_comments = df_metricas["comments"].iloc[1]
min_post_comments = df_metricas["comments"].iloc[3]
max_post_comments = df_metricas["comments"].iloc[7]

figAA2 = go.Figure()
figAA2.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#8A2BE2",
    value=soma_post_comments,
    title={"text": "<span style='font-size:14px;color:black'>Total:</span>"},
    domain={'row': 1, 'column': 1}))
figAA2.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#8A2BE2",
    value=media_post_comments,
    title={"text": "<span style='font-size:14px;color:black'>Média:</span>"},
    domain={'row': 1, 'column': 3}))
figAA2.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#8A2BE2",
    value=min_post_comments,
    title={"text": "<span style='font-size:14px;color:black'>Mínimo:</span>"},
    domain={'row': 1, 'column': 5}))
figAA2.add_trace(go.Indicator(
    mode="number",
    number_font_size=40,
    number_font_color="#8A2BE2",
    value=max_post_comments,
    title={"text": "<span style='font-size:14px;color:black'>Máximo:</span>"},
    domain={'row': 1, 'column': 7}))
figAA2.update_layout(
    paper_bgcolor="#F8F8FF", height=80, margin=dict(l=1, r=1, b=0, t=25),
    grid={'rows': 1, 'columns': 9})

# GRAFICO DE PIZZA - TIPO DE PUBLICAÇÃO - QUANTIDADE----------------------------------------------
df_type = df.groupby('type').agg('sum')
GraphImage_count = df_type["private"].iloc[0]
GraphSidecar_count = df_type["private"].iloc[1]

labels = ['Imagem Única', "Imagens Coleção"]

figABB = go.Figure(data=[go.Pie(labels=labels,
                              values=[GraphImage_count, GraphSidecar_count],
                              textinfo='none',
                              showlegend=True,
                              marker=dict(colors=['#8A2BE2', '#483D8B'],
                                          line=dict(color='#000010', width=2)))])
figABB.update_traces(hole=.4, hoverinfo="label+percent+value",
                     hovertemplate="</br><b>Tipo da Publicação:</b> %{label} " +
                                   "</br><b>Publicações desse Tipo:</b>  %{value}" +
                                   "</br><b>Proporção desse Tipo:</b>  %{percent}",
                     domain={'x': [0, 0.7], 'y': [0, 1]})
figABB.update_layout(
                   height=110, margin=dict(l=20, r=20, b=20, t=30),
                   paper_bgcolor="#F8F8FF", font={'size': 20},
                   legend=dict(font_size=14, orientation="h",
                               yanchor="middle", y=0.50, xanchor="center", x=1.1))

### ---------------------------------------------------------------------------------

GraphImage_likes = df_type["likes"].iloc[0]
GraphImage_comments = df_type["comments"].iloc[0]
GraphSidecar_likes = df_type["likes"].iloc[1]
GraphSidecar_comments = df_type["comments"].iloc[1]

labels = ['Imagem Única', "Imagens Coleção"]
colors = ['#8A2BE2', '#483D8B']
figAB = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                       subplot_titles=['Likes', 'Comentários'])

figAB.add_trace(go.Pie(labels=labels, name="Likes",
                              values=[GraphImage_likes, GraphSidecar_likes],
                              textinfo='none',
                              showlegend=True,
                              marker=dict(colors=colors,
                                          line=dict(color='#000010', width=2))), 1, 1)

figAB.add_trace(go.Pie(labels=labels, name="Comentários",
                              values=[GraphImage_comments, GraphSidecar_comments],
                              textinfo='none',
                              showlegend=True,
                              marker=dict(colors=colors,
                                          line=dict(color='#000010', width=2))), 1, 2)

figAB.update_traces(hole=.4, hoverinfo="label+name+percent+value",
                    hovertemplate="</br><b>Tipo da Publicação:</b> %{label} " +
                                  "</br><b>Número de Interações:</b>  %{value}" +
                                  "</br><b>Proporção:</b>  %{percent}")
figAB.update_layout(autosize=True,
                   height=200, margin=dict(l=20, r=20, b=20, t=30),
                   legend=dict(font_size=14, orientation="h", yanchor="top",
                               y=-0.05, xanchor="center", x=0.5),
                   paper_bgcolor="#F8F8FF", font={'size': 20})


## -------------------------------------------------------------------------------------

df['weekday'] = pd.to_datetime(df['time']).apply(lambda x: x.weekday())

### AE2 - GRÁFICO DE BARRA -
df_week = df.groupby('weekday').agg('mean')
df_week_soma = df.groupby('weekday').agg('sum')

values = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
y_like = [df_week['likes'][0], df_week['likes'][1], df_week['likes'][2], df_week['likes'][3],
          df_week['likes'][4], df_week['likes'][5], df_week['likes'][6]]
y_comments = [df_week['comments'][0], df_week['comments'][1], df_week['comments'][2], df_week['comments'][3],
              df_week['comments'][4], df_week['comments'][5], df_week['comments'][6]]
y_num = [df_week_soma['private'][0], df_week_soma['private'][1], df_week_soma['private'][2], df_week_soma['private'][3],
         df_week_soma['private'][4], df_week_soma['private'][5], df_week_soma['private'][6]]
y_num_soma = [df_week_soma['likes'][0], df_week_soma['likes'][1], df_week_soma['likes'][2], df_week_soma['likes'][3],
              df_week_soma['likes'][4], df_week_soma['likes'][5], df_week_soma['likes'][6]]
y_num_comments = [df_week_soma['comments'][0], df_week_soma['comments'][1], df_week_soma['comments'][2], df_week_soma['comments'][3],
                  df_week_soma['comments'][4], df_week_soma['comments'][5], df_week_soma['comments'][6]]

figBA = go.Figure()
figBA.add_trace(go.Bar(
    name='Likes', x=values, y=y_like, text=y_num_soma,
    hovertemplate="</br><b>Média de Likes:</b> %{y:.2f}" +
                   "</br><b>Total de Likes:</b> %{text}",
    textposition='none', marker_color=['#4B0082', '#4B0082', '#4B0082', '#4B0082',
                                       '#4B0082', '#4B0082', '#4B0082']
))
figBA.add_trace(go.Bar(
    name='Comentários', x=values, y=y_comments, text=y_num_comments,
    hovertemplate="</br><b>Média de Comentários:</b> %{y:.2f}" +
                   "</br><b>Total de Comentários:</b> %{text}",
    textposition='none', marker_color=['#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF',
                                       '#00FFFF', '#00FFFF', '#00FFFF']
))
figBA.add_trace(go.Bar(
    name='Publicações', x=values, y=y_num,
    hovertemplate="</br><b>Total de Publicações:</b> %{y}",
    textposition='none', marker_color=['#FFA07A', '#FFA07A', '#FFA07A', '#FFA07A',
                                       '#FFA07A', '#FFA07A', '#FFA07A']
))
figBA.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=11, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=200, barmode='stack', margin=dict(l=1, r=1, b=1, t=1), autosize=True, hovermode="x")
figBA.update_yaxes(
    title_text="Número de Interações",title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')


### --------------------------------------------------------------------------

df['Dates'] = pd.to_datetime(df['time']).dt.date
df_day = df.groupby('Dates').agg('sum').reset_index()

figBB = go.Figure()
figBB.add_trace(go.Scatter(
    x=df_day['Dates'], y=df_day['likes'],
    name='Likes', mode='lines',  hovertemplate=None, xhoverformat="%d %b %y",
    line=dict(width=1, color='#4169E1'), stackgroup='one'))

figBB.add_trace(go.Scatter(
    x=df_day['Dates'], y=df_day['comments'],
    name='Comentários', mode='lines', hovertemplate=None, xhoverformat="%d %b %y",
    line=dict(width=1, color='#D70270'), stackgroup='two'))

figBB.add_trace(go.Scatter(
    x=df_day['Dates'], y=df_day['private'],
    name='Publicações', mode='lines', hovertemplate=None, xhoverformat="%d %b %y",
    line=dict(width=1, color='#FFA07A'), stackgroup='three'))

figBB.update_layout(
    paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF", font={'color': "#000000", 'family': "sans-serif"},
    legend=dict(font_size=12, orientation="h", yanchor="top", y=1.20, xanchor="center", x=0.5),
    height=220, hovermode="x unified", margin=dict(l=1, r=1, b=1, t=1))
figBB.update_xaxes(
    rangeslider_visible=True)
figBB.update_yaxes(
    title_text="Número de Interações", title_font=dict(family='Sans-serif', size=12),
    tickfont=dict(family='Sans-serif', size=9), nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')




### GRAFICO DE CALOR - INTERAÇÕES TURNO E DIA DA SEMANA -------

df['Hour'] = pd.to_datetime(df['time']).dt.hour

conditions = [
        (df['Hour'] >= 6) & (df['Hour'] <= 12),
        (df['Hour'] >= 12) & (df['Hour'] <= 18),
        (df['Hour'] >= 18) & (df['Hour'] <= 24),
        (df['Hour'] >= 0) & (df['Hour'] <= 6)]
values = ['Manhã', 'Tarde', 'Noite', 'Madrugada']
df['Turno'] = np.select(conditions, values)

df_day = df.groupby(['weekday', 'Turno']).agg('sum').reset_index()
df_day['inter'] = df_day['likes'] + df_day['comments']
df_day = df_day[['weekday', 'Turno', 'likes', 'comments', 'inter', 'private']]

dom_1 = 0; dom_2 = df_day["inter"].iloc[2]; dom_3 = df_day["inter"].iloc[1]; dom_4 = df_day["inter"].iloc[0]
seg_1=0; seg_2=0; seg_3=df_day["inter"].iloc[3]; seg_4=0
ter_1=0; ter_2=0; ter_3=df_day["inter"].iloc[5]; ter_4=df_day["inter"].iloc[4]
qua_1=df_day["inter"].iloc[6]; qua_2 = df_day["inter"].iloc[8]; qua_3 = df_day["inter"].iloc[7]; qua_4 = 0
qui_1 = 0; qui_2 = df_day["inter"].iloc[10]; qui_3 = df_day["inter"].iloc[9]; qui_4=0
sex_1=df_day["inter"].iloc[11]; sex_2 = df_day["inter"].iloc[13]; sex_3 = df_day["inter"].iloc[12]; sex_4=0
sab_1 = df_day["inter"].iloc[14]; sab_2 = df_day["inter"].iloc[16]; sab_3 = df_day["inter"].iloc[15]; sab_4=0

dom_1_p=0; dom_2_p=df_day["private"].iloc[2]; dom_3_p = df_day["private"].iloc[1]; dom_4_p = df_day["private"].iloc[0]
seg_1_p=0; seg_2_p=0; seg_3_p=df_day["private"].iloc[3]; seg_4_p=0
ter_1_p=0; ter_2_p=0; ter_3_p=df_day["private"].iloc[5]; ter_4_p=df_day["private"].iloc[4]
qua_1_p=df_day["private"].iloc[6]; qua_2_p = df_day["private"].iloc[8]; qua_3_p = df_day["private"].iloc[7]; qua_4_p = 0
qui_1_p=0; qui_2_p = df_day["private"].iloc[10]; qui_3_p = df_day["private"].iloc[9]; qui_4_p=0
sex_1_p=df_day["private"].iloc[11]; sex_2_p = df_day["private"].iloc[13]; sex_3_p = df_day["private"].iloc[12]; sex_4_p=0
sab_1_p=df_day["private"].iloc[14]; sab_2_p = df_day["private"].iloc[16]; sab_3_p = df_day["private"].iloc[15]; sab_4_p=0

matriz = [[dom_4, seg_4, ter_4, qua_4, qui_4, sex_4, sab_4],
          [dom_3, seg_3, ter_3, qua_3, qui_3, sex_3, sab_3],
          [dom_2, seg_2, ter_2, qua_2, qui_2, sex_2, sab_2],
          [dom_1, seg_1, ter_1, qua_1, qui_1, sex_1, sab_1]]

matr_p = [[dom_4_p, seg_4_p, ter_4_p, qua_4_p, qui_4_p, sex_4_p, sab_4_p],
          [dom_3_p, seg_3_p, ter_3_p, qua_3_p, qui_3_p, sex_3_p, sab_3_p],
          [dom_2_p, seg_2_p, ter_2_p, qua_2_p, qui_2_p, sex_2_p, sab_2_p],
          [dom_1_p, seg_1_p, ter_1_p, qua_1_p, qui_1_p, sex_1_p, sab_1_p]]

figCA = go.Figure(data=go.Heatmap(
                   z=matriz, text=matr_p, name="",
                   x=['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                   y=['Madrugada', 'Noite', 'Tarde', 'Manhã'],
                   hovertemplate="</br><b>Dia:</b> %{x}"+
                                 "</br><b>Turno:</b> %{y}"+
                                 "</br><b>Interações:</b> %{z}",
                   colorscale='Portland'))
figCA.update_layout(autosize=True,
                   height=200, margin=dict(l=1, r=10, b=10, t=15),
                   paper_bgcolor="#F8F8FF", font={'size': 12})



figCB = go.Figure(data=go.Heatmap(
                   z=matr_p, text=matriz, name="",
                   x=['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                   y=['Madrugada', 'Noite', 'Tarde', 'Manhã'],
                   hovertemplate="</br><b>Dia:</b> %{x}"+
                                 "</br><b>Turno:</b> %{y}"+
                                 "</br><b>Publicações:</b> %{z}",
                   colorscale='Portland'))
figCB.update_layout(autosize=True,
                   height=200, margin=dict(l=1, r=10, b=10, t=15),
                   legend=dict(font_size=12, orientation="h", yanchor="top",
                               y=-0.05, xanchor="center", x=0.5),
                   paper_bgcolor="#F8F8FF", font={'size': 12})