# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 05 - Exemplo 05:
- Gradiente morfológico.
Referencias:
---------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

import numpy as np
from scipy import misc
from skimage import img_as_float, filters, morphology
import matplotlib.pyplot as plt

# Carrega a imagem
# ----------------
imf_1 = misc.imread('../data/dip_3ed/ch09/licoln from penny.tif')

# Garante que a imagem é booleana
# -------------------------------
imf_1 = imf_1.astype(bool)

# Cria uma imagem artificial
# --------------------------
x, y = np.indices((16, 16))
x1, y1 = 8, 8 # Centro do circulo.
r1 = 7 # Raio do circulo.
im_1 = (x - x1) ** 2 + (y - y1) ** 2 < r1 ** 2

# Seleciona a imagem de entrada.
im = imf_1 

# Mostra imagem no terminal.
print(im.astype(np.uint8))

# Elemento estruturante (cruz 3x3)
ee1 = np.array([[0,1,0],
                [1,1,1],
                [0,1,0]])

# Elemento estruturante (quadrado 3x3)
ee2 = np.ones([3,3])

# Erosao da imagem original
im_ero1 = morphology.binary_erosion(im,ee1)
# Subtrai im_ero1 de im.
im_gm1 = im - im_ero1

# Erosao da imagem original
im_ero2 = morphology.binary_erosion(im,ee2)
# Subtrai im_ero2 de im.
im_gm2 = im - im_ero2

# Plota as imagens 
plt.figure()
plt.subplot(2,3,1)
plt.imshow(im, cmap='gray', interpolation='nearest')
plt.title('Imagem original')
plt.subplot(2,3,2)
plt.imshow(im_ero1, cmap='gray', interpolation='nearest')
plt.title('Erosao - 8-conectado')
plt.subplot(2,3,3)
plt.imshow(im_gm1, cmap='gray', interpolation='nearest')
plt.title('Grad. morf. - 4-conectado')
plt.subplot(2,3,4)
plt.imshow(im, cmap='gray', interpolation='nearest')
plt.title('Imagem original')
plt.subplot(2,3,5)
plt.imshow(im_ero2, cmap='gray', interpolation='nearest')
plt.title('Erosao - 4-conectado')
plt.subplot(2,3,6)
plt.imshow(im_gm2, cmap='gray', interpolation='nearest')
plt.title('Gradiente morfologico - 8-conectado')

# Mostra figuras na tela
plt.show()
