from sympy import Symbol, Derivative, lambdify

#definiuje funkcje obliczajaca wartosc funkcji w punkcie 
def funkcja(x):
	return x**3+1

def pochodna_funkcji(wart):
	#okreslam po jakiej zmiennej ma byc liczona pochodna
	x=Symbol('x')	

	#licze pochodna
	funkcja=x**3+1
	pochodna= funkcja.diff(x)
	
	#i teraz wartosc pochodnej w miejscu wart
	wart_pochodna=lambdify(x,pochodna)
	return wart_pochodna(wart)


def ne_raph (x0,epsilon,m):
	
	i=1
	while (i<m):
		x1=(x0-(funkcja(x0)/pochodna_funkcji(x0)))
		
		if (abs(x0-x1)<epsilon):
		
			print 'Miejscem zerowym funkcji jest:','%.4f'%x1
			print 'Liczba iteracji:',i
			
			break
	
		else:
		
			x0=x1
			i+=1.
						

			
x0=50.	#punkt poczatkowy
epsilon=0.00001	#dokladnosc 
m=100	#naksymalna liczba iteracji

ne_raph(x0,epsilon,m)	
	

