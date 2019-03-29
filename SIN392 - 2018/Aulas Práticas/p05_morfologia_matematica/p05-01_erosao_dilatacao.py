# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 05 - Exemplo 01:
- Erosão e dilatação morfológicas.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

import numpy as np
from scipy import misc
from skimage import img_as_float, filters, morphology
import matplotlib.pyplot as plt

# Carrega a imagem a partir de arquivo.
# -------------------------------------
imf_1 = misc.imread('../data/dip_3ed/ch09/text_gaps_1_and_2_pixels.tif')
imf_2 = misc.imread('../data/dip_3ed/ch09/noisy_rectangle.tif')

# Imagem artificial
# -----------------
im_1 = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ])


# Selecione a imagem de entrada:
im = imf_2

# Plota a imagem
plt.figure()
plt.imshow(im, cmap='gray', interpolation='nearest')

# Elemento estruturante (cruz 3x3)
ee1 = np.array([[0,1,0],
                [1,1,1],
                [0,1,0]])

# Elemento estruturante (quadrado 3x3)
ee2 = np.ones([3,3])

# Elemento estruturante (quadrado 5x5)
ee3 = np.ones([45,45])

# Seleciona o EE
ee = ee3

# Dilatacao
im_dil1 = morphology.binary_dilation(im, ee)
# Erosao
im_ero1 = morphology.binary_erosion(im, ee)
# Abertura
im_abe1 = morphology.binary_opening(im, ee)
# Fechamento
im_fec1 = morphology.binary_closing(im_abe1, ee)

# Plota imagens
plt.figure()
plt.subplot(221)
plt.imshow(im_ero1, cmap='gray', interpolation='nearest')
plt.title('Erosao')
plt.subplot(222)
plt.imshow(im_dil1, cmap='gray', interpolation='nearest')
plt.title('Dilatacao')
plt.subplot(223)
plt.imshow(im_abe1, cmap='gray', interpolation='nearest')
plt.title('Abertura')
plt.subplot(224)
plt.imshow(im_fec1, cmap='gray', interpolation='nearest')
plt.title('Fechamento')

plt.show()

