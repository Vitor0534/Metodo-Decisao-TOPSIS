import numpy as np

def return_bigger_number(vector):
    big_number=0
    for i in range(0,len(vector),1):
        big_number = vector[i] if(big_number < vector[i]) else big_number #thernary operator
    return big_number
#****************end_function*******************


def normalize_Vector_by_sum(vector):
    big_number = sum(vector)
    return np.array(vector)/big_number
#****************end_function*******************


#pega o maior valor da coluna e divide os elementos da coluna por ele
def normalize_Matrix_by_bigger_N(Matrix):
    for i in range(0,len(Matrix),1):
        big_number = max(Matrix[i])
        
        for j in range(0,len(Matrix[0]),1):
            Matrix[i][j] = Matrix[i][j]/big_number

    return Matrix
#****************end_function*******************


def normalize_Matrix(Matrix):
    Matrix_2 = []
    Matriz_N = normalize_Matrix_by_bigger_N(Matrix)
    print("matriz normalizada: " + str(Matriz_N))

    W_N = normalize_Vector_by_sum(W)
    print("vetor peso normalizado: "+str(W_N))
    
    for i in range(0, len(Matriz_N),1):
            Matrix_2.append(np.array(Matriz_N[i])*np.array(W_N))
    return Matrix_2
#****************end_function*******************
    
def get_maxA_minA_V2(Matriz_AC):

    max_A = []
    min_A = []
    for j in range(0,len(Matriz_AC[0]),1):
        rowMax = 0
        rowMin = 0
        for i in range(0,len(Matriz_AC),1):
            rowN.append(Matriz_AC[i][j])
        max_A.append(max(rowN))
        min_A.append(min(rowN))

    return [max_A, min_A]
#****************end_function*******************

def get_maxA_minA(Matriz_AC):

    max_A = []
    min_A = []

    for j in range(0,len(Matriz_AC[0]),1):
        rowMax = Matriz_AC[0][j]
        rowMin = Matriz_AC[0][j]
        for i in range(0,len(Matriz_AC),1):
            rowMax = Matriz_AC[i][j] if(rowMax < Matriz_AC[i][j]) else rowMax
            #print("rowMax["+str(i) +","+str(j)+"]: "+ str(rowMax))
            rowMin = Matriz_AC[i][j] if(rowMin > Matriz_AC[i][j]) else rowMin
            #print("rowMin["+str(i) +","+str(j)+"]: "+ str(rowMin))
            
        max_A.append(rowMax)
        min_A.append(rowMin)
    return [max_A, min_A]
#****************end_function*******************


def Distance_Euclidian(vector_A,vector_B):
    return np.sqrt(np.sum((np.array(vector_A)- np.array(vector_B))**2))
#****************end_function*******************

def Matriz_Distancia_minA_maxA(Matriz_AC, max_A, min_A):
    Matriz_D = []
    for i in range(0,len(Matriz_AC),1):
        Matriz_D.append([Distance_Euclidian(Matriz_AC[i],max_A),Distance_Euclidian(Matriz_AC[i],min_A)])
    return Matriz_D
#****************end_function*******************


def relative_proximity(Matriz_D):
    CCI = []
    for i in range(0,len(Matriz_D),1):
        CCI.append(Matriz_D[i][1]/(Matriz_D[i][0]+Matriz_D[i][1]))
    return np.array(CCI)
#****************end_function*******************



def TOPSIS_Method(Matriz_AC,W):
    print("\n******************TOPSI-Method********************\n")
    
    #Passo 1: normalizar Matriz_AC e o vetor W e obter Maximo negativo e positivo
    Matriz_N = normalize_Matrix(Matriz_AC)
    print("Matriz_N: " + str(Matriz_N))
    
    [max_A, min_A] = get_maxA_minA(Matriz_N)
    print("max_A = " + str(max_A))
    print("min_A = " + str(min_A))
    
    #Passo 2: calcular a distancia euclidiana de An para max_A e min_A
    Matriz_D = Matriz_Distancia_minA_maxA(Matriz_N, max_A, min_A)
    print("Passo 2 - Matrix_D: " + str(Matriz_D))
    
    #Passo 3: Determinar a Proximidade relativa
    CCI = relative_proximity(Matriz_D)

    #Passo 4: ordenar da maior para a menor proximidade relativa
    Rank = -np.sort(-CCI, axis = None) #inverti a ordem com o -, poderia usar np.fliplr() tb

    out = ""
    for i in range(0,len(Rank),1):
        out+="\n*****************" + str(i+1) +"º: "+str(Rank[i]) + "*********";
        
    
    return out
#***End Function *****************#           




#*********Place to call functions **************

#Melhoria---> implementar método para o user inserir --> {tamanho; valores} da matriz
#Melhoria---> implementar impressão da saida de todos os Passos no terminal
#Melhoria---> implementar a saida para mostrar o ranqueamento das alternativas A1, A2, A3,..., An
#Melhoria---> Bug: Alguns valores do passo 1 ficam diferentes, pode ser arredondamento

#Matrix of Alternatives by Criterius [m,n]
qtd_Rows, qtd_Colums = [3,3]
Matriz_AC = np.zeros((qtd_Rows,qtd_Colums),dtype=np.float64)
Matriz_AC = [[5,2,1],[1,5,3],[3,3,4]]

#print(len(Matriz_AC))
#print(len(Matriz_AC[1]))

#weights
W = [3,3,4]

#print(Distance_Euclidian([1,2,3],[4,5,6]))


#Calling TOPSIS_Method
print("\nResult:" + TOPSIS_Method(Matriz_AC,W))
