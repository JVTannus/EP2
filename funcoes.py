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