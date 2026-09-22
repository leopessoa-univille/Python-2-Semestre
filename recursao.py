#Chamada interna para a sua própria função  

#loop infinto. Não faça
def recursao():
    print("a")
    #recursao()
recursao()


def imprimir(n):
    #clausula de encerramento
    if n < 0:
        return
    
    imprimir(n-1)
    print(n)

imprimir(10)


def somar(n):
    if n <1:
        return 0 
    soma = somar(n-1) + n 
    print(soma)
    return soma

somar(10)

#procurar se o elemento existe na lista
def procurar(lista,elemento,  posicao = 0):
    if posicao >= len(lista):
        return False 
    if lista[posicao] == elemento:
        return True
    return procurar(lista,elemento, posicao + 1)

resultado = procurar([1,2,3,4,5,4,5],9)
print("Existe na lista? ", resultado)


#procurar o indice do elemento na lista
def procurar(lista,elemento,  posicao = 0):
    if posicao >= len(lista):
        return -1 
    if lista[posicao] == elemento:
        return posicao
    return procurar(lista,elemento, posicao + 1)

resultado = procurar([1,2,3,4,5,4,5],5)
print("Existe na lista? ", resultado)

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

r = fib(5)
print(r)