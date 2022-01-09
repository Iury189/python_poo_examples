class JoJo:
    # Construtor
# =============================================================================
#     def __init__(self, nome, stand):
#         self.nome = nome
#         self.stand = stand
# =============================================================================
    # Desconstrutor
# =============================================================================
#     def __del__(self):
#         print (f"O usuário {self.GetNome()} foi excluído pelo desconstrutor.")
# =============================================================================
    # Getter
    def GetNome(self): return self.nome
    def GetStand(self): return self.stand
    # Setter
    def SetNome(self, nome): self.nome = nome
    def SetStand(self, stand): self.stand = stand
    def Falar(self): print(f"Nome: {self.GetNome()} | Stand: {self.GetStand()}")