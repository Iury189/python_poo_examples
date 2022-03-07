import random

class Naruto():
    def falar1(self):
        print("Esse é meu jeito ninja!")

class Goku():
    def falar2(self):
        print("Oi, eu sou o Goku!")

class Seiya():
    def falar3(self):
        print("Me dê sua força Pégasu!")

class Papagaio(Naruto, Goku, Seiya):
    def repetir(self):
        random.choice((self.falar1, self.falar2, self.falar3))()

papagaio = Papagaio()
papagaio.repetir()