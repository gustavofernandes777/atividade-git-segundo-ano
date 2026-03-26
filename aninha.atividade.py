idade= int(input("Olá meu querido (a), por favor, imsira sua idade: "))
print(idade)
print()

autorizacao=(input("Possui a autorização do seu responsável? (sim / não):  "))
print(autorizacao)
print()

if idade >= 18:
   print("Entrada permitida, aproveite muito!")
elif idade >= 16 and autorizacao == "sim":
   print("Entrada permitida, aproveite muito!")
elif idade <= 16 and autorizacao == "sim":
   print("Entrada permitida, mas apenas com seu responsável.")
else:
   print("Entrada negada, sinto muito.")