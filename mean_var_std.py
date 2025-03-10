# Crie uma função chamada calculate() em mean_var_std.py que use o Numpy para produzir a média, variância, desvio-padrão, máximo, mínimo e soma das linhas, colunas e elementos em uma matriz de 3 x 3.
# A entrada da função deve ser uma lista com 9 algarismos. A função deve converter a lista em um array 3 x 3 do Numpy e, em seguida, retornar um dicionário contendo a média, variância, desvio padrão, máximo, mínimo e soma ao longo de ambos os eixos e para a matriz nivelada.
# O dicionário retornado deve seguir esse formato:
# {
#   'mean': [axis1, axis2, flattened],
#   'variance': [axis1, axis2, flattened],
#   'standard deviation': [axis1, axis2, flattened],
#   'max': [axis1, axis2, flattened],
#   'min': [axis1, axis2, flattened],
#   'sum': [axis1, axis2, flattened]
# }
# Se uma lista que contiver menos de 9 elementos for passada para a função, ela deve criar uma exceção ValueError com a mensagem: "List must contain nine numbers." (A lista deve conter nove números). Os valores do dicionário retornado devem ser listas e não matrizes do Numpy.
# Por exemplo, calculate([0,1,2,3,4,5,6,7,8]) deve retornar:
# {
#   'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
#   'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
#   'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
#   'max': [[6, 7, 8], [2, 5, 8], 8],
#   'min': [[0, 1, 2], [0, 3, 6], 0],
#   'sum': [[9, 12, 15], [3, 12, 21], 36]
# }

import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        array = np.array(list).reshape(3,3)
        calculations = {
            'mean': [np.mean(array,axis=0).tolist(),
                     np.mean(array,axis=1).tolist(),
                     np.mean(array).tolist()],
            'variance': [np.var(array,axis=0).tolist(),
                         np.var(array,axis=1).tolist(),
                         np.var(array).tolist()],
            'standard deviation': [np.std(array,axis=0).tolist(),
                                   np.std(array,axis=1).tolist(),
                                   np.std(array).tolist()],
            'max': [np.max(array,axis=0).tolist(),
                    np.max(array,axis=1).tolist(),
                    np.max(array).tolist()],
            'min': [np.min(array,axis=0).tolist(),
                    np.min(array, axis=1).tolist(),
                    np.min(array).tolist()],
            'sum': [np.sum(array,axis=0).tolist(),
                    np.sum(array, axis=1).tolist(),
                    np.sum(array).tolist()]                    
        }
    return calculations