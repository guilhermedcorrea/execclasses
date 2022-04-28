
from sqlite3 import Row
import pandas as pd
import os
from marcas.consulta_bd import Select
import re

class Incepa:
    def __init__(self, marca):
        self.marca = marca

    def converte_valores_float(self, elementos):
        try:
            elementos = str(elementos).split("\n")[-1].strip().replace(",",".")
            return elementos
        except:
            return float(0)

    def ajuste_referencia_sku(self, elementos):
        try:
            skus = elementos.strip()
            return skus
        except:
            return 'valornaoencontrado'

    def df_hausz(self, *sku):

        lista_dicts = []
        if type(sku) == str():
            refs = Select(sku).executa_consulta(sku)
            desc = {}
            for key in refs:
                desc = {}
                desc['Marca'] = key[0]
                desc['IdMarca'] = key[1]
                desc['Sku'] = key[2]
                desc['NomeProduto'] = key[3]
                lista_dicts.append(desc)
            
        else:
            consulta = [Select(sku).executa_consulta(x) for x in sku]
            for cons in consulta:
                for x in cons:
                    desc = {}
                    desc['Marca'] = x[0]
                    desc['IdMarca'] = x[1]
                    desc['Sku'] = x[2]
                    desc['NomeProduto'] = x[3]
                    lista_dicts.append(desc)
           
        return lista_dicts

     
    def excel_reader(self):
        dfincepa = pd.read_csv('D:\\PythonJobs\\Hausz\\backendestoques\\files\\'+self.marca, sep=";")
        dfincepa.fillna(0, inplace=True)
        dfincepa['Saldo0'] = dfincepa['Saldo0'].apply(lambda x: self.converte_valores_float(x))
        dfincepa['Referencia'] = dfincepa['Referencia'].apply(lambda x: self.ajuste_referencia_sku(x))
        dfincepa = dfincepa[['Referencia','Nome','Saldo0']]
        incepa = self.df_hausz('Incepa')
        hauszdf = pd.DataFrame(incepa)
      
        finall = pd.merge(hauszdf, dfincepa, left_on='Sku', right_on='Referencia', how='left')
        finall.fillna(0, inplace=True)
        finall = finall[['IdMarca','Marca','Sku','NomeProduto','Saldo0']]
    

       
        
       