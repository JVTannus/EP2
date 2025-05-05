#1
import random
def rolar_dados(numero):
    return [random.randint(1,6) for i in range(numero)]

#2
def guardar_dado(dados_rolados, dados_guardados, indice):
    dado = dados_rolados[indice]
    novos_dados_rolados = dados_rolados[:indice] + dados_rolados[indice+1:]
    novos_dados_guardados = dados_guardados + [dado]
    return novos_dados_rolados, novos_dados_guardados