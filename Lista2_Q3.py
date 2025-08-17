print ("Operação - Adição!\n")
resposta = "S"
while resposta == "S":
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    print(f"\nA soma é {n1+n2}")
    resposta = input("\nDeseja realizar mais uma soma? [S ou N] ").upper()
    if resposta != "S" and resposta != "N":
        print("Opção inválida! Digite 'S' ou 'N'")
        resposta = "S"
    elif resposta == "N":
        print("Programa encerrado!")
        break
