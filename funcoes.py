#1
import random
def rolar_dados(numero):
    return [random.randint(1,6) for i in range(numero)]

#2
def guardar_dado(dados_rolados, dados_guardados, indice):
    d = dados_rolados[indice]
    resp = []
    for i in range(len(dados_rolados)):
        if i != indice:
            resp.append(dados_rolados[i])
    
    dados_guardados.append(d)
    return [resp, dados_guardados]

#3
def remover_dado(dados_rolados, dados_guardados, indice):
    d = dados_guardados[indice]
    resposta = []
    for i in range(len(dados_guardados)):
        if i != indice:
            resposta.append(dados_guardados[i])
    
    dados_rolados.append(d)
    
    return [dados_rolados, resposta]

#4
def calcula_pontos_regra_simples(lista_face):
    pont = {}

    for f in range(1, 7):
        soma = 0
        for dado in lista_face:
            if dado == f:
                soma += dado
        pont[f] = soma

    return pont

#5
def calcula_pontos_soma(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

#6
def calcula_pontos_sequencia_baixa(lista):
    i = 0
    nova = []
    
    while i < len(lista):
        if lista[i] not in nova:
            nova.append(lista[i])
        i += 1
    
    if 1 in nova and 2 in nova and 3 in nova and 4 in nova:
        return 15
    if 2 in nova and 3 in nova and 4 in nova and 5 in nova:
        return 15
    if 3 in nova and 4 in nova and 5 in nova and 6 in nova:
        return 15
    else:
        return 0

#7
def calcula_pontos_sequencia_alta(lista):
    i = 0
    nova = []

    while i < len(lista):
        if lista[i] not in nova:
            nova.append(lista[i])
        i += 1
    if 1 in nova and 2 in nova and 3 in nova and 4 in nova and 5 in nova:
        return 30
    if 2 in nova and 3 in nova and 4 in nova and 5 in nova and 6 in nova:
        return 30
    else:
        return 0
    
#8
def calcula_pontos_full_house(dados):
    frequencias = {}
    total = 0

    for dado in dados:
        total += dado
        if dado in frequencias:
            frequencias[dado] += 1
        else:
            frequencias[dado] = 1

    num_2 = 0
    num_3 = 0

    for chave in frequencias:
        if frequencias[chave] == 2:
            num_2 += 1
        elif frequencias[chave] == 3:
            num_3 += 1

    if num_2 == 1 and num_3 == 1:
        return total
    return 0

#9
def calcula_pontos_quadra(dados):
    frequencias = {}
    total = 0

    for dado in dados:
        total += dado
        if dado in frequencias:
            frequencias[dado] += 1
        else:
            frequencias[dado] = 1

    for chave in frequencias:
        if frequencias[chave] >= 4:
            return total
    return 0

#10
def calcula_pontos_quina(dados):
    frequencias = {}

    for dado in dados:
        if dado in frequencias:
            frequencias[dado] += 1
        else:
            frequencias[dado] = 1

    for chave in frequencias:
        if frequencias[chave] >= 5:
            return 50
    return 0

#11
def cinco_iguais(dados):
    primeiro = dados[0]
    for valor in dados:
        if valor != primeiro:
            return 0
    return 50

def full_house(dados):
    contagens = [0, 0, 0, 0, 0, 0]
    for valor in dados:
        contagens[valor - 1] += 1

    tem_3 = False
    tem_2 = False
    for i in range(6):
        if contagens[i] == 3:
            tem_3 = True
        elif contagens[i] == 2:
            tem_2 = True

    if tem_3 and tem_2:
        return sem_combinacao(dados)
    return 0

def quadra(dados):
    contagens = [0, 0, 0, 0, 0, 0]
    for valor in dados:
        contagens[valor - 1] += 1

    for i in range(6):
        if contagens[i] >= 4:
            return 20
    return 0

def sem_combinacao(dados):
    soma = 0
    for valor in dados:
        soma += valor
    return soma

def sequencia_alta(dados):
    tem = [0, 0, 0, 0, 0, 0]
    for valor in dados:
        tem[valor - 1] = 1

    todos_presentes = True
    for i in range(5):
        if tem[i] != 1:
            todos_presentes = False
            break
    if todos_presentes:
        return 40

    todos_presentes = True
    for i in range(1, 6):
        if tem[i] != 1:
            todos_presentes = False
            break
    if todos_presentes:
        return 40

    return 0

def sequencia_baixa(dados):
    tem = [0, 0, 0, 0, 0, 0]
    for valor in dados:
        tem[valor - 1] = 1

    sequencias = [
        [0, 1, 2, 3],  # 1-4
        [1, 2, 3, 4],  # 2-5
        [2, 3, 4, 5],  # 3-6
    ]
    for seq in sequencias:
        encontrada = True
        for i in seq:
            if tem[i] != 1:
                encontrada = False
                break
        if encontrada:
            return 30
    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': cinco_iguais(dados),
        'full_house': full_house(dados),
        'quadra': quadra(dados),
        'sem_combinacao': sem_combinacao(dados),
        'sequencia_alta': sequencia_alta(dados),
        'sequencia_baixa': sequencia_baixa(dados),
    }
    
