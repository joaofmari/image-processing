# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 04 - Exemplo 01:
- Detecção de bordas usando o Laplaciano.
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
## im = data.coins()

# Carrega a imagem a partir de arquivo (descomentar)
# --------------------------------------------------
im = misc.imread('../data/dip_3ed/ch10/yeast_USC.tif')

# Converte imagem para float
# --------------------------
im = img_as_float( im.astype(np.uint8) )

# Aplica o filtro da média sobre a imagem (3x3, 5x5  9x9)
# -------------------------------------------------------
im_m3 = ndi.convolve(im, np.ones([3,3])/9. )
im_m5 = ndi.convolve(im, np.ones([5,5])/25. )
im_m9 = ndi.convolve(im, np.ones([9,9])/81. )

# Mascaras do Laplaciano
# ----------------------
# Laplaciano 4
lap_4 = np.array([[ 0.,  1., 0.],
                  [ 1., -4., 1.],
                  [ 0.,  1., 0.]], dtype=float) 
# Laplaciano 8 (componentes diagonais)
lap_8 = np.array([[-1., -1., -1.],
                  [-1.,  8., -1.],
                  [-1., -1., -1.]], dtype=float)

# Calcula os imagens filtradas pelas máscaras laplacianas
# -------------------------------------------------------
# Laplaciano 4
im_m0_l4  = ndi.convolve( im,    lap_4 )
im_m3_l4  = ndi.convolve( im_m3, lap_4 )
im_m5_l4  = ndi.convolve( im_m5, lap_4 )
# Laplaciano 8
im_m0_l8  = ndi.convolve( im,    lap_8 )
im_m3_l8  = ndi.convolve( im_m3, lap_8 )
im_m5_l8  = ndi.convolve( im_m5, lap_8 )

# Corrige intensidades negativas tomando o valor absoluto dos pixels
# ------------------------------------------------------------------
# Laplaciano 4
im_m0_l4_  = np.abs( im_m0_l4 )
im_m3_l4_  = np.abs( im_m3_l4 )
im_m5_l4_  = np.abs( im_m5_l4 )
# Laplaciano 8
im_m0_l8_  = np.abs( im_m0_l8 )
im_m3_l8_  = np.abs( im_m3_l8 )
im_m5_l8_  = np.abs( im_m5_l8 )

# Limiarização do Laplaciano
# --------------------------
perc = 0.2 # Porcentagem da intensidade maxima
# Laplaciano 4
im_m0_l4_t = im_m0_l4_ >= im_m0_l4_.max() * perc
im_m3_l4_t = im_m3_l4_ >= im_m3_l4_.max() * perc
im_m5_l4_t = im_m5_l4_ >= im_m5_l4_.max() * perc
# Laplaciano 8
im_m0_l8_t = im_m0_l8_ >= im_m0_l8_.max() * perc
im_m3_l8_t = im_m3_l8_ >= im_m3_l8_.max() * perc
im_m5_l8_t = im_m5_l8_ >= im_m5_l8_.max() * perc

# Mostra as imagens
# -----------------
# Laplaciano 4
plt.figure(1)
plt.subplot(341); plt.imshow(im, cmap='gray')
plt.title('Imagem original.')
plt.subplot(342); plt.imshow(im_m0_l4, cmap='gray')
plt.title('Laplaciano')
plt.subplot(343); plt.imshow(im_m0_l4_, cmap='gray')
plt.title('Laplaciano corrigido.')
plt.subplot(344); plt.imshow(im_m0_l4_t, cmap='gray')
plt.title('Bordas detectadas por limiarizacao')
plt.subplot(345); plt.imshow(im_m3, cmap='gray')
plt.title('Filtro da media (3x3).')
plt.subplot(346); plt.imshow(im_m3_l4, cmap='gray')
plt.title('Laplaciano.')
plt.subplot(347); plt.imshow(im_m3_l4_, cmap='gray')
plt.title('Laplaciano corrigido.')
plt.subplot(348); plt.imshow(im_m3_l4_t, cmap='gray')
plt.title('Bordas detectadas por limiarizacao')
plt.subplot(349); plt.imshow(im_m5, cmap='gray')
plt.title('Filtro da media (5x5).')
plt.subplot(3,4,10); plt.imshow(im_m5_l4, cmap='gray')
plt.title('Laplaciano.')
plt.subplot(3,4,11); plt.imshow(im_m5_l4_, cmap='gray')
plt.title('Laplaciano corrigido.')
plt.subplot(3,4,12); plt.imshow(im_m5_l4_t, cmap='gray')
plt.title('Bordas detectadas por limiarizacao')
# Laplaciano 4
plt.figure(2)
plt.subplot(341); plt.imshow(im, cmap='gray')
plt.title('Imagem original.')
plt.subplot(342); plt.imshow(im_m0_l8, cmap='gray')
plt.title('Laplaciano')
plt.subplot(343); plt.imshow(im_m0_l8_, cmap='gray')
plt.title('Laplaciano corrigido.')
plt.subplot(344); plt.imshow(im_m0_l8_t, cmap='gray')
plt.title('Bordas detectadas por limiarizacao')
plt.subplot(345); plt.imshow(im_m3, cmap='gray')
plt.title('Filtro da media (3x3).')
plt.subplot(346); plt.imshow(im_m3_l8, cmap='gray')
plt.title('Laplaciano.')
plt.subplot(347); plt.imshow(im_m3_l8_, cmap='gray')
plt.title('Laplaciano corrigido.')
plt.subplot(348); plt.imshow(im_m3_l8_t, cmap='gray')
plt.title('Bordas detectadas por limiarizacao')
plt.subplot(349); plt.imshow(im_m5, cmap='gray')
plt.title('Filtro da media (5x5).')
plt.subplot(3,4,10); plt.imshow(im_m5_l8, cmap='gray')
plt.title('Laplaciano.')
plt.subplot(3,4,11); plt.imshow(im_m5_l8_, cmap='gray')
plt.title('Laplaciano corrigido.')
plt.subplot(3,4,12); plt.imshow(im_m5_l8_t, cmap='gray')
plt.title('Bordas detectadas por limiarizacao')

# Mostra figuras na tela
plt.show()
