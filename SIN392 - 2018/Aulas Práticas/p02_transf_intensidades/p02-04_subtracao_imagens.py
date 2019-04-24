# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 02 - Exemplo 04: 
- Subtração de duas imagens.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

import numpy as np
from scipy import misc, ndimage
import matplotlib.pyplot as plt

# Lê as imagens a partir de arquivos
im_l = misc.imread('../data/dip_3ed/ch03/angiography_live_image.tif')
im_m = misc.imread('../data/dip_3ed/ch03/angiography_mask_image.tif')

# Subtrai imagem máscara da imagem ativa.
im_sub = im_l.astype(np.float) - im_m.astype(np.float)

# Plota as imagens em uma figura.
# Cria uma nova figura 
plt.figure() 
# Divide a área de plotagem: 1 linha e 3 colunas.
plt.subplot(1,3,1) # A área ativa é a 1.
plt.imshow(im_l, cmap='gray')
plt.axis('off')
plt.title('Imagem ativa - antes do contraste')
plt.subplot(1,3,2) # Agora a área ativa é a 2.
plt.imshow(im_m, cmap='gray')
plt.title('Imagem mascara - apos do contraste')
plt.subplot(1,3,3) # A área ativa é a 3.
plt.imshow(im_sub, cmap='gray')
plt.title('Resultado da subtracao')
plt.show()
