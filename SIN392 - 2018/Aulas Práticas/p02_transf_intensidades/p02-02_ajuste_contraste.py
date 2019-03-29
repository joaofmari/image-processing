# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 02 - Exemplo 02: 
- Operações de ajuste de contraste. Alargamento de contraste e equalização de histograma.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
import numpy as np
from scipy import misc 
from skimage import data, img_as_float, exposure
import matplotlib.pyplot as plt

# Carrega uma imagem de baixo contraste a partir do módulo skimage.data.
im = data.moon()
# Converte o tipo de dados da imagem para float [0..1]
im = img_as_float(im)
# Imprime algumas informações sobre a imagem.
print(im.shape, im.min(), im.max(), im.mean(), im.std())

# Alargamento de contraste 1.
im_ac1 = exposure.rescale_intensity(im)
# Alargamento de contraste 2
im_ac2 = exposure.rescale_intensity(im, (0.2,0.6), (0.0,1.0))
# Equalização de histograma
im_eq = exposure.equalize_hist(im)

# Mostra as imagens na tela.
plt.figure()
plt.title('Processamento de histograma')
plt.axis('off')
plt.subplot(2,4,1)
plt.imshow(im,     cmap='gray')
plt.title('Imagem original')
plt.subplot(2,4,2)
plt.imshow(im_ac1, cmap='gray')
plt.title('Alarg. de constraste 1')
plt.subplot(2,4,3)
plt.imshow(im_ac2, cmap='gray')
plt.title('Alarg. de constraste 2')
plt.subplot(2,4,4)
plt.imshow(im_eq,  cmap='gray')
plt.title('Equalizacao de histograma')
plt.subplot(2,4,5)
plt.hist(im.flatten(),     256, range=(0, 1.), normed=True)
plt.title('Histograma')
plt.subplot(2,4,6)
plt.hist(im_ac1.flatten(), 256, range=(0, 1.), normed=True)
plt.title('Histograma')
plt.subplot(2,4,7)
plt.hist(im_ac2.flatten(), 256, range=(0, 1.), normed=True)
plt.title('Histograma')
plt.subplot(2,4,8)
plt.hist(im_eq.flatten(),  256, range=(0, 1.), normed=True)
plt.title('Histograma')
 
plt.show()
