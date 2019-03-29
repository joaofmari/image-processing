# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 05 - Exemplo 02:
- Transformada hit-or-miss.
Referencias:
---------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

import numpy as np
from scipy import misc
from scipy.ndimage import morphology as morph
from skimage import img_as_float, filters, morphology
import matplotlib.pyplot as plt

# Imagem artificial
# -----------------
im = np.array(
      [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ] )
        
# Plota figura
plt.figure()
plt.imshow(im, cmap='gray', interpolation='nearest')
plt.colorbar()

# Elemento estruturante
ee1 = np.ones([3,3])
print(ee1)

# Aplica a transformada hit-or-miss
im_hm = morph.binary_hit_or_miss(im,ee1)
print(im_hm.astype(np.uint8))

# Plota figuras
plt.figure()
plt.imshow(im_hm.astype(np.uint8), cmap='gray', interpolation='nearest')
plt.colorbar()
 
plt.show() 