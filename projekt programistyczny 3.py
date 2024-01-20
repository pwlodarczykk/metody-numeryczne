import numpy as np
import matplotlib.pyplot as plt

#ZADANIE 1
r, K, h = 0.4, 100000, 0.1
t = np.arange(75, 150, h)
N, N[0] = np.zeros(t.shape[0]), 10
NV, NV[0] = np.zeros(t.shape[0]), 10

for i in range(1, N.shape[0]):
    N[i] = N[i-1] + h*r*N[i-1]*np.log(K/N[i-1])
    NV[i] = NV[i-1] + h*(r*NV[i-1]*(K - NV[i-1])/K)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.plot(t, N, color = 'r', label='Model Gompertza')
axes.plot(t, NV, color = 'b', label='Model Verhulsta')
axes.set_xlabel('Czas')
axes.set_ylabel('Objętość guza')
plt.legend()
axes.grid(True)
plt.show()

#ZADANIE 2
#podpunkt a
epsilon1, gamma1, h1 = 1.25, 0.5, 0.1
epsilon2, gamma2, h2 = 0.5, 0.2, 0.2
h = 0.001
t = np.arange(0,50,h)
N1, N2 = np.zeros(t.shape[0]), np.zeros(t.shape[0])
N1[0], N2[0] = 3, 4

for i in range(1, N1.shape[0]):
    N1[i] = N1[i-1] + h*(epsilon1 - gamma1*(h1*N1[i-1] + h2*N2[i-1]))*N1[i-1]
    N2[i] = N2[i-1] + h*(epsilon2 - gamma2*(h1*N1[i-1] + h2*N2[i-1]))*N2[i-1]

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.plot(t, N1, color='r', label='Populacja N1')
axes.plot(t, N2, color='b', label='Populacja N2')
plt.title('Zadanie 2, podpunkt a')
axes.set_xlabel('Czas')
axes.set_ylabel('Liczba osobników w populacji')
plt.legend()
axes.grid(True)
plt.show()

''' 
Na wykresie możemy zauważyć, że obie populacje rosną, ale tempo wzrostu 
populacji N1 jest wyraźnie szybsze niż tempo wzrostu populacji N2. To sugeruje, 
że czynniki wpływające na wzrost populacji, takie jak epsilon, gamma oraz h1 i h2, 
sprzyjają populacji N1, co skutkuje szybszym rozwojem tej populacji 
w porównaniu do N2, pomimo tego, że warunek początkowy populacji N2 jest większy
niż populacji N1 (4>3).
'''

#podpunkt b
epsilon1, gamma1, h1 = 5, 4, 1
epsilon2, gamma2, h2 = 5, 8, 4
h = 0.001
t = np.arange(0,50,h)
N1, N2 = np.zeros(t.shape[0]), np.zeros(t.shape[0])
N1[0], N2[0] = 3, 4

for i in range(1, N1.shape[0]):
    N1[i] = N1[i-1] + h*(epsilon1 - gamma1*(h1*N1[i-1] + h2*N2[i-1]))*N1[i-1]
    N2[i] = N2[i-1] + h*(epsilon2 - gamma2*(h1*N1[i-1] + h2*N2[i-1]))*N2[i-1]

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.plot(t, N1, color='r', label='Populacja N1')
axes.plot(t, N2, color='b', label='Populacja N2')
plt.title('Zadanie 2, podpunkt b')
axes.set_xlabel('Czas')
axes.set_ylabel('Liczba osobników w populacji')
plt.legend()
axes.grid(True)
plt.show()

''' 
Na wykresie możemy zauważyć, że populacja N2 maleje do 0, podczas gdy populacja
N1 na początku maleje, następnie rośnie i się wyrównuje. Oznacza to, że wartości
gamma i h sprzyjały populacji N1, pomimo takiej samej wartości epsilon w obu 
populacjach. Na początku populacje ze sobą współzawodniczyły, jednak populacja N1
wygrała z populacja N2.
'''

#Dane do podpunktów c, d, e
t = np.arange(0,10,h)
epsilon1, gamma1, h1 = 0.8, 1, 0.3
epsilon2, gamma2, h2 = 0.4, 0.5, 0.4
N1c, N2c = np.zeros(t.shape[0]), np.zeros(t.shape[0])
N1c[0], N2c[0] = 4, 8
N1d, N2d = np.zeros(t.shape[0]), np.zeros(t.shape[0])
N1d[0], N2d[0] = 8, 8
N1e, N2e = np.zeros(t.shape[0]), np.zeros(t.shape[0])
N1e[0], N2e[0] = 12, 8

for i in range(1, t.shape[0]):
    #podpunkt c
    N1c[i] = N1c[i-1] + h*(epsilon1 - gamma1*(h1*N1c[i-1] + h2*N2c[i-1]))*N1c[i-1]
    N2c[i] = N2c[i-1] + h*(epsilon2 - gamma2*(h1*N1c[i-1] + h2*N2c[i-1]))*N2c[i-1]
    #podpunkt d
    N1d[i] = N1d[i-1] + h*(epsilon1 - gamma1*(h1*N1d[i-1] + h2*N2d[i-1]))*N1d[i-1]
    N2d[i] = N2d[i-1] + h*(epsilon2 - gamma2*(h1*N1d[i-1] + h2*N2d[i-1]))*N2d[i-1]
    #podpunkt e
    N1e[i] = N1e[i-1] + h*(epsilon1 - gamma1*(h1*N1e[i-1] + h2*N2e[i-1]))*N1e[i-1]
    N2e[i] = N2e[i-1] + h*(epsilon2 - gamma2*(h1*N1e[i-1] + h2*N2e[i-1]))*N2e[i-1]

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.plot(N1c, N2c, color = 'r', label='c) (N1, N2) = (4, 8)')
axes.plot(N1d, N2d, color = 'b', label='d) (N1, N2) = (8, 8)')
axes.plot(N1e, N2e, color = 'g', label='e) (N1, N2) = (12, 8)')
axes.scatter([4, 8, 12], [8, 8, 8], color='black', label='Warunki początkowe')
plt.title('Portret fazowy')
axes.set_xlabel('Populacja N1')
axes.set_ylabel('Populacja N2')
axes.grid(True)
plt.legend()
plt.show()

'''
Na podstawie otrzymanego portretu fazowego możemy zauważyć, że populacje N2 
maleją szybciej od populacji N1, przy czym im większa wartość warunków 
początkowych, tym wolniej maleje populacja.
'''