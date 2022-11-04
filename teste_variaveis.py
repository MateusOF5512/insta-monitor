from PIL import Image

# CAMINHO PARA OS DADOS ----------------------------------------------------------------

path = "instagram1.csv"
path_brasil = "instagram_tratado_vtrbrasil.csv"
path_comentarios = "instagram_allcomments.csv"



# - TOPO E RODAPÉ ------------------------------------------------------------------------
html_title="""
<h1 style="font-size:300%; color:#4169e1; font-family:sans-serif;
            text-align:center; ">Instagram Monitor Interativo</h1>
"""
html_rodape="""
<hr style= "display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
  <p style="color:Gainsboro; text-align: center;">Última atualização: 27/10/2022</p>
"""



# - PARTE 1 ------------------------------------------------------------------
## 1.1 - Número de Doses & Vacinas Aplicadas:
html_header_10="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; 
                                  text-align: center; padding: 10px 0; font-size:200%;"
                                  >Monitoramento das Publicações</h2>
  </div>
</div>
"""
html_subheader_11="""
<div class="card">
  <div class="card-body" style="border-radius: 50px 50px 50px 50px; background: #4169E1; 
                                border:solid; border-color: black; border-width: 2px 2px 2px 2px;
                                padding-top: 1px; padding-right: 35px; padding-bottom: 1px; padding-left: 35px; 
                                width: 100%; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; 
                                  font-family:sans-serif; text-align: center; 
                                  padding-top: 15px; padding-right: 15px; padding-bottom: 0px; padding-left: 15px;
                                  font-size:150%;" 
                                  >1.1 - Número de Doses & Vacinas Aplicadas</h3>
  </div>
</div>
"""

html_expanderheader_1_10="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; 
                                  text-align: center; padding: 10px 0; font-size:130%;"
                                  >Selecione o tipo da sua análise:</h2>
  </div>
</div>
"""

html_card_header_AA1="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 1px; padding-bottom: 1px; padding-left: 1px; 
                                  text-align: center;font-size: 120%;" 
                                  >Métricas Globais</h5>
  </div>
</div>
"""

html_card_header_AA="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 10px; 
                                width: 100%; height: 25px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 1px; padding-right: 10px; padding-bottom: 1px; padding-left: 10px; 
                                  text-align: center;font-size: 100%;" 
                                  >Métricas dos Likes</h5>
  </div>
</div>
"""

html_card_header_AA2="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 10px; 
                                width: 100%; height: 25px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 1px; padding-right: 10px; padding-bottom: 1px; padding-left: 10px; 
                                  text-align: center;font-size: 100%;"  
                                  >Métricas dos Comentários</h5>
  </div>
</div>
"""
html_card_header_ABB="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Tipo de Publicação - Quantidade</h5>
  </div>
</div>
"""

html_card_header_AB="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Interações por Tipo de Publicação</h5>
  </div>
</div>
"""


html_card_header_BA="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Média de Interações por Dia da Semana</h5>
  </div>
</div>
"""

html_card_header_BB="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Variação de Interações por Dia</h5>
  </div>
</div>
"""


html_card_header_CA="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Interações por Turno e Dia da Semana</h5>
  </div>
</div>
"""

html_card_header_CC="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Publicações por Turno e Dia da Semana</h5>
  </div>
</div>
"""



#-------------------------------------------------------------------------------------------------------
html_header_20="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; 
                                  text-align: center; padding: 10px 0; font-size:200%;"
                                  >Monitoramento dos Comentários</h2>
  </div>
</div>
"""


html_card_header_2A1="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Comentários</h5>
  </div>
</div>
"""

html_card_header_2A2="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Respostas</h5>
  </div>
</div>
"""

html_card_header_2B1="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Comentários mais Frequêntes</h5>
  </div>
</div>
"""

html_card_header_2B2="""
<div class="card">
  <div class="card-body" style="border-radius: 15px 15px 0px 0px; background: #4169E1;  
                                border:solid; border-color: black; border-width: 1px 1px 1px 1px;
                                padding-top: 1px; padding-right: 20px; padding-bottom: 1px; padding-left: 20px; 
                                width: 100%; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif;
                                  padding-top: 7px; padding-right: 15px; padding-bottom: 1px; padding-left: 15px; 
                                  text-align: center;font-size: 120%;" 
                                  >Respostas mais Frequêntes</h5>
  </div>
</div>
"""