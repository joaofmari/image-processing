# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 01 - Exemplo 01:
- Carrega uma imagem a partir do módulo misc do SciPy e grava a imagem em um
arquivo. Carrega a imagem a partir do arquivo e plota na tela.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
from scipy import misc
import matplotlib.pyplot as plt
   
# Carrega a imagem a partir do submódulo scipy.misc
# im = misc.lena() # A imagem da Lena não esta mais disponível
im = misc.ascent()
   
# Grava a imagem 'im' em arquivo com nome 'ascent.tif'
misc.imsave('ascent.tif', im)
 
# Lê a imagem a partir de um arquivo
im2 = misc.imread('ascent.tif')
  
# Plota a imagem
plt.imshow(im)
# Mostra as figuras na tela
plt.show()
