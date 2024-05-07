def boas_vindas(nome, quantidade = 6):
  print(f'Olá {nome}!')
  print(f'Tem {quantidade} laptops no estoque.')
  n1 = 10
  n2 = 5
  res = n1 * n2
  print(res)

boas_vindas('João', 7)
boas_vindas('Maria', 5)
boas_vindas('José')

def cliente(nome):
  return f'Olá {nome}!'

print(cliente("Igor"))

def soma(*n):
  total = 0
  for num in n:
    total += num
  return total

x = soma(2, 4, 6, 8)
print(x)

def agencia(**carro):
  return carro

print (agencia(marca='Gol', cor='Branca', motor=1.0, placa=1234))
print (agencia(marca='Gol', cor='Azul', motor=1.0))
print (agencia(marca='Gol', cor='Preto'))

# Módulos
import math

print(math.factorial(4))
print(math.floor(4.6))

# Listas
cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']
print(cidades)
cidades[0] = 'Brasília'
print(cidades)
cidades.append('Santa Catarina')
cidades.remove('Salvador')
print(cidades)
cidades.insert(1, 'Belo Horizonte')
cidades.pop(0)
cidades.sort()
print(cidades)

numeros=[1, 2, 3, 4]
letras = ['a', 'b', 'c']
res1 = numeros * 2
res2 = numeros + letras
print(res1)
print(res2)
numeros.extend(letras)
print(numeros)

lista = [[1, 2], [3, 4]]
print(lista[1][1])

item1, item2, *outros = letras
print(item1)
print(item2)

valores = [10, 80, 110, 150]
for x in valores:
  print(f'O valor final do produto é de R${x}.')

cor_cliente = input("Digite a cor desejada: ")
cores = ['amarelo', 'verde', 'azul', 'vermelho']
if cor_cliente.lower() in cores:
  print('Cor está na lista!')
else:
  print('Cor não está na lista!')

duas_listas = zip(cores, valores) # une listas
print(list(duas_listas)) # divide em cada index

frutas_usuario = input("Por favor digite o nome das frutas separados por vírgulas: ")
frutas_list = frutas_usuario.split(', ')
print(frutas_list)

cores_tuples = ('amarelo', 'verde', 'azul', 'vermelho') # Tuples são listas imutáveis

print(type(cores))
print(type(cores_tuples))

# array - matriz
from array import array
letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]
print(letras)
print(numeros_i)
print(numeros_f)
print()

# tipos de arrays na documentação. Utilizados 'u' string, 'i' int e 'f' float
letras = array('u', ['a', 'b', 'c', 'd'])
letras = array('i', [10, 20, 30, 40])
letras = array('f', [1.2, 2.2, 3.2])
print(letras)
print(numeros_i)
print(numeros_f)

# itens dulicados
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #une as duas listas retirando os repetidos
print(num1 & num2) #retorna os elementos em comum
print(num1 - num2) #retorna os elementos da primeira lista que não estão na segunda
print(num1 ^ num2) #retorna os elementos que não estão repetidos nas duas listas
print(len(num1))

set1 = {10, 20, 30, 40, 50}
print(type(set1))
set1.add(60)
set1.add(40)
print(set1)
set1.update([70, 80, 90])
print(set1)
set1.remove(10)
set1.discard(10)
print(set1)

set2 = {'a', 'b', 'c'}
set3 = {'a', 'd', 'e'}
set4 = {'c', 'd', 'f'}

set5 = set2.union(set3)
print(set5)
set5 = set2.difference(set4)
print(set5)
set5 = set2.intersection(set3)
print(set5)
set5 = set2.symmetric_difference(set4)
print(set5)

# Dicionários
aluno = {} #dicionário vazio
aluno = {
  'nome': 'Ana',
  'idade': 16,
  'nota_final': 'A',
  'aprovacao': True
}
print(aluno)
print(aluno['nome'])
print(aluno.get('nome'))
print(aluno.get('endereco', 'Não existe'))
print(aluno.keys())
print(aluno.values())
print(aluno.items())
aluno['nome'] = 'José'
print(aluno)
aluno.update({'nome': 'José', 'nota_final': 'B'})
print(aluno)
aluno.update({'endereco': 'Rua A'})
print(aluno)
print(aluno.get('endereco', 'Não existe'))
del aluno['idade']
print(aluno)
print()

for keys, values in aluno.items():
  print(f'{keys}: {values}')

aluno.update({'materias': ['Python', 'JavaScript', 'MySQL']})
print(aluno)
print(aluno.get('materias'))
print(len(aluno))

# Função lambda - sem nome
somar10 = lambda x, y: x + y + 10
print(somar10(2, 4))

def somar(x):
  func2 = lambda x: x + 10
  return func2(x) * 4

# Função map
print(somar(2))

def multi(x):
  return x * 2
numeros2 = map(multi, numeros)
print(list(numeros2))

print(list(map(lambda x: x * 2, numeros)))

# Função filter
def remover20(x):
  return x > 20

print(list(map(remover20, valores)))
print(list(filter(remover20, valores)))
print(list(filter(lambda x: x > 20, valores)))

# List comprehension
cores2 = []
for item in cores:
  if 'a' in item:
    cores2.append(item)

print(cores2)
cores3 = [item for item in cores if 'a' in item]
print(cores3)

valores2 = []
for x in range(6):
  valores2.append(x * 10)

print(valores2)
valores3 = [x * 10 for x in range(100)]
print(valores3)

# Generator expressions
from sys import getsizeof
print(getsizeof(valores3))
print()

print(type(valores3))
valores3 = (x * 10 for x in range(100))
print(type(valores3))
print(valores3)
print(list(valores3))
print(getsizeof(valores3))
