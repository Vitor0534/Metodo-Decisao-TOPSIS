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
from Report_Utils import ReportUtils
from os import system, name
import Header

def clear():
    """ Objetivo    : Limpar o cmd de execução
                    Parâmetro(s): 
                    Retorno(s)  :
    """
    # Windows
    if name == 'nt':
        _ = system('cls')
  
    # Mac e Linu
    else:
        _ = system('clear')


def menu(): 
    """ Objetivo    : menu de interação com o usuário
                    Parâmetro(s): 
                    Retorno(s)  :
    """
    decimal_places = 3               # Informe a quantidade de casas decimais a serem mostradas no relatorio
    reportName = "\TOPSISRport-0.txt"  # Informe o nome do relatório a ser salvo ao final da execução
                                     # No nome do arquivo colocar /NomeArquivo.extensão
    rpUtil = ReportUtils(reportName = reportName)

    clear()

    print(Header.getHeader())    
    print('')
    print('Selecione o arquivo com extensão .csv que contém os dados')
    print('Pressione qualquer tecla para continuar...')
    input()

    clear()

    if rpUtil.openFileExplorer():

        [alternative_names, criterios_names, Matriz_AC,W] = rpUtil.load_Data()

        strPrint = Topsis.TOPSIS_Method(Matriz_AC, W, alternative_names, criterios_names, decimal_places)

        print(strPrint)

        print('Selecione o diretório em que o relatório será salvo:')
        print('Pressione qualquer tecla para continuar...')
        input()

        if rpUtil.openDirectoryExplorer():
            rpUtil.print_report(strPrint)
        else: 
            print('Nenhum diretório selecionado')
    else:
        print('Nenhum arquivo selecionado!')            

#*********Place to call functions **************

def main():
    menu()
    

   
if __name__ == "__main__":
    main()
