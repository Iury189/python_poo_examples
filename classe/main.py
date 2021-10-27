import pyttsx3
from dobrador import Dobrador

voz = pyttsx3.init()
tipo = voz.getProperty('voices')
voz.setProperty('voice', tipo[1].id)
 
d1 = Dobrador()
while True:
  nome_dobrador = str(input("Digite o nome do dobrador: "))
  if (len(nome_dobrador.strip()) <= 0):
    print('O nome não pode ficar vazio, digite novamente.')
  else:
    d1.setNome(nome_dobrador.title())
    break
while True:
  elemento_dobrador = str(input("Digite o elemento do dobrador: "))
  if (len(elemento_dobrador.strip()) <= 0):
    print('O elemento do dobrador não pode ficar vazio, digite novamente.')
  else:
    d1.setElemento(elemento_dobrador.title())
    break
voz.say(d1.Falar())
voz.runAndWait()
