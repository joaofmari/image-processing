# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 05 - Exemplo 06:
- Morfologia matemática em imagens de intensidades.
Referencias:
---------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

import numpy as np
from scipy import misc
from skimage import img_as_float, morphology, data
import matplotlib.pyplot as plt

# Carrega a imagem
# ----------------
## im = misc.ascent()
im = data.coins()

# Converte a imagem para float [0..1]
# -----------------------------------
im = img_as_float(im.astype(np.uint8))

# Elemento estruturante (cruz 3x3)
ee1 = np.array([[0,1,0],
                [1,1,1],
                [0,1,0]])

# Elemento estruturante (quadrado 3x3)
ee2 = np.ones([3,3])

# EEs gerados pelo skimage
ee3 = morphology.disk(7)
ee4 = morphology.square(7)

# Seleciona EE
ee = ee3

# Dilatacao
im_dil1 = morphology.dilation(im, ee)
# Erosao
im_ero1 = morphology.erosion(im, ee)
# Abertura
im_abe1 = morphology.opening(im, ee)
# Fechamento
im_fec1 = morphology.closing(im, ee)

# Plota as imagens
plt.figure()
plt.subplot(231)
plt.imshow(im, cmap='gray', interpolation='nearest')
plt.title('Imagem original.')
plt.subplot(232)
plt.imshow(im_ero1, cmap='gray', interpolation='nearest')
plt.title('Erosao')
plt.subplot(233)
plt.imshow(im_dil1, cmap='gray', interpolation='nearest')
plt.title('Dilatacao')
plt.subplot(234)
plt.imshow(ee, cmap='gray', interpolation='nearest', vmin=0, vmax=1)
plt.title('Elemento estruturante')
plt.subplot(235)
plt.imshow(im_abe1, cmap='gray', interpolation='nearest')
plt.title('Abertura')
plt.subplot(236)
plt.imshow(im_fec1, cmap='gray', interpolation='nearest')
plt.title('Fechamento')

# Mostra as figuras na tela
plt.show()
