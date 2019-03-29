# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 02 - Exemplo 03: 
- Operação de mascaramento usando multiplicação.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

import numpy as np
from scipy import misc, ndimage
import matplotlib.pyplot as plt
 
# Lê a imagem a partir de um arquivo
im = misc.imread('ascent.tif')
# Obtem a forma do arranjo. 
num_l, num_c = im.shape
# Constrói a mascara. 
mascara = np.zeros([num_l, num_c], dtype=float)
mascara[200:300, 350:450] = 1
# Mascaramento usando multiplicação. 
im_rdi = im * mascara

# Plota as imagens em uma figura.
plt.figure() # Cria uma nova figura 
# Divide a área de plotagem: 1 linha e 3 colunas.
plt.subplot(1,3,1) # A área ativa é a 1.
plt.imshow(im, cmap='gray')
plt.axis('off')
plt.title('Imagem original')
plt.subplot(1,3,2) # Agora a área ativa é a 2.
plt.imshow(mascara, cmap='gray')
plt.title('Imagem mascara (binaria)')
plt.subplot(1,3,3) # A área ativa é a 3.
plt.imshow(im_rdi, cmap='gray')
plt.title('RdI isolada por mascaramento')
plt.show()
