
#Exercício 4 força bruta
sequencia = ['A','C','G','T','A','C','G','T','T','A','C','G','G','A','A','T','C','G']

alvo = ['T','A','C','G']

encontrada = False
for i in range(len(sequencia) - len(alvo) +1):
    if sequencia[i:i + len(alvo)] == alvo:
        print("Sequencia encontrada, começando na posição", i)
        encontrada = True


if not encontrada:
    print("Sequência não encontrada!")


#exercício 3 dividir para conquistar


def quadrado(L,A):
    if L == A:
        return L
    elif L > A:
        return quadrado(L - A, A)
    else:
        return quadrado(L, A - L)

print(quadrado(24,16))

