# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 01 - Exemplo 03:
- Plota uma imagem em uma figura sem as informações nos eixos e em uma figura 
com a barra de cores. 
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
from scipy import misc
import matplotlib.pyplot as plt
   
# Carrega a imagem a partir de um arquivo
im = misc.imread('ascent.tif')
  
# Cria uma nova figura.
plt.figure() 
plt.imshow(im)
plt.colorbar() 
plt.title('Mostra a barra de cores')

# Cria uma nova figura.
plt.figure() 
plt.imshow(im, cmap='gray')
plt.title('Plota a figura sem informacoes sobre os eixos')
plt.axis('off') 

# Mostra as figuras na tela
plt.show()
