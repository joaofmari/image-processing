# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 04 - Exemplo 02:
- Detecção de bordas usando o Gradiente.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
import numpy as np
from scipy import misc
from scipy import ndimage as ndi
from skimage import img_as_float, filters, data, color
import matplotlib.pyplot as plt

# Carrega a imagem
# ----------------
## im = misc.ascent()
## im = data.camera()
im = data.coins()

# Carrega a imagem a partir de arquivo (descomentar)
# --------------------------------------------------
## im = misc.imread('../data/dip_3ed/ch10/yeast_USC.tif')

# Mostra informações sobre a imagem
print im.shape, im.dtype, im.min(), im.max()

# Converte imagem para float
# --------------------------
im = img_as_float(im)
# Mostra informações sobre a imagem
print im.shape, im.dtype, im.min(), im.max()

# Aplica o filtro da média sobre a imagem (3x3, 5x5  9x9)
# -------------------------------------------------------
im_m3 = ndi.convolve(im, np.ones( [3,3])/9. )
im_m5 = ndi.convolve(im, np.ones( [5,5])/25. )
im_m9 = ndi.convolve(im, np.ones( [9,9])/81. )

# Operadores de Sobel
# -------------------
# Sobel horizontal
sob_h = np.array([[-1., -2., -1.],
                  [ 0.,  0.,  0.],
                  [ 1.,  2.,  1.]], dtype=float)
# Sobel vertical
sob_v = np.array([[-1.,  0.,  1.],
                  [-2.,  0.,  2.],
                  [-1.,  0.,  1.]], dtype=float)

# Computa o Gradiente de Sobel
# ----------------------------
# Imagem original - sem filtro da média
im_sob_h  = ndi.convolve(im, sob_h)
im_sob_v  = ndi.convolve(im, sob_v)
# Magnitude do gradiente (hipotenusa)
im_m0_sob = np.sqrt(im_sob_h**2 + im_sob_v**2)
# Magnitude do gradiente (aproximado)
im_m0_sob_a = np.abs(im_sob_h) + np.abs(im_sob_v)

# Filtro da média 3x3
im_m3_sob_h  = ndi.convolve(im_m3, sob_h)
im_m3_sob_v  = ndi.convolve(im_m3, sob_v)
# Magnitude do gradiente (hipotenusa)
im_m3_sob = np.sqrt(im_m3_sob_h**2 + im_m3_sob_v**2)
# Magnitude do gradiente (aproximado)
im_m3_sob_a = np.abs(im_m3_sob_h) + np.abs(im_m3_sob_v)

# Filtro da média 5x5
im_m5_sob_h  = ndi.convolve(im_m5, sob_h)
im_m5_sob_v  = ndi.convolve(im_m5, sob_v)
# Magnitude do gradiente (hipotenusa)
im_m5_sob = np.sqrt(im_m5_sob_h**2 + im_m5_sob_v**2)
# Magnitude do gradiente (aproximado)
im_m5_sob_a = np.abs(im_m5_sob_h) + np.abs(im_m5_sob_v)

# Limiarização do Gradiente
# --------------------------
perc = 0.33 # Porcentagem da intensidade maxima.
im_m0_sob_t = im_m0_sob >= im_m0_sob.max() * perc
im_m3_sob_t = im_m3_sob >= im_m3_sob.max() * perc
im_m5_sob_t = im_m5_sob >= im_m5_sob.max() * perc

# Mostra as imagens na tela
# -------------------------
plt.figure(1)
plt.subplot(331); plt.imshow(im, cmap='gray')
plt.title('Imagem original.')
plt.subplot(332); plt.imshow(im_m0_sob, cmap='gray')
plt.title('Gradiente de Sobel')
plt.subplot(333); plt.imshow(im_m0_sob_t, cmap='gray')
plt.title('Bordas detectadas por limiarizacao.')
plt.subplot(334); plt.imshow(im_m3, cmap='gray')
plt.title('Filtro da media (3x3).')
plt.subplot(335); plt.imshow(im_m3_sob, cmap='gray')
plt.title('Gradiente de Sobel')
plt.subplot(336); plt.imshow(im_m3_sob_t, cmap='gray')
plt.title('Bordas detectadas por limiarizacao.')
plt.subplot(337); plt.imshow(im, cmap='gray')
plt.title('Filtro da media (5x5).')
plt.subplot(338); plt.imshow(im_m5_sob, cmap='gray')
plt.title('Gradiente de Sobel')
plt.subplot(339); plt.imshow(im_m5_sob_t, cmap='gray')
plt.title('Bordas detectadas por limiarizacao.')

# Mostra figuras na tela
plt.show()
