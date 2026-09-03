#São pequenas unidades de códigos nomeadas que podem ser reutilizadas(invocadas). Pode ou não devolver valores

# def -> define uma nova função
def hello_funcao():
    print("Hello World")


hello_funcao()



#passando parâmetros para a função
def hello_funcao(nome):
    print("Hello",nome)


hello_funcao("Leonardo")



def soma(a,b):
    print("a+b =", (a+b))

soma(2,2)

def a():
    print("A")

def b():
    print("B")
    a()

b()