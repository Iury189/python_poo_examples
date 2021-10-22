import veiculo
import locale

class Carro(veiculo.Veiculo):

  def Interacao(self):
    locale.setlocale(locale.LC_ALL, '')
    valor_formatado = locale.currency(self.getValor(), symbol=True, grouping=True, international=False)
    print(f"Marca: {self.getMarca()}")
    print(f"Modelo: {self.getModelo()}")
    print(f"Cor: {self.getCor()}")
    print(f"Ano: {self.getAno()}")
    print(f"Valor: {valor_formatado}")