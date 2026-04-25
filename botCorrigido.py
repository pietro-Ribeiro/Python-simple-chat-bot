import random
import math
from datetime import datetime

dicionario = {
    "oi": ["ola! no que posso ajudar", "oi, oque precisa?"],
    "tchau": ["ate mais!", "tchau!", "adeus!"],
    "horas": [datetime.now()],
    "pi": [math.pi, "o valor é basicamente 3,14", "3,14159"],
    "obrigado": ["de nada!", "nao a de que!", "nada kk"],
    "oque voce e": ["um bot simples", "codigos em python"],
}

print("Comandos: sair / aprender")
print("")

while True:
    fala = input("Voce: ").lower()
    
    if fala == "sair":
        print("Ate mais!")
        break
    
    if "aprender" in fala:
        chave = input("Digite a palavra/frase que eu devo aprender: ").lower()
        resp = input("O que eu respondo? ")
        dicionario[chave] = [resp]
        print("Aprendido! Agora sei o que responder.")
        continue
    
    if fala in dicionario:
        print("Bot:", random.choice(dicionario[fala]))
    else:
        print("Bot: Nao sei o que responder... me ensina usando 'aprender'")