from jojo import JoJo

j1 = JoJo()
while True:
  nome = str(input("Digite o nome do usuário: "))
  if (len(nome.strip()) <= 0):
    print("O nome do usuário não pode ficar vazio.")
  else:
    j1.SetNome(nome.title())
    break
while True:
  stand = str(input(f"Digite o nome do stand de {j1.GetNome()}: "))
  if (len(stand.strip()) <= 0):
    print(f"O nome do Stand de {j1.GetNome()} não pode ficar vazio.")
  else:
    j1.SetStand(stand.title())
    break
j1.Falar()
del j1
