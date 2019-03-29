# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 01 - Exemplo 02:
- Plota uma imagem em níveis de cinza com o mapa de cores padrão do matplotlib e 
depois com o mapa de cores cinza (gray).
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
  
# Plota imagens em múltiplas figuras.
# Cria uma nova figura.
plt.figure() 
plt.imshow(im)
plt.title('Mapa de cores padrao')
plt.show()

# Cria uma nova figura.
plt.figure() 
plt.imshow(im, cmap='gray')
plt.title('Mapa de cores alterado - gray')
plt.show()
