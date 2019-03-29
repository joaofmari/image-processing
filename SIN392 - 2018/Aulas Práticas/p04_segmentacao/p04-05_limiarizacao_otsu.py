# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 04 - Exemplo 05:
- Algoritmo de limiarização iterativa simples.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
import numpy as np
from scipy import misc
from skimage import img_as_float, filters, data
import matplotlib.pyplot as plt

# Carrega a imagem
# ----------------
## im = misc.ascent()
## im = data.camera()
im = data.coins()

# Carrega a imagem a partir de arquivo (descomentar)
# --------------------------------------------------
## im = misc.imread('../data/dip_3ed/ch10/yeast_USC.tif')

# Converte a imagem para float [0..1]
# -----------------------------------
# im = img_as_float( im.astype(np.uint8) )

# Limiar de Otsu
t_otsu = filters.threshold_otsu(im)
# Limiar Isodata
t_iso = filters.threshold_isodata(im)
# Limiar de Yen
t_yen = filters.threshold_yen(im)

# Mostra os valores de limiar
print("Limiar de Otsu: %.6f" % t_otsu)
print("Limiar Isodata: %.6f" % t_iso)
print("Limiar de Yen: %.6f"  % t_yen)

# Segmenta a imagem por limiarizacao
# -----------------------------------
im_otsu = im < t_otsu
im_iso  = im < t_iso
im_yen  = im < t_yen

# Calcula as diferenças entre os métodos
# --------------------------------------
dif_o_i = np.abs(im_otsu - im_iso)
dif_o_y = np.abs(im_otsu - im_yen)
dif_i_y = np.abs(im_iso  - im_yen)

# Mostra as imagens
# -----------------
plt.figure()
plt.subplot(241)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.title('Imagem original.')
plt.subplot(242)
plt.imshow(im_otsu, cmap='gray')
plt.colorbar()
plt.title('Limiar de Otsu.')
plt.subplot(243)
plt.imshow(im_iso, cmap='gray')
plt.colorbar()
plt.title('Limiar ISODATA.')
plt.subplot(244)
plt.imshow(im_yen, cmap='gray')
plt.colorbar()
plt.title('Limiar de Yen.')
plt.subplot(246)
plt.imshow(dif_o_i, cmap='gray')
plt.colorbar()
plt.title('Otsu - ISODATA.')
plt.subplot(247)
plt.imshow(dif_o_y, cmap='gray')
plt.colorbar()
plt.title('Otsu - Yen.')
plt.subplot(248)
plt.imshow(dif_i_y, cmap='gray')
plt.colorbar()
plt.title('ISODATA - Yen.')

# Mostra figuras na tela
plt.show()
