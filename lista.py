def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

# Exemplo de uso
lista_numeros = [10, 20, 30, 40, 50]
media = calcular_media(lista_numeros)
print(f"A média dos números é: {media}")

# Solicita um número inteiro ao usuário
x = int(input("Digite um número inteiro: "))

# Realiza uma operação, por exemplo, dobrar o valor
dobro = x * 2

# Exibe o resultado
print(f"O dobro de {x} é {dobro}")
