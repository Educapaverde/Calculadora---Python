print("=== CALCULADORA BASICA ===")

while True:
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))

    while n2 == 0:
        print("Divisao por zero nao pode! Digite outro numero.")
        n2 = float(input("Digite o segundo numero novamente: "))

    print("Soma:", n1 + n2)
    print("Subtracao:", n1 - n2)
    print("Multiplicacao:", n1 * n2)
    print("Divisao:", round(n1 / n2, 2))
    print("Exponenciacao:", n1 ** n2)

    opcao = input("Continuar? (S/N): ")
    if opcao.upper() == "N":
        print("Programa encerrado!")
        break
