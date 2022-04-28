from marcas import (tarkett, level, incepa, roca, level)

import pandas as pd
import os
import re

def exibe(brand):
    if re.search('deca|Deca|DECA',brand):
       pass

    if re.search('bobinex|Bobinex|BOBINEX', brand):
        pass
    
    if re.search('LEVEL|Level|level',brand):
       level.Level(brand).excel_reader()

    if re.search('Incepa|incepa', brand):
        incepa.Incepa(brand).excel_reader()
     
    if re.search('Roca|roca', brand):
       roca.Roca(brand).excel_reader()

    if re.search('tarkett|Tarkett', brand):
        tarkett.Tarkett(brand).excel_reader()
        
dirname = os.path.dirname('files/')
files = os.listdir(dirname)
valor = list(filter(lambda x: exibe(x),files))


