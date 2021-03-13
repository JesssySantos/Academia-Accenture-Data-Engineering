# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:36:37 2021

@author: jessi
"""

class Elevador(object):
    
    def __init__(self, andar_atual, n_andares, capacidade, passageiros_atual):
        self.andar_atual = andar_atual
        self.n_andares = n_andares
        self.capacidade = capacidade
        self.passageiros_atual = passageiros_atual
    
    def inicializa(self, n_andares, capacidade):
        self.n_andares = n_andares
        self.capacidade = capacidade
        
    def entra(self):
        if self.passageiros_atual < self.capacidade:
            self.passageiros_atual += 1
            print('Passageiros até o momento: ', self.passageiros_atual)
        else:
            print('Elevador Lotado!')
            
    def sai(self):
        if self.passageiros_atual > 0:
            self.passageiros_atual -= 1
            print('Passageiros até o momento: ', self.passageiros_atual)
        else:
            print('Elevador Vazio!')
    
    def sobe(self):
        if self.andar_atual != self.n_andares:
            self.andar_atual += 1
            print('Andar atual: ', self.andar_atual)
        else:
            print("Elevador já está no último andar!")
            
    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print('Andar atual: ', self.andar_atual)
        else:
            print('Elevador no térreo!')
            
def print_Menu():
    print('--------- MENU ---------')
    print('1 - Inicializar Elevador')
    print('2 - Inserir passageiro')
    print('3 - Remover passageiro')
    print('4 - Subir um andar')  
    print('5 - Descer um andar') 
    print('Pressione qualquer outro número para sair')         
            
if __name__ == '__main__':    
    
    while(True):
        print_Menu()
        op = int(input('Digite a operação desejada: '))
        
        if op == 1:
            objElevador = Elevador(0,0,0,0)
            num_andares = int(input('Insira o nº de andares do prédio: '))
            capacidade = int(input('Insira a capacidade de pessoas do elevador: ')) 
            objElevador.inicializa(num_andares, capacidade)
            print("Elevador inicializado com sucesso!")
            
        elif op == 2:
            objElevador.entra()
        elif op == 3:
            objElevador.sai()
        elif op == 4:
            objElevador.sobe()
        elif op == 5:
            objElevador.desce()
        else:
            print('Opção Inválida! Encerrando o programa...')
            break