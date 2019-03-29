# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 03 - Exemplo 02: 
- Filtro Gaussiano.
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

# Converte a o tipo de dado da imagem para float [0..1]
im = img_as_float(im)

# Realiza as filtragens usando convolucao.
# ========================================

# Padding por espelhamento.
# -------------------------
# Aplica o filtro Gaussiano com variancia 3.
gauss_3  = filters.gaussian_filter(im, sigma=3)
# Aplica o filtro Gaussiano com variancia 5.
gauss_5  = filters.gaussian_filter(im, sigma=5)
# Aplica o filtro Gaussiano com variancia 9.
gauss_9  = filters.gaussian_filter(im, sigma=9)
# Aplica o filtro Gaussiano com variancia 11.
gauss_11 = filters.gaussian_filter(im, sigma=11)
# Aplica o filtro Gaussiano com variancia 25.
gauss_25 = filters.gaussian_filter(im, sigma=25)

"""
# (mode='constant', cval=0) --> Padding com valor 0. (descomentar).
# -----------------------------------------------------------------
# Aplica o filtro Gaussiano com variancia 3.
gauss_3  = filters.gaussian_filter(im, sigma=3, mode='constant', cval=0)
# Aplica o filtro Gaussiano com variancia 5.
gauss_5  = filters.gaussian_filter(im, sigma=5, mode='constant', cval=0)
# Aplica o filtro Gaussiano com variancia 9.
gauss_9  = filters.gaussian_filter(im, sigma=9, mode='constant', cval=0)
# Aplica o filtro Gaussiano com variancia 11.
gauss_11 = filters.gaussian_filter(im, sigma=11, mode='constant', cval=0)
# Aplica o filtro Gaussiano com variancia 25.
gauss_25 = filters.gaussian_filter(im, sigma=25, mode='constant', cval=0)
"""

# Mostra as imagens na tela.
plt.figure()
plt.subplot(2,3,1)
plt.imshow(im, cmap='gray')
plt.title('Imagem original')
plt.subplot(2,3,2)
plt.imshow(gauss_3, cmap='gray')
plt.title('Filtro Gaussiano - sigma=3')
plt.subplot(2,3,3)
plt.imshow(gauss_5, cmap='gray')
plt.title('Filtro Gaussiano - sigma=5')
plt.subplot(2,3,4)
plt.imshow(gauss_9, cmap='gray')
plt.title('Filtro Gaussiano - sigma=99')
plt.subplot(2,3,5)
plt.imshow(gauss_11, cmap='gray')
plt.title('Filtro Gaussiano - sigma=11')
plt.subplot(2,3,6)
plt.imshow(gauss_25, cmap='gray')
plt.title('Filtro Gaussiano - sigma=25')

# Mostra as imagens na tela.
plt.figure()
plt.subplot(2,4,1)
plt.imshow(im, cmap='gray')
plt.title('Imagem original')
plt.subplot(2,4,2)
plt.imshow(gauss_3, cmap='gray')
plt.title('Filtro Gaussiano - sigma=3')
plt.subplot(2,4,3)
plt.imshow(gauss_5, cmap='gray')
plt.title('Filtro Gaussiano - sigma=5')
plt.subplot(2,4,4)
plt.imshow(gauss_9, cmap='gray')
plt.title('Filtro Gaussiano - sigma=9')

plt.subplot(2,4,5)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - Original')
plt.subplot(2,4,6)
plt.imshow(gauss_3[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - sigma=3')
plt.subplot(2,4,7)
plt.imshow(gauss_5[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - sigma=5')
plt.subplot(2,4,8)
plt.imshow(gauss_9[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - sigma=9')

plt.show()