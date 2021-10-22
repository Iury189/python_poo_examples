from dobrador import Dobrador

d1 = Dobrador();
nome_dobrador = str(input("Digite o nome do dobrador: "))
d1.setNome(nome_dobrador);
elemento_dobrador = str(input("Digite o elemento do dobrador: "))
d1.setElemento(elemento_dobrador);
d1.Falar();