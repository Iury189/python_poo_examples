from dobrador import Dobrador

d1 = Dobrador()
while True:
  nome_dobrador = str(input("Digite o nome do dobrador: "))
  d1.setNome(nome_dobrador);
  if (len(nome_dobrador) == 0):
    print('O nome não pode ficar vazio, digite novamente.')
  else:
    break
while True:
  elemento_dobrador = str(input("Digite o elemento do dobrador: "))
  d1.setElemento(elemento_dobrador);
  if (len(elemento_dobrador) == 0):
    print('O elemento do dobrador não pode ficar vazio, digite novamente.')
  else:
    break
d1.Falar()
