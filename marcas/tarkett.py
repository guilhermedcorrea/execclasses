
import pandas as pd
import os
from marcas.consulta_bd import Select

class Tarkett:
    def __init__(self, marca):
        self.marca = marca
     
    def ajuste_skus(self, elementos):
        try:
            referencias = str(elementos).split("(")[0].strip()
            return referencias
        except:
            return 'valorinvalido'

    def converte_valores_float(self,elementos):
        if isinstance(elementos, str):
            try:
                saldo = elementos.replace(".","").replace(",",".").strip()
                saldo = float(saldo)
                return saldo
            except:
                return 'Error'
        else:
            try:
                return float(0)
            except:
                return 'Error'
    
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
        dftarkett = pd.read_excel('D:\\PythonJobs\\Hausz\\backendestoques\\files\\'+self.marca)
        dftarkett['Codigos'] = dftarkett['Codigos'].apply(lambda x: self.ajuste_skus(x))
        dftarkett['Saldos'] = dftarkett['Saldos'].apply(lambda x: self.converte_valores_float(x))
        dftarkett = dftarkett[['Codigos','Saldos']]
        tarkett = self.df_hausz('Tarkett','Desso')
        hauszdf = pd.DataFrame(tarkett)

        finall = pd.merge(hauszdf, dftarkett, left_on='Sku', right_on='Codigos', how='left')
        finall = finall[['IdMarca','Marca','Sku','NomeProduto','Saldos']]
        finall.fillna(0, inplace=True)
    
        
       



       


        