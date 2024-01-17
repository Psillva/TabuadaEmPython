#Tabuada python
#Solicitando um número ao usuário
primeiroNumero = int(input("Digite o primeiro número: "))
#Tabuada Adição
print("TABUADA DE ADIÇÂO")
for i in range(11):
    adicao = primeiroNumero + i
    print(f"{primeiroNumero} + {i} = {adicao}")
print("\n")
#Tabuada de Subtração
print("TABUADA DE SUBTRAÇÃO")
for i in range(11):
    subtracao = primeiroNumero - i
    print(f"{primeiroNumero} - {i} = {subtracao}")
print("\n")
#Tabuada de Multiplcação
print("TABUADA DE MULTIPLICAÇÃO")
for i in range(11):
    multiplicacao = primeiroNumero * i
    print(f"{primeiroNumero} * {i} = {multiplicacao}")
print("\n")
#Tabuada de Divisão
print("TABUADA DE DIVISÃO")
for i in range(10):
    i += 1
    divisao = primeiroNumero / i
    print(f"{primeiroNumero} / {i} = {divisao}")
    


