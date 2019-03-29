# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 03 - Exemplo 04: 
- Filtro laplaciano.
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

# Borra a imagem artifialmente com filtro Gaussiano.
# Obs: Comente esta linha e teste novamente.
im  = filters.gaussian_filter(im, sigma=3)

# Mascaras - Laplaciano 4
lap_4_ = np.array([[ 0.,  1., 0.],
                   [ 1., -4., 1.],
                   [ 0.,  1., 0.]], dtype=float) 

lap_4 = np.array([[ 0., -1.,  0.],
                  [-1.,  4., -1.],
                  [ 0., -1.,  0.]], dtype=float)

# Mascaras - Laplaciano 8 (Componentes diagonais)
lap_8 = np.array([[-1., -1., -1.],
                  [-1.,  8., -1.],
                  [-1., -1., -1.]], dtype=float)

lap_8_ = np.array([[1.,  1.,  1.],
                   [1., -8.,  1.],
                   [1.,  1.,  1.]], dtype=float)


# ***** Calcula os imagens filtradas pelas máscaras laplacianas *****
im_lap_4  = filters.convolve(im, lap_4)
im_lap_4_ = filters.convolve(im, lap_4_)

im_lap_8  = filters.convolve(im, lap_8)
im_lap_8_ = filters.convolve(im, lap_8_)

"""
im_lap_4  = filters.convolve(im, lap_4,  mode='constant', cval=0)
im_lap_4_ = filters.convolve(im, lap_4_, mode='constant', cval=0)

im_lap_8  = filters.convolve(im, lap_8,  mode='constant', cval=0)
im_lap_8_ = filters.convolve(im, lap_8_, mode='constant', cval=0)
"""


# PLOT - Laplaciano - centro=4
plt.figure()
plt.subplot(2,3,1)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.title('Imagem original')
plt.subplot(2,3,2)
plt.imshow(im_lap_4, cmap='gray')
plt.colorbar()
plt.title('Laplaciano - centro = -4')
plt.subplot(2,3,3)
plt.imshow(im_lap_4_, cmap='gray')
plt.colorbar()
plt.title('Laplaciano - centro = 4')
# PLOT - Detalhes 
plt.subplot(2,3,4)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.colorbar()
plt.title('Detalhe - Original')
plt.subplot(2,3,5)
plt.imshow(im_lap_4[240:290,240:290], cmap='gray', interpolation='none')
plt.colorbar()
plt.title('Detalhe')
plt.subplot(2,3,6)
plt.imshow(im_lap_4_[240:290,240:290], cmap='gray', interpolation='none')
plt.colorbar()
plt.title('Detalhe')

# PLOT - laplaciano - centro=8
plt.figure()
plt.subplot(2,3,1)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.title('Imagem original')
plt.subplot(2,3,2)
plt.imshow(im_lap_8, cmap='gray')
plt.colorbar()
plt.title('Laplaciano - centro = -8')
plt.subplot(2,3,3)
plt.imshow(im_lap_8_, cmap='gray')
plt.colorbar()
plt.title('Laplaciano - centro = 8')
# PLOT - Detalhes 
plt.subplot(2,3,4)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.colorbar()
plt.title('Detalhe - Original')
plt.subplot(2,3,5)
plt.imshow(im_lap_8[240:290,240:290], cmap='gray', interpolation='none')
plt.colorbar()
plt.title('Detalhe')
plt.subplot(2,3,6)
plt.imshow(im_lap_8_[240:290,240:290], cmap='gray', interpolation='none')
plt.colorbar()
plt.title('Detalhe')

plt.show()
