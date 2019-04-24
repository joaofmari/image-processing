# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 03 - Exemplo 01: 
- Filtro da média por convolução.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

import numpy as np
from scipy import misc
from scipy.ndimage import filters 
from skimage import img_as_float
import matplotlib.pyplot as plt

# Carrega a imagem
im = misc.ascent()

# Converte a o tipo de dado da imagem para float [0..1]
im = img_as_float(im)

# Máscara da média 3x3.
# Preenchendo o arranjo manualmente.
masc3 = np.array([[1./9, 1./9, 1./9],
                  [1./9, 1./9, 1./9],
                  [1./9, 1./9, 1./9]], dtype=float)
print(masc3)                

# Mascara da media 5x5.
# Preenchendo o arranjo usando função do NumPy.
masc5 = np.ones([5,5], dtype=float)
masc5 = masc5 / 25.
print(masc5)
# Mascara da media 9x9
masc9 = np.ones([9,9], dtype=float)
masc9 = masc9 / 81.
print(masc9)
# Mascara da media 9x9
masc11 = np.ones([11,11], dtype=float)
masc11 = masc11 / 121.
print(masc11)
# Mascara da media 9x9
masc25 = np.ones([25,25], dtype=float)
masc25 = masc25 / 625.
print(masc25)

# Realiza as filtragens usando convolução.
# ----------------------------------------
# Aplica o filtro da media com mescara 3x3.
media_3x3 = filters.convolve(im, masc3, mode='constant', cval=0)
# Aplica o filtro da media com mescara 5x5.
media_5x5 = filters.convolve(im, masc5, mode='constant', cval=0)
# Aplica o filtro da media com mescara 9x9.
media_9x9 = filters.convolve(im, masc9, mode='constant', cval=0)
# Aplica o filtro da media com mescara 3x3.
media_11x11 = filters.convolve(im, masc11, mode='constant', cval=0)
# Aplica o filtro da media com mescara 25x25.
media_25x25 = filters.convolve(im, masc25, mode='constant', cval=0)

# Mostra as imagens na tela.
plt.figure()
plt.subplot(2,3,1)
plt.imshow(im, cmap='gray')
plt.title('Imagem original')
plt.subplot(2,3,2)
plt.imshow(media_3x3, cmap='gray')
plt.title('Filtro da media - 3x3')
plt.subplot(2,3,3)
plt.imshow(media_5x5, cmap='gray')
plt.title('Filtro da media - 5x5')
plt.subplot(2,3,4)
plt.imshow(media_9x9, cmap='gray')
plt.title('Filtro da media - 9x9')
plt.subplot(2,3,5)
plt.imshow(media_11x11, cmap='gray')
plt.title('Filtro da media - 11x11')
plt.subplot(2,3,6)
plt.imshow(media_25x25, cmap='gray')
plt.title('Filtro da media - 25x25')

# Mostra as imagens na tela.
# Mostra detalhe das imagens.
plt.figure()
plt.subplot(2,4,1)
plt.imshow(im, cmap='gray')
plt.title('Imagem original')
plt.subplot(2,4,2)
plt.imshow(media_3x3, cmap='gray')
plt.title('Filtro da media - 3x3')
plt.subplot(2,4,3)
plt.imshow(media_5x5, cmap='gray')
plt.title('Filtro da media - 5x5')
plt.subplot(2,4,4)
plt.imshow(media_9x9, cmap='gray')
plt.title('Filtro da media - 9x9')

plt.subplot(2,4,5)
plt.imshow(im[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - Original')
plt.subplot(2,4,6)
plt.imshow(media_3x3[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - 3x3')
plt.subplot(2,4,7)
plt.imshow(media_5x5[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - 5x5')
plt.subplot(2,4,8)
plt.imshow(media_9x9[240:290,240:290], cmap='gray', interpolation='none')
plt.title('Detalhe - 9x9')


plt.show()
