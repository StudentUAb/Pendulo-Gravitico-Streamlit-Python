<h1 align="center">
    <img width="600" src="streamlit.jpg" />
</h1>


<p align="center">
Grafico sobre Pêndulo Gravítico
</p>

<p align="center">
    <img src="angulo-pequeno.gif" ></p>

📌 Minha pagina do Pêndulo Gravítico
------------------
EfolioB de Física Geral, programa que simula o grafico do movimento de um Pêndulo, baseando numa formula para angulos pequenos, o metodo aplicado foi o Huen, este programa também cria um ficheiro .CSV com a tabela com os resultados esperados.
Este programa simula o movimento de um pêndulo amortecido usando o método de Heun. O método de Heun é um método numérico usado para resolver equações diferenciais ordinárias e é usado aqui para aproximar a posição e a velocidade do pêndulo ao longo do tempo.

O programa primeiro define várias variáveis, incluindo a massa e o comprimento do pêndulo, a densidade do ar e o coeficiente de arrasto. Esses valores são usados para calcular as equações de movimento do pêndulo. Ele também define as condições iniciais para o ângulo e a velocidade angular do pêndulo.
O programa então usa um loop while para percorrer as etapas de tempo e atualizar a posição e a velocidade do pêndulo usando o método de Heun. Ele estima o valor do ângulo e da velocidade angular no ponto médio do intervalo de tempo e usa isso para corrigir as estimativas, o que leva a uma solução mais precisa.
Finalmente, o programa plota o ângulo e a velocidade angular do pêndulo ao longo do tempo usando a biblioteca Matplotlib, de modo que permite visualizar o movimento do pêndulo.

O pêndulo gravítico tem um movimento harmónico simples quando todas as forças resistentes não, são consideradas.
Quando as forças resistentes, como a resistência do ar, são apreciáveis então verifica-se uma diminuição exponencial da amplitude e da velocidade angular ao longo do tempo.
Pela análise do gráfico obtido verifica-se que ocorre um amortecimento gradual da amplitude e da velocidade angular devido à resistência do ar. 
 
Utilizamos o Docker para executar esta aplicação, para compilar colocamos na mesma pasta todos os ficheiros e no terminal escrevemos:<br>
<br>
<strong>docker-compose build</strong><br>
<br>
<strong>docker-compose up</strong><br>
<br>
<p align="center">
    <img width="1400" src="stremlitgrafico.jpg" />
</p>
Atenção deve instalar o Docker no seu computador

Ver demo aqui:   http://pendulo.ivo.com.pt:8503<br>
🔧 Tecnologias utilizadas:
------------------

- <strong>Python 3.8.2</strong>
- <strong>Visual Studio Code</strong>
- <strong>MacOS</strong>
- <strong>Docker</strong>
<br>
<br>
Para instalar o Docker: https://docs.docker.com/desktop/install/mac-install/<br>
💬 Fale comigo<br>
------------------<br>
[*Entre em contato comigo*](https://www.linkedin.com/in/ivo-baptista-3712144/)<br>
























