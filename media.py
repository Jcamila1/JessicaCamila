valores = []

quantidade = int(input("Quantos números você quer digitar? "))

if quantidade > 0:
    for i in range(quantidade):
        numero = float(input(f"Digite o {i+1}º número: "))
        valores.append(numero)
    
    media = sum(valores) / len(valores)
    print("A média é:", media)
else:
    print("Você deve digitar pelo menos um número para calcular a média.")
