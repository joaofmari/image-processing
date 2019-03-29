# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 01 - Exemplo 04: 
- Mostra uma região de interesse (RdI) retangular de uma imagem.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
from scipy import misc
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
   
# Lê a imagem a partir de um arquivo
im = misc.imread('ascent.tif')

# Cria uma nova figura
plt.figure() 
plt.imshow(im, cmap='gray')
# Get the current axes
axis = plt.gca() 
# Desenha um retangulo com bordas vermelhas com inicio no pixel (200, 200) e com 
# 20 pixels de altura e 20 pixels de largura.
axis.add_patch(Rectangle((200,200), 20, 20, facecolor='none', edgecolor='red'))
plt.title('RdI destacado na imagem')
# Mostra as figuras na tela
plt.show() 

# Cria uma nova figura
plt.figure() 
# Mostra apenas a região de interesse (RdI) da imagem composta pelos pixels 
# entre as linhas 200 e 220 e entre as colunas 200 e 220.
plt.imshow(im[200:220, 200:220], cmap='gray')
plt.title('RdI com 20x20 pixels')

# Cria uma nova figura
plt.figure() 
# Altera o método de interpolação para bilinear.
plt.imshow(im[200:220, 200:220], cmap='gray', interpolation='nearest')
plt.title('RdI interpolado pelo metodo dos vizinhos mais proximos')

# Mostra as figuras na tela
plt.show() 