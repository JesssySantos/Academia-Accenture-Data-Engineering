# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:52:05 2021

@author: jessi
"""
class Pessoa(object):
    
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
        
class Agenda(object):
    contatos = []
            
    def armazenaPessoa(self, nome, idade, altura):
        if len(self.contatos) < 10:
            dic = {}
            dic['nome'] = nome
            dic['idade'] = idade
            dic['altura'] = altura
            self.contatos.append(dic)
        else:
            print('Agenda Cheia!')
            
    def removePessoa(self, nome):
        idx = -1
        
        if len(self.contatos) == 0:
            print('Lista Vazia')
            return
        
        for pessoa in self.contatos:
            if pessoa['nome'] == nome:
                self.contatos.pop(idx)
                print(nome, ' removida com sucesso da agenda!')
                return
            idx += 1
        
        print('Pessoa não encontrada!')
        
    def buscaPessoa(self, nome):
        for pessoa in self.contatos:
            if pessoa['nome'] == nome:
                return self.contatos.index(pessoa)
        return -1
    
    def imprimeAgenda(self):
        for pessoa in self.contatos:
            print(pessoa)
            
    def imprimePessoa(self, index):
        
        print(self.contatos[index]) 

def print_Menu():
    print('--------- MENU ---------')
    print('1 - Adicionar contato')
    print('2 - Remover contato')
    print('3 - Buscar contato')
    print('4 - Imprime Pessoa')  
    print('5 - Imprimir Agenda') 
    print('0 - EXIT')         
            
if __name__ == '__main__':
    objAgenda = Agenda()
    op = True
    
    while(op):
        print_Menu()
        op = int(input('Digite a opção desejada:'))
        
        if op == 1:
            nome = input('Insira o nome:')
            idade = int(input('Insira a idade:'))
            altura = float(input('Insira a altura:'))
            objAgenda.armazenaPessoa(nome, idade, altura)
        elif op == 2:
            nome = input('Insira o nome do contato a ser removido:')
            objAgenda.removePessoa(nome)
        elif op == 3:
            nome = input('Insira o nome do contato a ser buscado:')
            if objAgenda.buscaPessoa(nome) > 0:
                print('O contato ', nome, ' localiza-se na posição ', objAgenda.buscaPessoa(nome), 'da agenda.')
        elif op == 4:
            idx = int(input('Insira o índice do contato a ser impresso:'))
            objAgenda.imprimePessoa(idx)
        elif op == 5:
            objAgenda.imprimeAgenda()
        elif op == 0:
            break
        else:
            print("Comando inválido!")
            
        
    
        
        
