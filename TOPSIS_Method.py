import numpy as np
import TOPSIS_Utils
from collections import OrderedDict

def normalize_vector_by_sum(vector):
    """ Objetivo    : Realiza a normalização do vetor de pesos pelo seu maior valor
        Parâmetro(s): vector    -> matriz com os critérios a ser normalizada
        Retorno(s)  : obj temp  -> vetor com os dados normalizado pelo maior valor do vetor
    """
    big_number = sum(vector)
    return np.array(vector)/big_number
#****************end_function*******************


def normalize_matrix_by_bigger_N(Matrix):
    """ Objetivo    : Realiza a normalização da matriz pelo seu maior valor
        Parâmetro(s): Matrix -> matriz com os critérios a ser normalizada
        Retorno(s)  : Matrix -> matriz normalizada pelo maior valor
    """

    # Pega o maior valor da coluna e divide os elementos da coluna por ele
    big_number = max(max(Matrix))
    for i in range(0,len(Matrix),1):
        
        for j in range(0,len(Matrix[0]),1):
            Matrix[i][j] = Matrix[i][j]/big_number

    return Matrix
#****************end_function*******************


def matrix_vector_multiply(Matrix, W):
    """ Objetivo    : Normalizar a matriz
        Parâmetro(s): Matrix    -> matriz com os critérios a ser normalizada
                      W         -> vetor de pesos a ser normalizado
        Retorno(s)  : Matrix_2  -> Matriz normalizada
    """
    Matrix_2 = []
    
    for i in range(0, len(Matrix),1):
            Matrix_2.append(np.array(Matrix[i])*np.array(W))
    return Matrix_2
#****************end_function*******************

def get_maxA_minA(Matriz_AC):
    """ Objetivo    : Encontrar a máxima solução negativa e a máxima solução posiutiva
        Parâmetro(s): Matriz_AC -> Matriz normalizada
        Retorno(s)  : max_A     -> vetor de soluções positivas
                      min_A     -> vetor de soluções negativas
    """
    max_A = []
    min_A = []

    for j in range(0,len(Matriz_AC[0]),1):
        rowMax = Matriz_AC[0][j]
        rowMin = Matriz_AC[0][j]
        for i in range(0,len(Matriz_AC),1):
            rowMax = Matriz_AC[i][j] if(rowMax < Matriz_AC[i][j]) else rowMax
            rowMin = Matriz_AC[i][j] if(rowMin > Matriz_AC[i][j]) else rowMin
        max_A.append(rowMax)
        min_A.append(rowMin)
    return [max_A, min_A]
#****************end_function*******************


def Distance_Euclidian(vector_A,vector_B):
    """ Objetivo    : Calcular a distância euvlidiana entre dois vetores
        Parâmetro(s): Matriz_AC -> Matriz normalizada
                      vector_A  -> vetor para calcular a distância
                      vector_B  -> vetor para calcular a distância 
        Retorno(s)  : obj temp  -> Matriz com as distâncias euclidianas entre os dois vetores
    """
    return np.sqrt(np.sum((np.array(vector_A)- np.array(vector_B))**2))
#****************end_function*******************

def Matriz_Distancia_minA_maxA(Matriz_AC, max_A, min_A):
    """ Objetivo    : Calcular para cada alternativa a distância euclidiana de cada avaliação para o vetor
                      de soluções positivas e para o vetor de soluções negativas
        Parâmetro(s): Matriz_AC -> Matriz normalizada
                      max_A     -> vetor de soluções positivas
                      min_A     -> vetor de soluções negativas
        Retorno(s)  : Matriz_D  -> Matriz com as distâncias
    """
    Matriz_D = []
    for i in range(0,len(Matriz_AC),1):
        Matriz_D.append([Distance_Euclidian(Matriz_AC[i],max_A),Distance_Euclidian(Matriz_AC[i],min_A)])
    return Matriz_D
#****************end_function*******************


