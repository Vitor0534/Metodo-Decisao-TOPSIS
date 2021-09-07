"""
Autores : Lucas Macedo da Silva e Vitor de Almeida Silva

Projeto : TOPSIS-Method versão 1.2

Objetivo: Implmentar o método de apoio à tomada de decisão multicritério TOPSIS.
          Método implementado como parte da avaliação da disciplina de modelos e técnicas de apoio à tomada de decisão multicritério,
          ministrada pela Profª. Drª Nadya Regina Galo 

Uso     : Para utilizar o código acesse o método main e defina as variaveis
            qtd_Rows    -> se refere ao número de linhas da matriz de alternativas e critérios
            qtd_Colums  -> se refere ao número de colunas da matriz de alternativas e critérios
            Matriz_AC   -> informe a matriz de critérios e alternativas
            W           -> informe o vetor de pesos
            path        -> informe o caminho para salvar os arquivos
"""

import TOPSIS_Method as Topsis
import numpy as np
import csv
import pandas

def print_report(path, str_to_print):
    """ Objetivo    : Imprimir o relatório do método
        Parâmetro(s): path          -> caminho para salvar o arquivo
                      str_to_print  -> report a ser salvo
        Retorno(s)  : 
    """
    with open(path, "w") as file:
        file.write(str_to_print)
        file.close()

def convert_Matrix_to_Int(matrix):
    return np.array(matrix).astype(int)
    
def load_Data(Path):
    """ Objetivo    : Ler arquivo csv e extrair matriz de alternativas/critérios
        Parâmetro(s): path          -> caminho para ler aquivo
        Retorno(s)  : [alternative_names, criterios_names]: vetores dos nomes das alternativas e critérios
                      [Matrix_AC]: Matriz de valores de alternativas/critérios
                      [W]: vetor de pesos
    """
    alternative_names = []
    criterios_names = []
    Matrix_AC = []
    W = []

    with open(Path, newline='') as table:
        reader = csv.reader(table)
        criterios_names = next(reader)[0].split(';')
        for row in reader:
            for number in row:
                strSp = np.array(number.split(';'))
                if(strSp[0]!='W'):
                    alternative_names.append(strSp[0])
                    Matrix_AC.append(strSp[1:])
                else:
                    W.append(strSp[1:])

    Matrix_AC = convert_Matrix_to_Int(Matrix_AC)
    W = convert_Matrix_to_Int(W)

    print(alternative_names)
    print(criterios_names)
    print(np.array(Matrix_AC))
    print(W)
    return [alternative_names, criterios_names, Matrix_AC,W]


def code_V1():
    qtd_Rows = 3
    qtd_Colums = 3
    
    Matriz_AC = np.zeros((qtd_Rows,qtd_Colums),dtype=np.float64)

    Matriz_AC = [[2, 5, 3],[5, 4, 3],[4, 3, 3]]
    W = [2, 3, 5]

    strPrint = Topsis.TOPSIS_Method(Matriz_AC,W)
    path = "TopsisReport.txt"

    print(strPrint)
    print_report(path, strPrint)


def code_V2():
    [alternative_names, criterios_names, Matriz_AC,W] = load_Data("In-data.csv")

    strPrint = Topsis.TOPSIS_Method(Matriz_AC,W)
    path = "TopsisReport.txt"

    print(strPrint)
    print_report(path, strPrint)

#*********Place to call functions **************

def main():

    #Regra de entrada de dados V1.0
    #code_V1()

    #Regra de entrada de dados V2.0
    code_V2()
    

   
if __name__ == "__main__":
    main()
