# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:47:24 2021

@author: jessi
"""

class Televisao(object):
    def __init__(self, status_tv=True, volume=5, canal=1):
        self.status_tv = status_tv
        self.volume = volume
        self.canal = canal

class ControleRemoto(object):    
    def __init__(self, volume_max=50, canal_max=100, TV=Televisao()):
        self.volume_max = volume_max
        self.canal_max = canal_max
        self.TV = TV
        
    def aumenta_Volume(self):
        if self.TV.volume < self.volume_max:
            self.TV.volume += 1
            print('Volume Atual = ', self.TV.volume)
        else:
            print('Volume Máximo!')
            
    def diminui_Volume(self):
        if self.TV.volume > 0:
            self.TV.volume -= 1
            print('Volume Atual = ', self.TV.volume)
        else:
            print('TV no mudo!')
            
    def prox_Canal(self):
        if self.TV.canal < self.canal_max:
            self.TV.canal += 1
            print('Canal Atual = ', self.TV.canal)
        else:
            print('Último Canal!')
            
    def ant_Canal(self):
        if self.TV.canal > 1:
            self.TV.canal -= 1
            print('Canal Atual = ', self.TV.canal)
        else:
            print('Primeiro Canal!')
            
    def troca_Canal(self, new_canal):
        if new_canal > 0 and new_canal <=self.canal_max:
            self.TV.canal = new_canal
            print('Canal Atual = ', self.TV.canal)
            
    def canal_volume_atual(self):
        return self.TV.canal, self.TV.volume
    
def print_Menu():
    print('--------- MENU ---------')
    print('1 - Aumentar Volume')
    print('2 - Diminuir Volume')
    print('3 - Assistir Próximo Canal')
    print('4 - Assistir Canal Anterior')  
    print('5 - Assistir um canal específico') 
    print('6 - Consultar Canal/Volume Atuais') 
    print('Pressione qualquer outro número para sair')         
            
if __name__ == '__main__':
    controle_remoto = ControleRemoto()
    
    while(True):
        print_Menu()
        op = int(input('Insira a opção desejada:'))
        
        if op == 1:
            controle_remoto.aumenta_Volume()
        elif op == 2:
            controle_remoto.diminui_Volume()
        elif op == 3:
            controle_remoto.prox_Canal()
        elif op == 4:
            controle_remoto.ant_Canal()
        elif op == 5:
            canal = int(input('Digite o canal desejado:'))
            controle_remoto.troca_Canal(canal)
        elif op == 6:
            curr_canal, curr_volume = controle_remoto.canal_volume_atual()
            print('Canal atual = ', curr_canal, ' e volume atual = ', curr_volume)
        else:
            print('Opção Inválida! Encerrando o programa...')
            break
            
    
            
    