# Sua solução aqui
altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ")

if sexo == "M":
    peso_ideal = (72.7*altura) - 58
else:
    peso_ideal = (62.1*altura)- 44.7
print ( f"{peso_ideal:.2f}")
