# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 01 - Exemplo 05: 
- Multiplas imagens (plots) em uma única figura.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
from scipy import misc
import matplotlib.pyplot as plt

# Carrega a imagem a partir de um arquivo.
im = misc.imread('ascent.tif')

# Cria uma nova figura 
plt.figure() 
# Divide a área de plotagem: 1 linha e 2 colunas.
# A área ativa é a 1.
plt.subplot(1,2,1) 
plt.imshow(im)
plt.axis('off')
plt.title('Imagem sem os eixos')
# Agora a área ativa é a 2.
plt.subplot(1,2,2) 
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.title('Imagem (gray) com barra de cores')

plt.show()
