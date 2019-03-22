import random
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
def printa(qtdAcertos, qtdErros, string):
    print(string)
    print("Foram realizados {} jogos. {}% de acertos e {}% erros".format(qtdJogos, qtdAcertos*100/qtdJogos, qtdErros*100/qtdJogos))


def main():
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

    printa(qtdAcertos, qtdErros, 'Sem mudar')

    print("##################################################################")

    qtdAcertos = 0
    qtdErros = 0
    #muda
    for i in range(qtdJogos):
        portas = [1, 2, 3]
        palpite = escolhePorta(portas)
        correto = escolhePorta(portas)
        portas.remove(tiraUm(palpite, correto, portas))
        palpite = mudaPorta(palpite, portas)
        if palpite == correto:
            qtdAcertos += 1
        else:
            qtdErros += 1
    
    printa(qtdAcertos, qtdErros, 'Mudando')


main()
