from jojo import *
    
jojo = JoJo()

while True:
  nome = str(input("Digite o nome do usuário: "))
  if nome.strip() == '':
    print("O nome do usuário não pode ficar vazio.")
  else:
    jojo.setNome(nome.title())
    break
while True:
  stand = str(input(f"Digite o nome do stand de {jojo.getNome()}: "))
  if stand.strip() == '':
    print(f"O nome do stand de {jojo.getNome()} não pode ficar vazio.")
  else:
    jojo.setStand(stand.title())
    break

jojo.falar()
del jojo
