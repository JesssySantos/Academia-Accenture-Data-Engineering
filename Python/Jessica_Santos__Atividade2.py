#Jéssica Ap. Almeida dos Santos
import random

f = open("LISTA_PESSOAS PARA SORTEIO.txt", "r", encoding='latin1')
names = [line.replace('\n','') for line in f if line[0] != '#']
idx_sorteados = random.randrange(0, len(names)-1, 1)
f.close()

sorteados = []
for i in range(3):
    num_sorteado = random.randrange(0, len(names)-1, 1)
    sorteados.append(names.pop(num_sorteado))

print("----- SORTEADOS -----")
print('\n'.join(sorteados))

f = open("Pessoas Sorteadas.txt", "w+", encoding='latin1')
f.writelines(list( "%s\n" % item for item in sorteados))
f.close()
