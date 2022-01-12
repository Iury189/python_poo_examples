class JoJo:
    # Construtor
    def __init__(self):
        self.status_stand = False
    # Destrutor
    def __del__(self):
        print (f"O usuário {self.GetNome()} foi excluído pelo desconstrutor.")
    # Getter
    def GetNome(self): return self.nome
    def GetStand(self): return self.stand
    # Setter
    def SetNome(self, nome): self.nome = nome
    def SetStand(self, stand): self.stand = stand
    def AtivarStand(self):
        if self.status_stand:
            print(f"{self.GetStand()} já está invocado.")
        else:
            self.status_stand = True
            print(f"{self.GetStand()} foi invocado.")
    def DesativarStand(self):
        if self.status_stand == False:
            print(f"{self.GetStand()} já está oculto.")
        else:
            self.status_stand = False
            print(f"{self.GetStand()} foi ocultado.")
    def Falar(self): 
        print(f"Nome: {self.GetNome()} | Stand: {self.GetStand()}")
