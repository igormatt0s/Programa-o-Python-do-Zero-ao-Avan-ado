# Erros
try:
  letras = ['a', 'b', 'c']
  print(letras[3])
except IndexError:
  print('Index não existe!')

try:
  valor = int(input("Digite o valor do seu produto: "))
  print(valor)
except ValueError:
  print("Por favor digitar um valor em números!")
else:
  print("Usuário digitou um valor válido")
  resultado = valor * 10
  print(resultado)
finally:
  print("Fim do programa")

print("Mais códigos abaixo...")

# POO
from datetime import datetime
#criar a classe
'''
class Funcionarios:
  nome = 'Emanuelle'
  sobrenome = 'Mattos'
  data_nascimento = '2000'
'''
'''
class Funcionarios:
  pass
'''
class Funcionarios:
  # construtores
  def __init__(self, nome, sobrenome, ano_nascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.ano_nascimento = ano_nascimento

  def nome_completo(self):
    return self.nome + ' ' + self.sobrenome

  def idade(self):
    ano_atual = datetime.now().year
    self.ano_nascimento = ano_atual - int(self.ano_nascimento)
    return self.ano_nascimento
      
# criar o objeto
'''
usuario1 = Funcionarios()
usuario2 = Funcionarios()
'''
usuario1 = Funcionarios('Emanuelle', 'Mattos', '2000')
usuario2 = Funcionarios('Marlene', 'Araujo', '2010')
'''
# criar os parametros
usuario1.nome = 'Emanuelle'
usuario1.sobrenome = 'Mattos'
usuario1.data_nascimento = '2000'

usuario2.nome = 'Marlene'
usuario2.sobrenome = 'Araujo'
usuario2.data_nascimento = '2010'
'''
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.ano_nascimento)
print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.ano_nascimento)

print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario2))

print(usuario1.idade())
print(Funcionarios.idade(usuario2))
