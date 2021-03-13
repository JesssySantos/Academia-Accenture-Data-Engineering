# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:52:01 2021

@author: jessi
"""

import requests
import pyodbc

response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/distritos')
data = response.json()

password_usr = 'Pa$$w0rd1234'
conn = pyodbc.connect('Driver={SQL Server};''Server=sql-server-jessy2801.database.windows.net;'
                      'Database=BD_Dados_IBGE;''UID=sqluser;''PWD=%s' % (password_usr))
cursor = conn.cursor()
tam = len(data)

ufs_inseridos, cidades_inseridas, distritos_inseridos = [], [], []
progress = 0
for reg in data:
    #Dados UF
    dict_UF = reg['municipio']['microrregiao']['mesorregiao']['UF']
    uf_id, uf_sigla, uf_nome, uf_regiao = int(dict_UF['id']), dict_UF['sigla'], \
                                            dict_UF['nome'], dict_UF['regiao']['nome']
                                            
    #Dados Cidade
    dict_cidade = reg['municipio']
    cid_id, cid_nome = int(dict_cidade['id']), dict_cidade['nome']
    
    #Dados distrito
    distrito_id, distrito_nome = int(reg['id']), reg['nome']
    
    if cid_id not in cidades_inseridas:
        
        if uf_id not in ufs_inseridos:
            cursor.execute('INSERT INTO UF VALUES (?, ?, ?, ?)', 
                           uf_id, uf_sigla, uf_nome, uf_regiao)
            conn.commit()
            ufs_inseridos.append(uf_id)
        
        cursor.execute('INSERT INTO CIDADE VALUES (?, ?, ?)', cid_id, uf_id, cid_nome)
        conn.commit()
        cidades_inseridas.append(cid_id)

    cursor.execute('INSERT INTO DISTRITO VALUES (?, ?, ?)', distrito_id, cid_id, 
                   distrito_nome)
    conn.commit()
    distritos_inseridos.append(distrito_id)
    progress += 1
    
    print(progress, ' registros importados de ', tam, ' registros.')
        
with conn:
    crs = conn.cursor()
    crs.close()
print('Dados completamente importados.')
            
        
        

    