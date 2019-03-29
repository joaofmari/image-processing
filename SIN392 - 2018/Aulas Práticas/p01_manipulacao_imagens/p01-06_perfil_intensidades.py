# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 01 - Exemplo 06: 
- Mostra o histograma e a distribuição de intensidades dos pixels ao longo de 
uma seção transversal horizontal de uma imagem.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
from scipy import misc
import matplotlib.pyplot as plt
# Permite desenhar uma reta sobre a imagem.
from matplotlib.patches import  Arrow
  
# Carrega uma imagem a partir de um arquivo
im = misc.imread('ascent.tif')

# Cria uma nova figura
plt.figure() 
# Divide a figura em 2 linhas e 2 colunas.
# +-----+-----+
# |  1  |  2  |
# +-----+-----+
# |  3  |  4  |
# +-----+-----+
# ==> Área ativa é a 1.
plt.subplot(2,2,1) 
plt.imshow(im, cmap='gray')
plt.title('Imagem original')
# ==> Área ativa é a 2.
plt.subplot(2,2,2)  
plt.hist(im.flatten(), 256)
plt.title('Histograma')
# ==> Área ativa é a 3.
plt.subplot(2,2,3) 
plt.imshow(im, cmap='gray')
# Get current axis
axis = plt.gca() 
# Desenha uma linha que começa no pixel (0, 256) e possui 512 pixels de largura 
# e 0 pixels de altura. Ou seja, uma linha horizontal no centro da imagem.
axis.add_patch(Arrow(0, 256, 512, 0, edgecolor='red'))
plt.title('Secao horizontal (linha 256) na imagem')
# ==> A área ativa é a 4.
plt.subplot(2,2,4) 
# Arranjo 1D com os valores dos pixels de todas as colunas da linha 256 (seção 
# transversal da imagem na linha 256).
h_cut = im[256,0::] 
# Plota a distribuição de intensidades na seção transversal.
plt.plot(h_cut)
plt.title('Perfil de intensidade na secao transversal')
plt.show()
