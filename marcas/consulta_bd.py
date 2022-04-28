from sqlalchemy import text
import pyodbc
from sqlalchemy import create_engine
import dotenv
import os
from urllib.parse import quote_plus
from sqlalchemy import text


class Select:

    dotenv.load_dotenv(dotenv.find_dotenv())
   
    def __init__(self, sku):
        self.sku = sku
        self.driver  = os.getenv('driver')
        self.Server = os.getenv('server')
        self.usuario = os.getenv('usuario')
        self.tabela = os.getenv('database')
        self.password = os.getenv('password')

    def get_connection(self):
        connection_string = """{};SERVER={};DATABASE={};UID={};PWD={}""".format(self.driver,self.Server,self.tabela,self.usuario,self.password)
        url_db = quote_plus(connection_string)
        connection_url = f'mssql+pyodbc:///?odbc_connect=+{url_db}'
        return create_engine(connection_url,fast_executemany=True)


    def executa_consulta(self, sku):
        
        engine = self.get_connection()
        with engine.connect() as conn:
            skuselect = conn.execute(text("""SELECT brand.Marca,brand.IdMarca,basico.[SKU],basico.[NomeProduto]
                    FROM [HauszMapa].[Produtos].[ProdutoBasico] as basico
                    JOIN Produtos.Marca as brand
                    on brand.IdMarca = basico.IdMarca
                    where brand.Marca like '%{}%'""".format(sku))).all()

            return skuselect

          
     

           

            
               
'''
   desc["Marca"] = skuselect.Marca
                desc['IdMarca'] = skuselect.IdMarca
                desc['Sku'] = skuselect.SKU
                desc['NomeProduto'] = skuselect.NomeProduto
'''
    
