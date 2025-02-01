def ranked (vitorias, derrotas):
    pontos = vitorias - derrotas
    return pontos

vitorias =123
derrotas =21
nivel =(ranked(vitorias, derrotas))
print(nivel)
if 1<= nivel <10:
    print("Ferro")
elif 10<= nivel <= 21:
    print ("Bronze")
elif 21<= nivel <=50:
   print("prata")
elif 51<= nivel <=80:
    print("ouro")
elif 81<= nivel <=90:
    print("diamante")
elif 91<= nivel <=100:
    print("lendario")
else:
    print("imortal")