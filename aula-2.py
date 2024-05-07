velocidade = 100
if velocidade > 110:
  print("Velocidade acima do permitido!")
  print("Por favor reduzir a velocidade!")
elif velocidade < 60:
  print("Por favor dirigir acima de 80Km/h!")
else:
  print("Velocidade OK")

renda_acima_5mil = True
nome_limpo = False
# Operadores lógicos and e or
if renda_acima_5mil and nome_limpo:
  print("Financiamento Aprovado!")
else:
  print("Financiamento Negado!")

valor = 40
if 20 <= valor < 40:
  print("Produto Aceito!")
else:
  print("Produto Recusado!")

for numero in range(1, 6):
  print(numero)

for numero in range(0, 21, 2):
  print(numero)
  
texto_completo = "Aprendendo Python"

for texto in texto_completo:
  print(f'{texto} está dentro de {texto_completo}')

compra_confirmada = True
dados_compra = "Compra no valor de R$50.00 e entrega Confirmada"

for enviar in range(3):
  if compra_confirmada:
    print(dados_compra)
    print("Detalhes da compra enviados por e-mail!")
    break
else:
  print("Compra Recusada")

for numero1 in range(1, 6):
  print("Produto"+ str(numero1))
  for numero2 in range(6):
    print(numero1, numero2)

palavra = "FANTASTICO"
for espaco in palavra:
  print(f' {espaco}', end='') # end não quebra a linha

# Fazendo um retangulo
linhas = 6
colunas = 6
simbolo = '@'
for l in range(linhas):
  for c in range(colunas):
    print(simbolo, end='')
  print()

valor = 100
dia = 1
while valor > 20:
  print(f'No dia {dia} o produto vai ser vendido por R${valor}')
  dia += 1
  valor -= 5

idade = 14
resultado = 'Voto Permitido' if idade >= 16 else 'Voto não Permitido'
print(resultado)

valor = int(input('Digite o Valor do seu Produto: '))
while valor > 20:
  valor = (valor *0.10) + valor
  print(f'O valor final do seu produto será de R${valor}')
  break

'''
Python While Loop é usado para executar um bloco de instruções repetidamente até que uma determinada condição seja satisfeita. E quando a condição se torna falsa, a linha imediatamente após o loop no programa é executada. O loop while cai na categoria de iteração indefinida . Iteração indefinida significa que o número de vezes que o loop é executado não é especificado explicitamente com antecedência.


As instruções representam todas as instruções recuadas pelo mesmo número de espaços de caracteres depois que uma construção de programação é considerada parte de um único bloco de código. Python usa endentação como seu método de agrupamento de declarações. Quando um loop while é executado, expr é avaliado primeiro em um contexto booleano e, se for verdadeiro, o corpo do loop é executado. Em seguida, a expr é verificada novamente, se ainda for verdadeira, o corpo é executado novamente e continua até que a expressão se torne falsa.
'''