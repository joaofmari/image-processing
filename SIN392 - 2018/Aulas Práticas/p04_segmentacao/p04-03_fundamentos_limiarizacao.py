# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 04 - Exemplo 03:
- Fundamentos da segmentação por limiarização.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
import numpy as np
from scipy import misc
from skimage import img_as_float, data
import matplotlib.pyplot as plt

# Carrega a imagem
# ----------------
## im = misc.ascent()
## im = data.camera()
im = data.coins()

# Carrega a imagem a partir de arquivo (descomentar)
# --------------------------------------------------
## im = misc.imread('../data/dip_3ed/ch10/yeast_USC.tif')

# Converte imagem para float [0,1]
# --------------------------------
im = img_as_float( im.astype(np.uint8) )

# Define valores de limiares
# --------------------------
T1 = 0.1
T2 = 0.5
T3 = 0.7
T4 = 0.9

# Aplica a limiarização:
# ----------------------
# - Pixels <= T, 0.
# - Pixels > T, 1.
im_T1 = im > T1
im_T2 = im > T2
im_T3 = im > T3
im_T4 = im > T4

# Plota as imagens
# -----------------
plt.figure()
plt.subplot(2,3,1)
plt.imshow(im, cmap='gray')
plt.title('Imagem original')
plt.subplot(2,3,4)
plt.hist(im.flatten(), bins=256, range=(0,1))
plt.title('Histograma')
plt.subplot(2,3,2)
plt.imshow(im_T1, cmap='gray')
plt.title('T1 = 0.1')
plt.subplot(2,3,3)
plt.imshow(im_T2, cmap='gray')
plt.title('T2 = 0.5')
plt.subplot(2,3,5)
plt.imshow(im_T3, cmap='gray')
plt.title('T3 = 0.7')
plt.subplot(2,3,6)
plt.imshow(im_T4, cmap='gray')
plt.title('T4 = 0.9')

# Mostra as figuras na tela
plt.show()
