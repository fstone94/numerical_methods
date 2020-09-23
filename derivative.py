from sympy import *
from sympy import Symbol, Derivative, lambdify
import numpy as np
import matplotlib.pyplot as plt

#definiuje funkcje obliczajaca wartosc funkcji w punkcie 
def funkcja(x):
	return sin(x)

def pochodna_funkcji(wart):
	#okreslam po jakiej zmiennej ma byc liczona pochodna
	x = Symbol('x')	

	#licze pochodna
	pochodna = diff(sin(x)+x**2,x)
	
	#i teraz wartosc pochodnej w miejscu wart
	wart_pochodna = lambdify(x,pochodna)
	return wart_pochodna(wart)
	
def przyblizenie1(x,h):
	
	przyblizenie=(1/h)*(funkcja(x+h)-funkcja(x))
	
	return przyblizenie
	
h=0.1
x=[]
i=0.0
y=0.01
while (i<=2.01):
	
	x.append(i)
	i+=y
	
x=np.asarray(x)

pochodna=[]
iksy=[]
analitycznie=[]
for i in range (len(x)):
	
	pochodna.append(przyblizenie1(x[i],h))
	iksy.append(x[i])
	analitycznie.append(pochodna_funkcji(x[i]))

pochodna=np.asarray(pochodna)
iksy=np.asarray(iksy)
analitycznie=np.asarray(analitycznie)

plt.title('Przyblizenie 1')
plt.xlabel('y')
plt.ylabel('x')

plt.plot(iksy,pochodna,label='z przyblizenia')
plt.plot(iksy,analitycznie,label='analitycznie')
plt.legend()
plt.show()
	


