def calcular_engajamento_por_seguidores(curtidas, comentarios, compartilhamentos, seguidores):
    if seguidores == 0:
        return "Número de seguidores não pode ser zero"
    engajamento = (curtidas + comentarios + compartilhamentos) / seguidores * 100
    return round(engajamento, 2)

# Exemplo de uso
curtidas = int(input("Digite o número de curtidas: "))
comentarios = int(input("Digite o número de comentários: "))
compartilhamentos = int(input("Digite o número de compartilhamentos: "))
seguidores = int(input("Digite o número de seguidores: "))

resultado = calcular_engajamento_por_seguidores(curtidas, comentarios, compartilhamentos, seguidores)
print(f"Taxa de engajamento por seguidores: {resultado}%")

def calcular_engajamento_por_alcance(curtidas, comentarios, compartilhamentos, alcance):
    if alcance == 0:
        return "O alcance não pode ser zero"
    engajamento = (curtidas + comentarios + compartilhamentos) / alcance * 100
    return round(engajamento, 2)

# Exemplo de uso
curtidas = int(input("Digite o número de curtidas: "))
comentarios = int(input("Digite o número de comentários: "))
compartilhamentos = int(input("Digite o número de compartilhamentos: "))
alcance = int(input("Digite o alcance da publicação: "))

resultado = calcular_engajamento_por_alcance(curtidas, comentarios, compartilhamentos, alcance)
print(f"Taxa de engajamento por alcance: {resultado}%")

def calcular_engajamento_por_impressoes(curtidas, comentarios, compartilhamentos, impressoes):
    if impressoes == 0:
        return "O número de impressões não pode ser zero"
    engajamento = (curtidas + comentarios + compartilhamentos) / impressoes * 100
    return round(engajamento, 2)

# Exemplo de uso
curtidas = int(input("Digite o número de curtidas: "))
comentarios = int(input("Digite o número de comentários: "))
compartilhamentos = int(input("Digite o número de compartilhamentos: "))
impressoes = int(input("Digite o número de impressões da publicação: "))

resultado = calcular_engajamento_por_impressoes(curtidas, comentarios, compartilhamentos, impressoes)
print(f"Taxa de engajamento por impressões: {resultado}%")
