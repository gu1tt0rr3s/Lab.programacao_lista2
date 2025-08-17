estados = ["S", "C", "V", "D"]

while True:
        nome = str(input("Digite seu nome: "))
        if len(nome) > 3:
            break
        else:
            print("Nome inválido! Digite um nome maior que 3 caracteres")
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida! Digite uma idade entre 0 e 150.")
    except ValueError:
        print("Idade inválida! Digite apenas números entre 0 e 150.")
while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        else:
            print("Salário inválido! Digite um salário maior que 0")
    except ValueError:
        print("Salário inválido! Digite apenas números")
while True:
        sexo = str(input("Digite seu sexo: [M ou F] ")).upper()
        if sexo == "M" or sexo == "F":
            break
        else:
            print("Sexo inválido! Digite apenas 'M' ou 'F'")
while True:
        ec = str(input("Digite seu estado civil: [S-Solteiro, C-Casado, V-Viúvo, D-Divorciado] ")).upper()
        if ec in estados:
            break
        else:
            print("Estado civil inválido! Digite apenas 'S', 'C', 'V' ou 'D'")
ecs = {
     "S": "Solteiro",
     "C": "Casado",
     "V": "Viúvo",
     "D": "Divorciado"
}
sexos = {
     "M": "Masculino",
     "F": "Feminino"
}
print("\nDados validados com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:,.2f}".replace(",", "."))
print(f"Sexo: {sexos[sexo]}")
print(f"Estado Civil: {ecs[ec]}")