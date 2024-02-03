import numpy as np 
import matplotlib.pyplot as plt 

#zadanie 1
beta, sigma, gamma = 1, 1, 0.1
s0, e0, i0, r0 = 0.99, 0.01, 0, 0 
Nmax = 1  
dt = 0.01           
t = np.arange(0, 50, dt)  
N = len(t)      

y = np.zeros([N, 4])
y[0, 0] = s0
y[0, 1] = e0
y[0, 2] = i0
y[0, 3] = r0

def SEIR(state, t):
    s = state[0]
    e = state[1]
    i = state[2]
    r = state[3]
    
    ds = -beta*s*i/Nmax
    de = beta*s*i/Nmax - sigma*e
    di = sigma*e - gamma*i
    dr = gamma*i
    
    return np.array([ds, de, di, dr])

def RK(y, t, dt, derivative):
    k1 = dt*derivative(y, t)
    k2 = dt*derivative(y + k1/2., t + 0.5*dt)
    k3 = dt*derivative(y + k2/2., t + 0.5*dt)
    k4 = dt*derivative(y + k3, t + dt)
    y_next = y + 1/6.*(k1 + 2*k2 + 2*k3 + k4)
    return y_next

for i in range(N-1):
    y[i+1] = RK(y[i], t[i], dt, SEIR)

plt.figure()
plt.plot(t, y[:, 0], color = 'g', label='[S] - podatni na zachorowanie')
plt.plot(t, y[:, 1], color = 'y', label='[E] - wystawieni na działanie wirusa')
plt.plot(t, y[:, 2], color = 'r', label='[I] - chorzy, zarażający')
plt.plot(t, y[:, 3], color = 'b', label='[R] - przechorowani, zmarli')
plt.xlabel('Czas')
plt.ylabel('Liczebność')
plt.title('Zadanie 1: Model SEIR (β = 1)')
plt.legend()
plt.grid(True)
plt.show()


#zadanie 2
beta = 0.5

for i in range(N-1):
    y[i+1] = RK(y[i], t[i], dt, SEIR)

plt.figure()
plt.plot(t, y[:, 0], color = 'g', label='[S] - podatni na zachorowanie')
plt.plot(t, y[:, 1], color = 'y', label='[E] - wystawieni na działanie wirusa')
plt.plot(t, y[:, 2], color = 'r', label='[I] - chorzy, zarażający')
plt.plot(t, y[:, 3], color = 'b', label='[R] - przechorowani, zmarli')
plt.xlabel('Czas')
plt.ylabel('Liczebność')
plt.title('Zadanie 2: Model SEIR (β = 0.5)')
plt.legend()
plt.grid(True)
plt.show()

'''
Współczynnik β to współczynnik zarażeń (kontaktów). Jeśli zmniejszymy go o połowę,
spowoduje to, że mniej osób zostanie wystawionych na działanie wirusa i mniej osób 
zachoruje, w związku z czym funkcje e(t) i i(t) osiągną mniejsze wartości.
'''

#zadanie 3
beta, gamma = 2, 0.1
R0 = beta/gamma*s0

for i in range(N-1):
    y[i+1] = RK(y[i], t[i], dt, SEIR)

plt.figure()
plt.plot(t, y[:, 0], color = 'g', label='[S] - podatni na zachorowanie')
plt.plot(t, y[:, 1], color = 'y', label='[E] - wystawieni na działanie wirusa')
plt.plot(t, y[:, 2], color = 'r', label='[I] - chorzy, zarażający')
plt.plot(t, y[:, 3], color = 'b', label='[R] - przechorowani, zmarli')
plt.xlabel('Czas')
plt.ylabel('Liczebność')
plt.title(f'Zadanie 3: Model SEIR (R0 = {R0} > 1)')
plt.legend()
plt.grid(True)
plt.show()
'''
Parametr reprodukcji R0 jest dużo większy od 1, co oznacza, że jedna osoba zaraża 
wiele osób, co prowadzi do rozwoju epidemii.
'''

beta, gamma = 0.1, 1
R0 = beta/gamma*s0

for i in range(N-1):
    y[i+1] = RK(y[i], t[i], dt, SEIR)

plt.figure()
plt.plot(t, y[:, 0], color = 'g', label='[S] - podatni na zachorowanie')
plt.plot(t, y[:, 1], color = 'y', label='[E] - wystawieni na działanie wirusa')
plt.plot(t, y[:, 2], color = 'r', label='[I] - chorzy, zarażający')
plt.plot(t, y[:, 3], color = 'b', label='[R] - przechorowani, zmarli')
plt.xlabel('Czas')
plt.ylabel('Liczebność')
plt.title(f'Zadanie 3: Model SEIR (R0 = {R0} < 1)')
plt.legend()
plt.grid(True)
plt.show()

'''
Parametr reprodukcji R0 jest mniejszy od 1, co oznacza, że jedna osoba zaraża średnio
mniej niż jedną osobę, przez co epidemia wygasa. 
'''
