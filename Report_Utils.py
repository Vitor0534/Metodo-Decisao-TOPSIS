import tkinter as tk
from datetime import datetime
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

class ReportUtils:

    def __init__(self, path = "", reportName = "", file = None) -> None:
        """ Objetivo    : Construtor da classe ReportUtils
            Parâmetro(s): path          -> caminho arquivo
                          reportName    -> nome do relatório a ser salvo
            Retorno(s)  :
        """
        self.path = path
        self.file = file
        self.reportName = reportName

    def version_Controller_V1(self,var):
        name_report= self.reportName.split('.')[0].split('-')
        name_report[1] = int(name_report[1])+1
        print(name_report)
        self.reportName = str(name_report[0]) + '-' + str(name_report[1]) + '.' + str(self.reportName.split('.')[1])
        print(self.reportName)
        self.print_report(self)
        
    def version_Controller_V2(self,var):
        name_report= self.reportName.split('.')[0].split('-')
        name_report[1] = datetime.now().strftime("%Y_%m_%d %H:%M:%S:%f")
        print(name_report)
        self.reportName = str(name_report[0]) + '-' + str(name_report[1]) + '.' + str(self.reportName.split('.')[1])
        print(self.reportName)

    def version_Controller(self):
        """ Objetivo    : Retornar um cabeçalho com a data e hora de geração do relatório
            Parâmetro(s):
            Retorno(s)  : obj temp -> string formatada representando o cabeçalho
        """       
        return f'---------------------------------------------------------------------------------\nRelatório gerado em {datetime.now().strftime("%d/%m/%Y ás %H:%M:%S")}\n\n'

    def print_report(self, str_to_print):
        """ Objetivo    : Imprimir o relatório do método
            Parâmetro(s): path          -> caminho para salvar o arquivo
                        str_to_print  -> report a ser salvo
            Retorno(s)  : 
        """
        if self.file != None:
           self.file.write(f'{self.version_Controller()}{str_to_print}\n')
           self.file.close()


    
    def load_Data(self):
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
        strLineList = []

        with open(self.path, 'r') as table:
            strLineList = table.readlines()
            strLineListSplit = []

            # A primeira linha é referente ao nome dos critérios
            # A primeira coluna da primeira linha é vazia
            # Pega o nome dos critérios
            criterios_names = strLineList[0].replace('\n', '').split(';')[1:]

            # Inicia a partir da segunda linha, pois a primeira é referente ao nome dos criterios
            for i in range(1, len(strLineList)):
                line = strLineList[i].replace('\n', '')

                strLineListSplit = line.split(';')

                alternative_names.append(strLineListSplit[0])
                rowVector = []

                for ln in strLineListSplit[1:]: 
                    rowVector.append(int(ln)) if strLineListSplit[0] != 'W' else W.append(int(ln)) 

                if rowVector != []:
                    Matrix_AC.append(rowVector) 

        return [alternative_names, criterios_names, Matrix_AC, W]
    
    def openFileExplorer(self):
        """ Objetivo    : Abrir o explorador de aquivos para o usuário selecionar o arquivo de entrada
            Parâmetro(s): 
            Retorno(s)  : obj temp -> true caso o usuário tenha selecionado o arquivo, false caso contrário 
        """
        root = tk.Tk()
        root.withdraw()
        try:
            self.path = filedialog.askopenfilenames(filetypes=[('Arquivo de entrada','.csv')])[0]
        except:
            return False

        return self.path != ""
    
    def openDirectoryExplorerTosaveFile(self):
        """ Objetivo    : Abrir o explorador de aquivos para o usuário selecionar o diretório em que o report será salvo
            Parâmetro(s): 
            Retorno(s)  : obj temp -> true caso o usuário tenha selecionado o diretório, false caso contrário 
        """              
        root = tk.Tk()
        root.withdraw()

        files = [('Text Document', '*.txt')]

        self.file = asksaveasfile(filetypes = files, defaultextension = files, mode='a')

        return self.file != None
