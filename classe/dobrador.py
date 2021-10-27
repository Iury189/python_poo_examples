class Dobrador:
    # Construtor
    '''
    def __init__(self, nome, elemento):
      self.nome = nome
      self.elemento = elemento
    '''
    # Getters
    def getNome(self): return self.nome
    def getElemento(self): return self.elemento
    # Setters
    def setNome(self, nome): self.nome = nome
    def setElemento(self, elemento): self.elemento = elemento
    # Método Falar()
    def Falar(self): print(f"Dobrador: {self.getNome()} | Elemento: {self.getElemento()}")
