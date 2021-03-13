# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:26:21 2021

@author: jessi
"""
import datetime as dt

class Pessoa(object):
    
    def __init__(self, nome, dt_nasc, altura):
        self.__nome = nome
        self.__dt_nasc = dt_nasc
        self.__altura = altura
        
    def print_Pessoa(self):
        print('Nome:', self.__nome)
        print('Data de Nascimento:', self.__dt_nasc.strftime('%d/%m/%Y'))
        print('Altura:', self.__altura)
        
    def idade_Pessoa(self):
        return dt.datetime.now().year - self.__dt_nasc.year
    
def print_Menu():
    print('--------- MENU ---------')
    print('1 - Criar Pessoa')
    print('2 - Imprimir Pessoa')
    print('3 - Consultar Idade da Pessoa') 
    print('Pressione qualquer outro número para sair')
    
if __name__ == '__main__':
    while(True):
        print_Menu()
        op = int(input('Digite a opção desejada: '))
        
        if op == 1:
            nome = input('Digite o nome da pessoa: ')
            dt_nascimento = input('Digite a data de nascimento da pessoa no formato d/m/AAAA: ')
            dt_nascimento = dt.datetime.strptime(dt_nascimento, '%d/%m/%Y')
            altura = float(input('Digite a altura da pessoa com ponto flutuante: '))
            objPessoa = Pessoa(nome, dt_nascimento, altura)
        elif op == 2:
            objPessoa.print_Pessoa()
        elif op == 3:
            print('Idade da pessoa: ', objPessoa.idade_Pessoa())
        else:
            print('Opção Inválida! Encerrando o programa...')
            break
        