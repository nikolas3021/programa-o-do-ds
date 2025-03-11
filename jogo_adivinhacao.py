# Importa o módulo random, que contém funções para gerar números aleatórios
import random

# Gera um número aleatório entre 1 e 10 e o armazena na variável `numero_secreto`
numero_secreto = random.randint(1, 10)

# Define variáveis para acompanhar o número de tentativas e o limite máximo de tentativas
tentativas = 0
max_tentativas = 5

# Exibe uma mensagem de boas-vindas ao jogador e explica as regras do jogo
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Inicia o loop principal do jogo. O loop continua enquanto o número de tentativas for menor que o limite.
while tentativas < max_tentativas:
    try:
        # Solicita ao jogador que insira um número e tenta convertê-lo para inteiro
        palpite = int(input("\nDigite seu palpite: "))
        
        # Verifica se o número inserido está dentro do intervalo permitido
        if palpite < 1 or palpite > 10:
            print("Por favor, insira um número entre 1 e 10.")
            continue  # Retorna ao início do loop para que o jogador tente novamente
    except ValueError:
        # Captura erros caso o jogador insira algo que não seja um número inteiro
        print("Entrada inválida! Por favor, insira um número inteiro.")
        continue  # Retorna ao início do loop para nova entrada

    # Incrementa o número de tentativas feitas pelo jogador
    tentativas += 1

    # Verifica se o palpite do jogador é igual ao número secreto
    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou o número em {tentativas} tentativa(s).")
        break  # Encerra o loop caso o jogador acerte o número
    elif palpite < numero_secreto:
        # Dá uma dica ao jogador para tentar um número maior
        print("🔼 Quase lá! Tente um número maior.")
    else:
        # Dá uma dica ao jogador para tentar um número menor
        print("🔽 Quase lá! Tente um número menor.")

    # Informa ao jogador quantas tentativas ainda restam
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativa(s) restante(s).")
    else:
        print("\n😞 Infelizmente, suas tentativas acabaram.")

# Mensagem final para quando o jogador não acerta o número secreto
if palpite != numero_secreto:
    print(f"O número secreto era {numero_secreto}.")
print("🎮 Fim do jogo!")
