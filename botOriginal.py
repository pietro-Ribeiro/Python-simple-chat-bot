import random
import math
from datetime import datetime

dicionario = {
   "oi": ["ola! no que posso ajudar", "oi, oque precisa?"],
   "thau": ["até mais!", "thau!", "adeus!"],
   "horas": [datetime.now()],
   "reiniciar": ["[sistema reiniciado]"],
   "pi": [math.pi, "o valor é basicamente 3,14", "3,14159"],
   "obrigado": ["de nada!", "nao a de que!", "nada kk"],
   "oque voce é": ["um bot simples", "codigos em python"],
   
}

print("comandos :")
print("sair")
print("reiniciar")
print("")

while True:
    agora = datetime.now()
    fala = input()
    
    if fala in dicionario:
        print(random.choice(dicionario[fala]))
    if "aprender" in fala:
       chave = input("seu comando : ").lower()
       resp = input("eu digo : ")
    
    dicionario[chave] = [resp] # Adiciona no dicionário (fica na memória)
    print("Aprendido!")
    continue

    if fala == "sair":
        break
