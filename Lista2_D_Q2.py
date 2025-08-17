try:
    N = int(input("Quantos números você quer analisar? "))
    if N <= 0:
        print("Por favor, digite um número maior que 0!")
    else:
        n1 = float(input("Digite o 1° número: "))
        menor = n1
        maior = n1
        soma = n1
        for i in range(2, N + 1):
            numero = float(input(f"Digite o {i}° número: "))
            if numero < menor:
                menor = numero
            if numero > maior:
                maior = numero
            soma = soma + numero
        print(f"\nMenor valor: {menor}")
        print(f"Maior valor: {maior}")
        print(f"Soma dos valores: {soma}")
except ValueError:
    print("Entrada inválida! Digite apenas números.")