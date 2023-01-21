import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import math

st.set_option('deprecation.showPyplotGlobalUse', False)
# Cabeçalho do programa
st.header("EfolioB de Física")
# Titulo do programa
st.title("Simulador pêndulo gravítico ")


st.sidebar.title("Valores a Simular:")

# Entrada de texto para massa da esfera
massa_input = st.sidebar.text_input("Informe a massa da esfera (g)", "2.6")

# Slider para massa da esfera
massa_slider = st.sidebar.slider("Massa da esfera (g)", 1.0, 10.0, 2.6) # Massa em g

try:
    # Converte a entrada de texto para float
    massa = float(massa_input) if massa_input.strip() else massa_slider
    # Converte massa para kg
    m = massa/1000 # Massa em kg
except ValueError:
    st.warning("Por favor, insira um número válido para a massa.")
    m = massa_slider/1000  # Massa em kg

# Entrada de texto para massa da esfera
length_input = st.sidebar.text_input("Informe o comprimento do fio (m)", "1.0")

# Slider para comprimento do fio
length_slider= st.sidebar.slider("Comprimento do fio (m)", 0.5, 3.0, 1.0)  # Comprimento da corda em metros

try:
    # Converte a entrada de texto para float
    comprimento = float(length_input) if length_input.strip() else length_slider
    # Iguala valores do comprimento em metros
    L = comprimento # Comprimento em metros 
except ValueError:
    st.warning("Por favor, insira um número válido para a massa.")
    L = length_slider # Comprimento em metros 

# Entrada de texto para massa da esfera
radius_input = st.sidebar.text_input("Informe o Raio da esfera (cm)", "30.0")

# Slider para massa da esfera
radius_slider = st.sidebar.slider("Raio da esfera (cm)", 1.0, 20.0, 30.0)  # raio da esfera em cm

try:
    # Converte a entrada de texto para float
    radius = float(radius_input) if radius_input.strip() else radius_slider
    # Converte massa para kg
    R = radius/100 # Raio da esfera em metros
except ValueError:
    st.warning("Por favor, insira um número válido para a massa.")
    R = radius_slider/100  # Raio da esfera em metros

# #carrega gif animado com pendulo no sidebar
gif_pendulo = "angulo-pequeno.gif"
st.sidebar.image(gif_pendulo, width=300)

def run_simulation():
    # constants
    cd = 0.1   # Coeficiente de arrasto aerodinâmico para uma esfera
    rho = 1.28 # Massa específica do ar em kg/m^3
    g = 9.81   # Aceleração da gravidade em m/s^2
 
    # Área frontal do pêndulo
    A = math.pi * R**2 
    
    # Calcula o coeficiente de arrasto aerodinâmico
    b = 1/2 * rho * cd * A
    
    st.sidebar.write("Area frontal - A = {}".format(A))
    st.sidebar.write("Valor do Coeficiente de arrasto aerodinâmico  b = {}".format(b))

    theta0 = 0.05 # Ângulo inicial em radianos
    w0 = 0.0      # Velocidade angular inicial em rad/s 
    t0 = 0.0      # Tempo inicial em s
    h = 0.1       # Passo de tempo em s
    
    # Listas para armazenar resultados
    t = [t0]
    theta = [theta0]
    w = [w0]
    k1x_ = 0
    k1v_ = 0
    k2x_ = 0
    k2v_ = 0
    k1x = [k1x_] * len(t)
    k1v = [k1v_] * len(t)
    k2x = [k2x_] * len(t)
    k2v = [k2v_] * len(t)
    
    # Loop do tempo
    while t[-1] < 100.0:
      # Cálculo dos valores intermediários
        k1x_ = w[-1]
        k1v_ = -math.copysign(1, w[-1]) * (((b*L)/m) * w[-1]**2) - (g / L) * theta[-1]
        k2x_ = w[-1] + k1v_ * h
        k2v_ = -math.copysign(1, w[-1] + k1v_ * h) * (((b*L)/m )* (w[-1] + k1v_ * h)**2) - (g / L) * (theta[-1] + k1x_ * h)
      
        # Atualização dos valores de θ e w
        theta.append(theta[-1] + ((k1x_ + k2x_) / 2.0)*h)
        w.append(w[-1] + ((k1v_ + k2v_) / 2.0)*h)
     
        # Atualização do tempo
        t.append(t[-1] + h)
        
        # Atualiza novos valores para os arrays k1x, k1v, k2x e k2v
        k1x.append(k1x_)
        k1v.append(k1v_)
        k2x.append(k2x_)
        k2v.append(k2v_)
        
    
        fig, ax = plt.subplots()
        # Cria o gráfico para θ com a linha vermelha
        ax.plot(t, theta, 'r')
        
        # Adiciona uma linha para w com a linha azul
        ax.plot(t, w, 'b')
        
        # Adiciona uma legenda
        ax.legend(['theta (rad)', 'w (rad/s)'])
        
        # Adiciona títulos aos eixos
        ax.set_xlabel('Tempo (s)')
        ax.set_ylabel('Theta (rad), w (rad/s)')
    
    # Crie um dataframe das listas t, theta , w , e tambem k1x, k1v, k2x e k2v      
    df = pd.DataFrame({'t (s)': t, 'theta (rad)': theta, 'w (rad/s)': w, 'k1x': k1x, 'k1v': k1v, 'k2x': k2x, 'k2v': k2v})

    # Salva o dataframe em um arquivo CSV
    df.to_csv('pendulum_results_full_heun_Final.csv', index=False)
   
    # Exibe o gráfico   
    st.pyplot(fig)
    
    dfe=pd.read_csv("pendulum_results_full_heun_Final.csv")
    
    # Mostra as primeiras linhas do Dataframe
    st.title("Tabela ")
    
    #imprime tabela direto do array
    st.write(df) 
     
    #imprime tabela que carrega ficheiro
    # st.write(dfe)  

if st.button("Simular Grafico"): # Cria o botão para simular o grafico e a tabela
    run_simulation()
    
    st.text(" Realizado por: Ivo Baptista  ") # texto no final 

