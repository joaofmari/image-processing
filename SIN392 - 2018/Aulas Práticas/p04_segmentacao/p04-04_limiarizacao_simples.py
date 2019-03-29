# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 04 - Exemplo 04:
- Algoritmo de limiarização iterativa simples.
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
import numpy as np
from scipy import ndimage, misc
from skimage import img_as_float, data
import matplotlib.pyplot as plt

def limiar_global_simples(im, T_ini=None, min_delta_T=None, plot=False):
    """
    Algoritmo de limiarização iterativa simples.
    """
    if T_ini==None:
        # Nenhum valor inicial atribuido:
        # - Considerar a intensidade média.
        T_ini = im.mean()
    if min_delta_T==None:
        # Se min_delta_T nao informado:
        # - 'min_delta_T' eh 1% da maior intensidade!
        min_delta_T = im.max() * 0.01

    # Inicializa T com T_ini.
    T = T_ini
    # Inicializa delta_T com Infinito. 
    delta_T = np.inf

    # Iteracao
    i = 0
    while delta_T >= min_delta_T:
        # Segmenta a imagem usando T.
        g_bw = im > T
        # Calcula o numero de pixels de objeto e de fundo.
        num_px_bg, num_px_fg = np.bincount(g_bw.flatten()) 
        # Constroi imagem com os pixels de objeto.
        g_fg = im * g_bw
        # Constroi imagem com os pixels de fundo.
        g_bg = im * np.invert(g_bw)
        # Intensidade média - pixels de objeto
        fg_mean = g_fg.sum() / float( num_px_fg )
        # Intensidade média – pixels de fundo
        bg_mean = g_bg.sum() / float( num_px_bg )
        # Armazena valor atual de T.
        T_old = T
        # Calcula um novo limiar T.        
        T = 0.5 * (fg_mean + bg_mean)
        # Calcula o novo valor de delta_T.
        delta_T = np.abs(T - T_old)
        # Mostra informacoes na tela
        print('\nIteracao: ', i)
        print(' - T anterior: ', T_old)
        print(' - T atual:    ', T)
        print(' - delta_T     ', delta_T)
        # Incrementa i
        i = i + 1

        # Plota as imagens parciais
        if plot == True:
            plt.figure()
            plt.subplot(221); plt.imshow(im, cmap='gray')
            plt.title('Imagem original')
            plt.colorbar()
            plt.subplot(222); plt.imshow(g_bw, cmap='gray')
            plt.title('Imagem segmentada.')
            plt.colorbar()
            plt.subplot(223); plt.imshow(g_fg, cmap='gray')
            plt.colorbar()
            plt.title('Pixels de objeto.')
            plt.subplot(224); plt.imshow(g_bg, cmap='gray')
            plt.colorbar() 
            plt.title('Pixels de fundo.')
            # plt.show()

    # Retorna o limiar T.
    return T

if __name__ == '__main__':
    """
    """
    # Carrega a imagem
    # ----------------
    ## im = misc.ascent()
    ## im = data.camera()
    im = data.coins()

    # Carrega a imagem a partir de arquivo (descomentar)
    # --------------------------------------------------
    ## im = misc.imread('../data/dip_3ed/ch10/yeast_USC.tif')

    im = img_as_float(im.astype(np.uint8))

    # Chama a funcao para calculo do limiar global iterativo
    # ------------------------------------------------------
    valor_T = limiar_global_simples(im, 0.5, plot=True)
    # TESTE
    print('\nT final: ', valor_T)

    # Segmenta a imagem com o limiar T.
    im_bw = im > valor_T

    # Mostra a imagem final
    # ---------------------
    plt.figure()
    plt.subplot(121)
    plt.imshow(im, cmap='gray')
    plt.colorbar() 
    plt.title('Imagem original.')
    plt.subplot(122)
    plt.imshow(im_bw, cmap='gray')
    plt.colorbar() 
    plt.title('Imagem segmentada.')

    # Mostra as figuras na tela
    # -------------------------
    plt.show()
