#estrutura de dadks não ordenada, e os objetos não podem repetir

conjunto = {1,2,3,4}
print(conjunto)

conjunto.add(76)
print(conjunto)

existe = 1 in conjunto
print(existe)

for elemento in conjunto:
    print(elemento)



#exercícios
#1
frutas = {"maçã","banana","laranja","uva"}
print(frutas)
#2
frutas.add("abacaxi")
print(frutas)
frutas.add("banana")    # O conjunto não permite adicionar elementos já existentes
print(frutas)

#3
numeros = {10, 20, 30, 40, 50}
numeros.remove(30)
print(numeros)

#4
conjunto = {1,2,3,4,5,6,7,8,9,10}
#alvo = int(input("Escolha o número: "))
alvo = 1

for elemento in conjunto:
    if elemento == alvo:
        resposta = ("O número está no conjunto")

print(resposta)

#5 
lista = [1, 2, 2, 3, 4, 4, 5, 5, 5]
conjunto2 = set()
for elemento in lista:
    conjunto2.add(elemento)

print(conjunto2)

#6
A = {1, 2, 3, 4} 
B = {3, 4, 5, 6}
c = A.union(B)
print(c)

#7
c = A.intersection(B)
print(c)

#8
c = A.difference(B)
print(c)
d = B.difference(A)
print(c)

#9
e = c.union(d)
print(e)

#10