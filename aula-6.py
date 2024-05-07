# 1º Desafio
temp_cel = int(input('Qual é a temperatura da carne? '))

if temp_cel < 48:
  print('Cozinhar por mais alguns minutos')
elif temp_cel in range(48, 53):
  print('Selada')
elif temp_cel in range(54, 59):
  print('Ao ponto para mal')
elif temp_cel in range(60, 64):
  print('Ao ponto')
elif temp_cel in range(65, 70):
  print('Ao ponto para o bem')
else:
  print('Bem passada')

print()

# 2º Desafio
rendimento = int(input("Qual é o rendimento da lata? "))
altura = int(input("Qual é a altura da parede? "))
largura = int(input("Qual é  largura da parede? "))


def calculo_tinta():
  area = altura * largura
  total = area / rendimento
  print(f'Você precisa de {total} latas de tinta.')


calculo_tinta()
print()

# 3º Desafio
funcionarios = [
    'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'
]
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

lista1 = set(tem_carro).intersection(turno_noite)
lista2 = set(tem_carro).intersection(turno_dia)
lista3 = set(funcionarios).difference(tem_carro)

print(lista1)
print(lista2)
print(lista3)

print()

# 4º Desafio
altura = float(input("Digite a sua altura em cm: "))
peso = float(input("Digite o seu peso em kg: "))

imc = peso / (altura / 100)**2
if imc < 18.5:
  print("Magreza")
elif imc >= 18.5 and imc < 24.9:
  print("Normal")
elif imc >= 25.0 and imc < 29.9:
  print("Sobrepeso")
elif imc >= 30.0 and imc < 39.9:
  print("Obesidade")
else:
  print("Obesidade grave")
