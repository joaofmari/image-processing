# -*- coding: utf-8 -*- 
"""
Universidade Federal de Viçosa - Campus Rio Paranaíba
Bacharelado em Sistemas de Informação
SIN392 - Processamento Digital de Imagens (2018-1)
Prof. João Fernanado Mari - joaofmari@gmail.com
---------------
Prática 01 - Exemplo 08: 
- Exemplo de uma aplicação que processa uma imagem, mostra o resultado do processamento na tela e 
salva a imagem resultante em arquivo. O caminho para a imagem de entrada e da imagem de saída, assim
como o método utilizado para o processamento e os parâmetros são passados como argumento de linha de
comando. 
Referencias:
------------
[1] GONZALEZ, R.C.; WOODS, R.E.; Processamento de imagens digitais. 3 Ed. 
    Pearson, 2010.
"""

# Importa as bibliotecas necessárias
import time
import numpy as np
from scipy import misc, ndimage 
import matplotlib.pyplot as plt

def main(dict_param):
    """
    Recebe os parametros passados como argumento por meio de um dicionário.
    Realiza um espelhamento, que pode ser vertical ou horizontal, ou uma rotação 
    com o angulo no argumento.
    filename_in : Caminho para o arquivo de entrada.

    filename_out : Caminho para o arquivo de saída.

    param_1 : Parametro 1. Método de processamento. 'esp' ou 'rot'

    param_2 : Parametro 2. Parametro do método:
              Se 'esp' : 'h' - horizontal e 'v' - vertical
              Se 'rot' : graus de rotação.    
    """
    # Os parametros são passados em um dicionário
    print('Dicionario de parametros: ' % dict_param)
    # Inicia a contagem de tempo
    t1 = time.clock()
    # Lê a iamgem em filename_in
    im = misc.imread(dict_param['filename_in'])
    # Escolhe  e executa a 
    if dict_param['param_1']=='esp':
        if dict_param['param_2']=='h':
            im_out = np.flipud(im)
        elif dict_param['param_2']=='v':
            im_out = np.fliplr(im)
        else:
            print('Parametro 2 invalido para operacao de espelhamento!')
    elif dict_param['param_1']=='rot':
            im_out = ndimage.rotate(im, float(dict_param['param_2']))
    else:
        print('Parametro 1 invalido!')
        return

    # Finaliza contagem de tempo.
    t2 = time.clock()
    
    # Mostra as imagens
    # -----------------
    plt.figure() # Cria uma nova figura 
    # A area ativa é a 1.
    plt.subplot(1,2,1); plt.imshow(im, cmap='gray')
    plt.axis('off')
    plt.title('Imagem original.')
    # Agora a área ativa é a 2
    plt.subplot(1,2,2); plt.imshow(im_out, cmap='gray')
    plt.axis('off')
    plt.title('Imagem processada.')
    plt.show()
    
    # Contagem de tempo...
    timetaken = t2-t1
    print('Tempo = %f segundos' % timetaken)
    
    # Grava a imagem em arquivo
    misc.imsave(dict_param['filename_out'], im_out)
     
if __name__ == '__main__':
    """
    Como utilizar:
    --------------
    $ p01-08_command_line.py <imagem_entrada> <imagem_saida> <param1> <param2>
    Exemplo 01:
    -----------
    $ p01-08_command_line.py ../data/SIPI/misc/boat.512.tiff boat_ev.png esp v
    Obs: Espelha a imagem verticalmente.
    Exemplo 02:
    -----------
    $ p01-08_command_line.py ../data/SIPI/misc/boat.512.tiff boat_r90.png rot 90
    Obs.: Rotaciona a imagem 90 graus.
    Notas:
    ------
    Para construir chamadas via linha de comando mais eficientes consulte e 
    biblioteca 'argparse'.
    """
    import sys
    print('Numero de argumentos' + str(len(sys.argv)))
    print('Lista de argumentos: ')
    print(sys.argv)
    # Converte a lista sys.argv para um dicionário
    dict_param = {'filename_in'  : sys.argv[1],
                  'filename_out' : sys.argv[2],
                  'param_1'      : sys.argv[3],
                  'param_2'      : sys.argv[4]}
    
    # Chama a função 'main'
    # ---------------------
    main(dict_param)