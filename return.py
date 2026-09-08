#1. Crie uma função que receba por parâmetro dois números e retorne o número maior.
def maior(a,b):
    if a > b:
        return("O primeiro é maior!")
    elif a == b:
        return("Os dois são iguais")
    else:
        return("O segundo é maior!")
    
Omaior = maior(10,8)
print(Omaior)
#2. Crie uma função que receba por parâmetro dois números e retorne o número maior.

#3. Crie uma função que receba por parâmetro uma lista de números e retorne o número maior.
def maior2(*numeros):
    maior = 0
    for numero in numeros:
        if numero > maior:
            maior = numero

    return maior

lista = maior2(1,2,3,4,27,33,1)
print(lista)
#4. Crie uma função que receba por parâmetro uma lista de números e retorne o número menor.
def menor(*numeros):
    menor = 10000
    for numero in numeros:
        if numero < menor:
            menor = numero

    return menor

lista = menor(1,2,3,4,27,33,1)
print(lista)
#5. Crie uma função que receba por parâmetro dois números e retorne a soma.
def soma(a,b):
    return a+b

somas = soma(2,55)
print(somas)
#6. Crie uma função que receba por parâmetro dois números e retorne a subtração.
def sub(a,b):
    return a-b

subs = sub(2,55)
print(subs)
#7. Crie uma função que receba por parâmetro dois números e retorne a multiplicação. Não utilize o operador de multiplicação * da linguagem. Utilize a sua função de soma para realizar a multiplicação.
def multi(a,b):
    multipl = 0 
    i = 0
    for i in range(b):
        multipl += a

    return multipl

multiplicacao =  multi(2,3)
print(multiplicacao)
#8. Crie uma função que receba por parâmetro uma distância em kilometros e retorne a distância em Milhas.
def milhas(km):
    milhas = km * 0.6

    return milhas

distancia = milhas(20)
print(distancia)
#9. Crie uma função que receba por parâmetro um texto e verifique se o texto é um anagrama. Caso verdadeiro, a função deve returnar True, caso contrário, deve retornar False.

#10. Crie uma função que receba por parâmetro um texto e verifique se o texto é um palíndromo. Caso verdadeiro, a função deve returnar True, caso contrário, deve retornar False.