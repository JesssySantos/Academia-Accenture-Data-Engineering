# -*- coding: utf-8 -*-
#author: Jéssica Santos

import pyodbc

password_usr = input('Digite a senha do usuário sa:')
conn = pyodbc.connect('Driver={SQL Server};''Server=LOCALHOST\\SqlExpress;'
                      'Database=Atividade02_Python;''UID=sa;''PWD=%s' % (password_usr))

dados_faturamento = open(r'DADOS_FATURAMENTO.txt', encoding='latin1')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE FATURAMENTO (ID	INT	NOT NULL IDENTITY(1, 1),
                DT DATE NOT NULL,
                COD_ORCAMENTO INTEGER NOT NULL,
                COD_PROJ INTEGER NOT NULL,
                FATURAMENTO	DECIMAL(10, 2)	NOT NULL);''')
conn.commit()
print('Tabela FATURAMENTO criada com sucesso!')

for line in dados_faturamento:
    data = line[:8]
    cod_orcamento = int(line[8:12])
    cod_proj = int(line[12:16])
    faturamento = float(line[16:].replace('\n',''))
    cursor.execute('INSERT INTO FATURAMENTO VALUES (CAST(? AS DATETIME), ?, ?, ?)',
                   data, cod_orcamento, cod_proj, faturamento)
conn.commit()
dados_faturamento.close()    
print('Valores inseridos na tabela FATURAMENTO com sucesso!')
    