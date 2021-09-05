class TopsisUtils:
    """ Classe de utilidades para o método TOPSIS
    """
    def __init__(self, decimal_places = 3) -> None:
        """ Objetivo    : Construtor da classe TopsisUtils
            Parâmetro(s): decimal_places -> número de casas decimais a serem impressas.
                                            Por padrão 3 casas decimais serão impressas
            Retorno(s)  :
        """
        self.decimal_places =  decimal_places

    def format_matrix_to_string(self, matrix):
        """ Objetivo    : Imprimir a matiz no terminal
            Parâmetro(s): matrix            -> matriz a ser impressa
            Retorno(s)  : strMatrixFormat   -> string  com a matriz formatada
        """
        strMatrixFormat = ""

        for i in range(0, len(matrix)):
            strMatrixFormat = f'{strMatrixFormat}|'
            for j in range(0, len(matrix[0])):
                strMatrixFormat = f'{strMatrixFormat}{matrix[i][j]:.{self.decimal_places}f}\t'
            strMatrixFormat = f'{strMatrixFormat[:-1]}|\n'
        
        return strMatrixFormat

    def format_vector_to_string(self, vector):
        """ Objetivo    : Imprimir um vetor no terminal
            Parâmetro(s): vector            -> matriz a ser impressa
            Retorno(s)  : strVectorFormat   -> string  com a vetor formatada
        """
        strVectorFormat = "|"
        for i in range(0, len(vector)):
            strVectorFormat = f'{strVectorFormat}{vector[i]:.{self.decimal_places}f}\t'
        
        strVectorFormat = f'{strVectorFormat[:-1]}|'
        return strVectorFormat