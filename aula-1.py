'''
Autor: Igor
Data: 
Versão: 1.0
'''

# Impressão no console
print('Olá mundo!')
print("Tudo bem?")

x = 2
y = 'Igor'
z = 7.4

print(x + z)
print(y)

a = str(9)
b = int(5.9)
c = float(0.1)

print(a + a, b, c)

sobrenome = input("Qual é o seu sobrenome: ")
idade = 22
universidade = 'UTFPR'

print(f'Meu nome é {y}, tenho {idade} anos e estudo na {universidade}') # texto formatado

print('Meu sobrenome é '+ sobrenome +', tenho '+ str(idade) +' anos e estudo na '+ universidade)

ano_nascimento = input("Em que ano você nasceu? ")
print(type(ano_nascimento))
idade = 2023 - int(ano_nascimento)
print(type(idade))
print('Você tem '+ str(idade) + ' anos.')

ano_nascimento = str(ano_nascimento)
print(sobrenome[0]) # primeira letra
print(sobrenome[-1]) # última letra
print(ano_nascimento[2 : 4]) # intervalos

# Métodos
texto = "   o Tolkien é o autor de Senhor dos Anéis"

print(texto.lower()) # tudo minúsculo
print(texto.upper()) # tudo maiúsculo
print(texto.capitalize()) # primeira letra maiúscula
print(texto.find('a'))
print(texto.find('A'))
print(texto.find('r'))
print(texto.replace('Tolkien', 'J. R. R. Tolkien')) # trocar palavras
print(texto.strip()) # ignorar espaços no início da string

calculo = 2 ** 3 + (2 + 2) * 3 / 2
print(calculo)

operador1 = 'banana' == 'Banana'
operador2 = 'banana' != 'Banana'
print(operador1)
print(operador2)

operador_atribuicao = 10
operador_atribuicao += 5
print(operador_atribuicao)
operador_atribuicao -= 5
print(operador_atribuicao)
operador_atribuicao *= 5
print(operador_atribuicao)
operador_atribuicao /= 5
print(operador_atribuicao)
operador_atribuicao %= 3
print(operador_atribuicao)