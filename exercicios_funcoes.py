#1
def multiplicacao(a,b):
    multi = a * b
    print(multi)

multiplicacao(10,5)

#2
def somar(a):
    soma = 0
    for elemento in a:
        soma = soma + elemento

    print("A soma é:",soma)

lista = [6,2,3,1,2]
somar(lista)

#3
def procura(alvo):
    lista = [1,2,3,4,5,6,7]
    for i in range(len(lista)):
        if lista[i] == alvo:
            print("O elemento está na posição",lista[i])

procura(1)
