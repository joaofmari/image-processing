# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 03 - Exemplo 06: 
- Filtro gradiente.
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

im = filters.median_filter(im, size=3)

# Operadores diagonais de Roberts
rob_d1 = np.array([[-1., 0.],
                   [ 0., 1.]], dtype=float)
rob_d2 = np.array([[0., -1.],
                   [1.,  0.]], dtype=float)

# Operadores de Prewitt
pre_h = np.array([[-1., -1., -1.],
                  [ 0.,  0.,  0.],
                  [ 1.,  1.,  1.]], dtype=float)
pre_v = np.array([[-1.,  0.,  1.],
                  [-1.,  0.,  1.],
                  [-1.,  0.,  1.]], dtype=float)

# Operadores de Sobel
sob_h = np.array([[-1., -2., -1.],
                  [ 0.,  0.,  0.],
                  [ 1.,  2.,  1.]], dtype=float)
sob_v = np.array([[-1.,  0.,  1.],
                  [-2.,  0.,  2.],
                  [-1.,  0.,  1.]], dtype=float)


# Gradiente de Roberts.
im_rob_d1  = filters.convolve(im, rob_d1)
im_rob_d2  = filters.convolve(im, rob_d2)
# Magnitude do gradiente (hipotenusa)
im_rob = np.sqrt(im_rob_d1**2 + im_rob_d2**2)
# Magnitude do gradiente (aproximado)
im_rob_a = np.abs(im_rob_d1) + np.abs(im_rob_d2)

# Gradiente de Prewitt.
im_pre_h  = filters.convolve(im, pre_h)
im_pre_v  = filters.convolve(im, pre_v)
# Magnitude do gradiente (hipotenusa)
im_pre = np.sqrt(im_pre_h**2 + im_pre_v**2)
# Magnitude do gradiente (aproximado)
im_pre_a = np.abs(im_pre_h) + np.abs(im_pre_v)

# Gradiente de Sobel.
im_sob_h  = filters.convolve(im, sob_h)
im_sob_v  = filters.convolve(im, sob_v)
# Magnitude do gradiente (hipotenusa)
im_sob = np.sqrt(im_sob_h**2 + im_sob_v**2)
# Magnitude do gradiente (aproximado)
im_sob_a = np.abs(im_sob_h) + np.abs(im_sob_v)



# PLOT - Gradiente de Roberts 
plt.figure()
# - linha 1
plt.subplot(2,4,1)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Imagem Original')
plt.subplot(2,4,2)
plt.imshow(im_rob_d1, cmap='gray', interpolation='none')
plt.title('Gradiente de Roberts - Diagonal 1')
plt.subplot(2,4,3)
plt.imshow(im_rob_d2, cmap='gray', interpolation='none')
plt.title('Gradiente de Roberts - Diagonal 2')
plt.subplot(2,4,4)
plt.imshow(im_rob, cmap='gray', interpolation='none')
plt.title('Gradiente de Roberts - Exato (hipotenusa)')
# - linha 2
plt.subplot(2,4,5)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - Original')
plt.subplot(2,4,6)
plt.imshow(im_rob_d1[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe')
plt.subplot(2,4,7)
plt.imshow(im_rob_d2[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe')
plt.subplot(2,4,8)
plt.imshow(im_rob[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe')

# PLOT - Gradiente de Prewitt 
plt.figure()
# - linha 1
plt.subplot(2,4,1)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Imagem Original')
plt.subplot(2,4,2)
plt.imshow(im_pre_h, cmap='gray', interpolation='none')
plt.title('Gradiente de Prewitt - Horizontal')
plt.subplot(2,4,3)
plt.imshow(im_pre_v, cmap='gray', interpolation='none')
plt.title('Gradiente de Prewitt - Vertical')
plt.subplot(2,4,4)
plt.imshow(im_pre, cmap='gray', interpolation='none')
plt.title('Gradiente de Prewitt - Exato (hipotenusa)')
# - linha 2
plt.subplot(2,4,5)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Prewitt - Original')
plt.subplot(2,4,6)
plt.imshow(im_pre_v[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Prewitt')
plt.subplot(2,4,7)
plt.imshow(im_pre_h[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Prewitt')
plt.subplot(2,4,8)
plt.imshow(im_pre[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Prewitt')

# PLOT - Gradiente de Sobel 
plt.figure()
# - linha 1
plt.subplot(2,4,1)
plt.imshow(im, cmap='gray', interpolation='none')
plt.title('Imagem Original')
plt.subplot(2,4,2)
plt.imshow(im_sob_h, cmap='gray', interpolation='none')
plt.title('Gradiente de Sobel - Horizontal')
plt.subplot(2,4,3)
plt.imshow(im_sob_v, cmap='gray', interpolation='none')
plt.title('Gradiente de Sobel - Vertical')
plt.subplot(2,4,4)
plt.imshow(im_sob, cmap='gray', interpolation='none')
plt.title('Gradiente de Sobel - Exato (hipotenusa)')
# - linha 2
plt.subplot(2,4,5)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Sobel - Original')
plt.subplot(2,4,6)
plt.imshow(im_sob_v[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Sobel')
plt.subplot(2,4,7)
plt.imshow(im_sob_h[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Sobel')
plt.subplot(2,4,8)
plt.imshow(im_sob[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Sobel')

plt.show()
