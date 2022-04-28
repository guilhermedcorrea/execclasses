import pandas as pd
import os
from marcas.consulta_bd import Select

class Level:
    file = 'D:\\PythonJobs\\Hausz\\backendestoques\\files\\'
    def __init__(self, marca):
        self.marca = marca
        
    def excel_reader(self):
        lista_dfs = []
        dflevel = pd.ExcelFile(self.file+str(self.marca).replace('~$',''))
        for sheet in dflevel.sheet_names:
            lista_dfs.append(sheet)
        print(lista_dfs)
            
            


