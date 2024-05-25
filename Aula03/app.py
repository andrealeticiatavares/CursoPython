num1 = 5
num2 = 3.5

type(num1) # Consegue ver o tpo de dado de uma variável

#convertendo variável para outro tipo
print(type(num1)) #resposta: int
a = float(num1)
print(a)
print(type(a))  #resposta: float

print(type(num2))  #resposta: float
b = int(num2)
print(type(b))  #resposta: int

num3 = "3.8"
print(type(num3))  #resposta: str (string)
c = int(float(num3))
print(type(c))    #resposta: int
c = float(num3)
print(type(c))    #resposta: float
# Obs: A string com número décimal não pode ser convertida diretamente para int, é necessário antes converter para float

num4 = "3"
print(type(num3)) #resposta: str (string)
d = int(num3)
print(type(d))  #resposta: int
d = float(num3)
print(type(d))  #resposta: float

# Operadores aritimeticos
num1 + num2  #soma
num1 - num2  #subtração
num1 * num2  #multiplicação
num1 / num2  #divisão
num1 % num2  #resto da divisão
num1 ** num2 #exponenciação
num1 // num2 #divião inteira: arredonda o resultado da divisão para o numero mais próximo

# Funções
abs(-15)  #retorna o número absoluto
pow(3,3)  #exponenciação
max(100, 8, 3, -55)  #retorna o número maior
min(100, 8, 3, -55)  #retorna o número menor
round(8.3) #arredondamento por aproximação

import math
math.floor(8.3) #arredonda para baixo
math.ceil(8.3) #arredonda para cima
math.sqrt(9) #raiz quadrada