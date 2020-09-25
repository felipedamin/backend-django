# -*- coding: utf-8 -*-
import re

a = "olá, viado, puta"
b = "chefe legal"
def redflag(text):
    alerta = {
        'LGBTQ+fóbicos' : ['viado', 'boiola', 'gayzinho', 'veado', 'bicha', 'bixa'], 
        'machista' : ['vagabunda', 'puta', 'prostituta', 'boceta', 'buceta', 'biscate', 'vadia'],
        'racista': ['neguinho'],
    }                                        
    res = re.findall(r'\w+', text) 
    termos = []
    palavras = []
    for i in range(len(res)):
        (termo, palavra) = get_key(res[i], alerta)
        if termo != ():
            termos.append(termo)
            palavras.append(palavra)
    if termos != []:
        #print("Atenção você usou termos inadequados das seguintes naturezas: ", end = '')
        return [termos, palavras]
        for i in range(len(termos)):
            if i == len(termos)-1:
                print(termos[i]) 
            else:
                print(termos[i] + ', ', end = '')
        print("As palavras ofensivas são: ", end = '')
        for i in range(len(palavras)):
            if i == len(palavras)-1:
                print(palavras[i]) 
            else:
                print(palavras[i] + ', ', end = '')
    return ''


            
def get_key(val, redflag): 
    for key, value in redflag.items():
        for i in range(len(value)):
            if val == value[i]:
                return (key, val) 
      
    return ((), ())
