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
def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]
    novos_dados_rolados = dados_rolados + [dado]
    novos_dados_no_estoque = dados_no_estoque[:dado_para_remover] + dados_no_estoque[dado_para_remover+1:]
    return novos_dados_rolados, novos_dados_no_estoque