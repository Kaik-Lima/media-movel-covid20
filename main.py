import pandas as pd
import numpy as np
import queue


def mediaMovel(array, limite):
    fila = queue.Queue()
    soma = 0
    result = []
    for contador in array:
        fila.put(contador)
        soma += contador
        while fila.qsize() >= limite:
            result.append(soma / limite)
            retirada = fila.get()
            soma = soma - retirada
    return result


# Importando os dados
datas = pd.read_excel('semanal-2020.xlsx')
# Criando array somente com os casos
casos = np.array(datas['Casos Novos'])
# Tamanho do limite para média
limite = 3
# Chamada da função
valores = mediaMovel(casos, limite)
# Impressão
for c in valores:
    print(f'{c:.2f}', end=' ')
