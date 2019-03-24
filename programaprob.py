#Gabriel Oliveira Borges, RA:197458, Ciência da Computação 018
#Nota: A professora disse durante a aula de quinta-feira (21/03) que não seria preciso usar o jupyter notebook

import random
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np

qtdJogos =  100000

def tiraUm(palpite, correto, portas):
    for i in portas:
        if i != correto and i != palpite:
            return i

def escolhePorta(portas):
    return random.randint(1, len(portas))

def mudaPorta(palpite, portas):
    for i in portas:
        if i != palpite:
            return i

def montaGrafico(naoMudou, mudou):
    n_groups = 2
    
    #create plot
    ax = plt.subplots()
    index = np.arange(n_groups)
    barWidth = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, mudou, barWidth, alpha = opacity, color = 'b', label = 'Acertou')
    rects2 = plt.bar(index + barWidth, naoMudou, barWidth, alpha = opacity, color = 'g', label = 'Errou')


    plt.ylabel('Porcentagem\n(%)')
    plt.title('Porcentagem de acertos e erros no jogo das portas. \nForam realizados {} jogos'.format(qtdJogos))
    plt.xticks(index + barWidth/2, ('Manteve porta', 'Mudou de porta'))
    plt.legend()

    plt.tight_layout()

    plt.show()

def main():
    print('Fazendo simulações')
    qtdAcertos = 0
    qtdErros = 0

    #nao muda
    for i in range(qtdJogos):
        portas = [1, 2, 3]
        palpite = escolhePorta(portas)
        correto = escolhePorta(portas)
        portas.remove(tiraUm(palpite, correto, portas))
        if palpite == correto:
            qtdAcertos += 1
        else:
            qtdErros += 1

    qtdAcertosMuda = 0
    qtdErrosMuda = 0
    #muda
    for i in range(qtdJogos):
        portas = [1, 2, 3]
        palpite = escolhePorta(portas)
        correto = escolhePorta(portas)
        portas.remove(tiraUm(palpite, correto, portas))
        palpite = mudaPorta(palpite, portas)
        if palpite == correto:
            qtdAcertosMuda += 1
        else:
            qtdErrosMuda += 1
    

    montaGrafico((qtdAcertosMuda*100/qtdJogos, qtdErrosMuda*100/qtdJogos), (qtdAcertos*100/qtdJogos, qtdErros*100/qtdJogos))


main()





