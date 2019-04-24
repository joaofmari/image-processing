# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 03 - Exemplo 03: 
- Filtro da mediana.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

import numpy as np
from scipy import misc
from scipy.ndimage import filters 
from skimage import data, img_as_float
import matplotlib.pyplot as plt

# Carrega a imagem
im = misc.ascent()

# Descomentar esta linha para testar uma imagem com ruído sal e pimenta.
# im = misc.imread('../data/dip_3ed/ch03/ckt_board_saltpep_prob_pt05.tif')

# Converte a o tipo de dado da imagem para float [0..1]
im = img_as_float(im)

# Aplica filtragem pela mediana. Não é realizada por convolução.
# ==============================================================

# Padding por espelhamento (padrão do scipy).
# -------------------------
# Aplica o filtro da mediana com mascara 3x3.
mediana_3x3 = filters.median_filter(im, size=3)
# Aplica o filtro da mediana com mascara 5x5.
mediana_5x5 = filters.median_filter(im, size=5)
# Aplica o filtro da  mediana com mascara 9x9.
mediana_9x9 = filters.median_filter(im, size=9)
# Aplica o filtro da mediana com mascara 5x5.
mediana_11x11 = filters.median_filter(im, size=11)
# Aplica o filtro da  mediana com mascara 9x9.
mediana_25x25 = filters.median_filter(im, size=25)

"""
# (mode='constant', cval=0) --> Padding com valor 0. (descomentar).
# -----------------------------------------------------------------
# Aplica o filtro da mediana com mascara 3x3.
mediana_3x3 = filters.median_filter(im, size=3, mode='constant', cval=0)
# Aplica o filtro da mediana com mascara 5x5.
mediana_5x5 = filters.median_filter(im, size=5, mode='constant', cval=0)
# Aplica o filtro da  mediana com mascara 9x9.
mediana_9x9 = filters.median_filter(im, size=9, mode='constant', cval=0)
# Aplica o filtro da mediana com mascara 5x5.
mediana_11x11 = filters.median_filter(im, size=11, mode='constant', cval=0)
# Aplica o filtro da  mediana com mascara 9x9.
mediana_25x25 = filters.median_filter(im, size=25, mode='constant', cval=0)
"""

# Mostra as imagens na tela.
plt.figure()
plt.subplot(2,3,1)
plt.imshow(im, cmap='gray')
plt.title('Imagem original')
plt.subplot(2,3,2)
plt.imshow(mediana_3x3, cmap='gray')
plt.title('Filtro da mediana - 3x3')
plt.subplot(2,3,3)
plt.imshow(mediana_5x5, cmap='gray')
plt.title('Filtro da mediana - 5x5')
plt.subplot(2,3,4)
plt.imshow(mediana_9x9, cmap='gray')
plt.title('Filtro da mediana - 9x9')
plt.subplot(2,3,5)
plt.imshow(mediana_11x11, cmap='gray')
plt.title('Filtro da mediana - 11x11')
plt.subplot(2,3,6)
plt.imshow(mediana_25x25, cmap='gray')
plt.title('Filtro da mediana - 25x25')

# Mostra as imagens na tela.
plt.figure()
plt.subplot(2,4,1)
plt.imshow(im, cmap='gray')
plt.title('Imagem original')
plt.subplot(2,4,2)
plt.imshow(mediana_3x3, cmap='gray')
plt.title('Filtro da mediana - 3x3')
plt.subplot(2,4,3)
plt.imshow(mediana_5x5, cmap='gray')
plt.title('Filtro da mediana - 5x5')
plt.subplot(2,4,4)
plt.imshow(mediana_9x9, cmap='gray')
plt.title('Filtro da mediana - 9x9')

plt.subplot(2,4,5)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - Original')
plt.subplot(2,4,6)
plt.imshow(mediana_3x3[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - 3x3')
plt.subplot(2,4,7)
plt.imshow(mediana_5x5[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - 5x5')
plt.subplot(2,4,8)
plt.imshow(mediana_9x9[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - 9x9')

plt.show()
