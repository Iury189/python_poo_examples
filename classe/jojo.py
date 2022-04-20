class JoJo:
    # Construtor
    def __init__(self):
        self.status_stand = False
    # Destrutor
    def __del__(self):
        print (f"O usuário {self.getNome()} foi excluído pelo destrutor.")
    # Getter
    def getNome(self): return self.nome
    def getStand(self): return self.stand
    # Setter
    def setNome(self, nome): self.nome = nome
    def setStand(self, stand): self.stand = stand
    # Método ativarStand()    
    def ativarStand(self):
        if self.status_stand:
            print(f"{self.getStand()} já está invocado.")
        else:
            self.status_stand = True
            print(f"{self.getStand()} foi invocado.")
    # Método desativarStand()
    def desativarStand(self):
        if self.status_stand == False:
            print(f"{self.getStand()} já está oculto.")
        else:
            self.status_stand = False
            print(f"{self.getStand()} foi ocultado.")
    # Método falar()        
    def falar(self):
        print(f"Nome: {self.getNome()} | Stand: {self.getStand()}")
        print ("Status do stand: " + {True: "Ativo.", False: "Inativo."}[self.status_stand])
        self.ativarStand() if self.status_stand else self.desativarStand()