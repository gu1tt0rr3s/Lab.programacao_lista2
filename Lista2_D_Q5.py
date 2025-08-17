numero = int(input("Digite um número inteiro: "))
if numero < 2:
    print("Não é primo")
elif numero == 2: #verifica se o número é 2 já que 2 é o único número par primo
    print("É primo")
elif numero % 2 == 0:
    print("Não é primo")
else:
    for i in range(3, numero // 2, 2): #testa os ímpares até numero//2. Se 24÷3=8, já sabemos que 3 e 8 são divisores (vêm em pares)
        if numero % i == 0:
            print("Não é primo")
            break
    else:
        print("É primo")