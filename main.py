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

def print_report(path, str_to_print):
    """ Objetivo    : Imprimir o relatório do método
        Parâmetro(s): path          -> caminho para salvar o arquivo
                      str_to_print  -> report a ser salvo
        Retorno(s)  : 
    """
    with open(path, "w") as file:
        file.write(str_to_print)
        file.close()

#*********Place to call functions **************

def main():
    qtd_Rows = 3
    qtd_Colums = 3

    Matriz_AC = np.zeros((qtd_Rows,qtd_Colums),dtype=np.float64)

    Matriz_AC = [[2, 5, 3],[5, 4, 3],[4, 3, 3]]
    W = [2, 3, 5]

    strPrint = Topsis.TOPSIS_Method(Matriz_AC,W)
    path = "C:\\Users\\Lucas\\Desktop\\Projects\\Metodo-Decisao-TOPSIS\\TopsisReport.txt"

    print(strPrint)
    print_report(path, strPrint)

if __name__ == "__main__":
    main()