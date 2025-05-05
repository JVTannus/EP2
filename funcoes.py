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
