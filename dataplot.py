from random import randrange, seed
import matplotlib.pyplot as plt

# seed(2) # quando colocamos um numero inteiro o random tem sempre o mesmo comportamento
notas_matematica = []

for notas in range(8):
  notas_matematica.append(randrange(0,11))


x = list(range(1,9,1))
y = notas_matematica
plt.plot(x,y, marker='o')
plt.title('Notas Matematicas')
plt.xlabel('provas')
plt.ylabel('notas')
plt.show()