def relative_proximity(Matriz_D):
    """ Objetivo    : Calcular a distância relativa CCi da matriz
        Parâmetro(s): Matriz_D  -> matriz com as distâncias
        Retorno(s)  : obj temp  -> vetor com as distâncias relativas
    """
    CCI = []
    for i in range(0,len(Matriz_D),1):
        CCI.append(Matriz_D[i][1]/(Matriz_D[i][0]+Matriz_D[i][1]))
    return np.array(CCI)
#****************end_function*******************

def order_by_proximity(CCI):
    """ Objetivo    : Ordenar a distância relativa CCi da matriz por proximidade
        Parâmetro(s): CCI       -> vetor com as distâncias relativas
        Retorno(s)  : obj temp  -> vetor com as distâncias relativas ordenado
    """

    # Cria um dicionário para mostrar a melhor alternativa
    # a chave do dicionário é o número da alternativa
    cci_dict = dict(zip(np.arange(1, len(CCI) + 1, 1), CCI))
    return sorted(cci_dict.items(), key=lambda x: x[1], reverse=True)

def TOPSIS_Method(Matriz_AC, W):
    """ Objetivo    : Aplicar o método TOPSIS em uma matriz de critérios e seu vetor de pesos
        Parâmetro(s): Matriz_AC -> matriz de critério
        Retorno(s)  : W         -> vetor de pesos
    """

    decimal_places = 4
    strReport = ""
    util = TOPSIS_Utils.TopsisUtils(decimal_places)

    strReport += 'Método TOPSIS\n\n'
    strReport += f'Matriz de critérios e alternativas de entrada\n{util.format_matrix_to_string(Matriz_AC)}\n' 
    
    # Passo 1: normalizar a matriz de critérios e alternativas e o vetor W
    # e obter Maximo negativo e positivo    
    Matriz_AC = normalize_matrix_by_bigger_N(Matriz_AC)
    W = normalize_vector_by_sum(W)

    strReport += '--------------------- Passo 1 ---------------------\n'
    strReport += f'Matriz de critérios e alternativas normalizada\n{util.format_matrix_to_string(Matriz_AC)}\n' 
    strReport += f'Vetor de pesos normalizado\n{util.format_vector_to_string(W)}\n\n' 

    Matriz_N = matrix_vector_multiply(Matriz_AC, W)
    strReport += f'Matriz de critérios * vetor de pesos\n{util.format_matrix_to_string(Matriz_N)}\n' 

    [max_A, min_A] = get_maxA_minA(Matriz_N)
    strReport += f'Vetor com as máximas soluções positivas\n{util.format_vector_to_string(max_A)}\n' 
    strReport += f'Vetor com as máximas soluções negativas\n{util.format_vector_to_string(min_A)}\n\n' 
    
    # Passo 2: calcular a distancia euclidiana de An para max_A e min_A
    strReport += '--------------------- Passo 2 ---------------------\n'
    Matriz_D = Matriz_Distancia_minA_maxA(Matriz_N, max_A, min_A)
    strReport += f'Matriz com as distâncias euclidianas\n{util.format_matrix_to_string(Matriz_D)}\n' 

    # Passo 3: Determinar a Proximidade relativa
    strReport += '--------------------- Passo 3 ---------------------\n'
    CCI = relative_proximity(Matriz_D)
    strReport += f'Vetor com as distâncias relativas\n{util.format_vector_to_string(CCI)}\n\n' 

    #Passo 4: ordenar da maior para a menor proximidade relativa
    strReport += '--------------------- Passo 4 ---------------------\n'
    Rank = order_by_proximity(CCI)

    out = ""
    for i in range(0,len(Rank),1):
        out += f'{str(i+1)}º: A{Rank[i][0]} -> {Rank[i][1]:.{decimal_places}f}\n'

    strReport += f'Ordenação das alternativas\n{out}\n' 

    strReport += f'Portanto, a melhor alternativa é: A{Rank[0][0]}\n' 

    return strReport
#***End Function *****************#           

