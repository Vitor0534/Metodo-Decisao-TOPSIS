# Metodo-Decisao-TOPSIS

Autores: 
- Lucas Macedo da Silva  (git-link: )
- Vitor de Almeida Silva


O presente repositório contem a implementação do método de decisão multicritério TOPSIS

Para executar o algoritmo instale o python 3.8 em seu computador e execute o arquivo de nome main.py

O algorítmo recebe como entrada um arquivo .csv que deve conter a Matriz de decisão e o vetor de pesos, no seguite padrão:
  
  - Coluna 1, nome das alternativas;
  - Linha 1, nome dos critérios;
  - As celular internas [2][2] até [n][m], correpondem aos valores de relação entre as An alternativas e os Cm critérios

Ao final o programa imprime um relatório contendo a descrição de cada passo no terminal e permite que o usuário salve um relatório em .txt

Para utilizar o método em um programa, basta baixar o repositório e importar o arquivo TOPSIS_Method.py. A principal função é chamada da seguinte forma:

  -  TOPSIS_Method(Matriz_AC, W, alternative_names, criterios_names, decimal_places)

.
.
.
.
.
.

### English --------------------------------------------------------------------------

This repository contains the implementation of the TOPSIS multicriteria decision method

To run the algorithm install python 3.8 on your computer and run the file named main.py

The algorithm receives as input a .csv file that must contain the Decision Matrix and the weight vector, in the following pattern:
  
  - Column 1, name of alternatives;
  - Line 1, name of criteria;
  - The internal cells [2][2] to [n][m], correspond to the values of the relationship between the alternative An and the C criteria

In the end, the program prints a report containing the description of each step in the terminal and allows the user to save a report in .txt

To use the method in a program, just download the repository and import the file TOPSIS_Method.py. The main function is called as follows:

  - TOPSIS_Method(Matrix_AC, W, alternative_names, criteria_names, decimal_places)
