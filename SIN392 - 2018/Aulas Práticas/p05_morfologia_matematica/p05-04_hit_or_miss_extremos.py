# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 05 - Exemplo 04:
- Transformada hit-or-miss para detecção de extremidades.
Referencias:
---------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
import numpy as np
from scipy import misc
from scipy.ndimage import morphology as morph
from skimage import img_as_float, filters, morphology
import matplotlib.pyplot as plt

# Carrega a imagem
# ----------------
imf_1 = misc.imread('../data/dip_3ed/ch09/text_image.tif')
       
# Imagem artificial
# -----------------          
im_1 = np.array( [ [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 1, 1, 0, 0, 1, 0, 0 ],
                   [ 0, 1, 0, 1, 0, 1, 1, 0 ], 
                   [ 0, 0, 0, 1, 0, 1, 0, 0 ],
                   [ 0, 1, 0, 1, 1, 1, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 1, 1, 1, 1, 1, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0 ] ] )  

# Seleciona a imagem de entrada.
im = im_1            

# Plota as figuras
plt.figure()
plt.imshow(im, cmap='gray', interpolation='nearest')

# Elementos estruturantes - HIT
ee1_h = np.array([[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]])
                  
ee2_h = np.array([[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]])

ee3_h = np.array([[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]])
                  
ee4_h = np.array([[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]])

# Elementos estruturantes - MISS
ee1_m = np.array([[1, 1, 1],
                  [1, 0, 1],
                  [0, 0, 0]])
                  
ee2_m = np.array([[0, 0, 0],
                  [1, 0, 1],
                  [1, 1, 1]])
                  
ee3_m = np.array([[1, 1, 0],
                  [1, 0, 0],
                  [1, 1, 0]])
                  
ee4_m = np.array([[0, 1, 1],
                  [0, 0, 1],
                  [0, 1, 1]])

# Aplica hit-or-miss
im_hm1 = morph.binary_hit_or_miss(im,ee1_h,ee1_m)
im_hm2 = morph.binary_hit_or_miss(im,ee2_h,ee2_m)
im_hm3 = morph.binary_hit_or_miss(im,ee3_h,ee3_m)
im_hm4 = morph.binary_hit_or_miss(im,ee4_h,ee4_m)

# Uniao das transformadas hit-or-miss
im_hm = np.logical_or(im_hm1, im_hm2)
im_hm = np.logical_or(im_hm,  im_hm3)
im_hm = np.logical_or(im_hm,  im_hm4)

# Plota as figuras
plt.figure()
plt.subplot(231)
plt.imshow(im, cmap='gray', interpolation='nearest')
plt.title('Imagem original')
plt.subplot(232)
plt.imshow(im_hm1, cmap='gray', interpolation='nearest')
plt.title('Hit-or-miss EE1')
plt.subplot(233)
plt.imshow(im_hm2, cmap='gray',interpolation='nearest')
plt.title('Hit-or-miss EE2')
plt.subplot(234)
plt.imshow(im_hm3, cmap='gray', interpolation='nearest')
plt.title('Hit-or-miss EE3')
plt.subplot(235)
plt.imshow(im_hm4, cmap='gray', interpolation='nearest')
plt.title('Hit-or-miss EE4')
plt.subplot(236)
plt.imshow(im_hm, cmap='gray', interpolation='nearest')
plt.title('Hit-or-miss - UNIAO')
 
plt.show()
