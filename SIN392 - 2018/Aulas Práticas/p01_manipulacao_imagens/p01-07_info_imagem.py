# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 01 - Exemplo 07: 
- Mostra informações básicas sobre a imagem.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
from scipy import misc
  
# Lê a imagem a partir de um arquivo
im = misc.imread('ascent.tif')

# Tipo do objeto que armazena a imagem
print(type(im))
# Forma da imagem
print(im.shape)
# Tipo de dados
print(im.dtype)
# Intensidade mínima e máxima
print(im.min(), im.max())
# Intensidade média e desvio padrão da intensidade
print(im.mean(), im.std())
