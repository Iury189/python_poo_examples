from carro import Carro

c1 = Carro()
# Campo marca
while True:
  marca_carro = str(input("Digite a marca do carro (Ex: M1): "))
  if (len(marca_carro.split()) <= 0):
    print('A marca do carro não pode ficar vazio, refaça novamente a operação.')
  else:
    c1.setMarca(marca_carro.title())
    break
# Campo modelo
while True:
  modelo_carro = str(input("Digite o modelo do carro (Ex: MD1): "))
  if (len(modelo_carro.split()) <= 0):
    print('O modelo do carro não pode ficar vazio, refaça corretamente a operação.')
  else:
    c1.setModelo(modelo_carro.title())
    break
# Campo cor
while True:
  cor_carro = str(input("Digite a cor do carro (Ex: Vermelho): "))
  if (len(cor_carro.split()) <= 0):
    print('A cor do carro não pode ficar vazio, refaça corretamente a operação.')
  else:
    c1.setCor(cor_carro.title())
    break
# Campo ano de fabricação
while True:
    try:
        ano_carro = int(input("Digite o ano de fabricação do carro (Ex: 2021): "))
        if (ano_carro <= 0):
          print('O ano de fabricação do carro não pode ser menor ou igual a zero.')
        else:
          c1.setAno(ano_carro)
          break
    except (ValueError, TypeError):
        print("Apenas números inteiros são permitidos, refaça corretamente a operação.")   
# Campo valor do carro
while True:
    try:
        valor_carro = float(input("Digite o valor do carro (Ex: 8500.00): "))
        if (valor_carro <= 0):
          print('O valor do carro não pode ser menor ou igual a zero.')
        else:
          c1.setValor(valor_carro)
          break
    except (ValueError, TypeError):
        print("Apenas números são permitidos, refaça corretamente a operação.")
print("\n")
c1.Interacao()
