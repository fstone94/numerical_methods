from sympy import * 
import numpy as np

def funkcja(x):
	return sin(x)

def trapezy(n,a,b):
	
	h=((b-a)/n)
	suma=0
	for i in range (n):
		suma=suma+funkcja(a+i*h)
		
	calka=(0.5*h)*(funkcja(a)+(2*suma)+funkcja(b))
	
	return calka

n=np.array([10,20,100])	
for i in range (len(n)):
	rozwiazanie=trapezy(n[i],0,float(pi))
	print ''
	print 'Uzywajac metody trapezow, dla n =',n[i]
	print 'Wartosc calki to:',rozwiazanie
	

def simpson(n,a,b):
	
	h=((b-a)/(2*n))
	x=[]
	for i in range (0,(2*n)+1):
		x.append(a+(i*h))
		
	x=np.asarray(x)
	
	suma1=0
	suma2=0
	
	for i in range (n+1):
		suma1=suma1+funkcja(x[(2*i)-1])
	for i in range (n):
		suma2=suma2+funkcja(x[2*i])
		
	calka=(h/3)*(funkcja(a)+(4*suma1)+(2*suma2)+funkcja(x[2*n]))
	
	return calka
	
for i in range (len(n)):
	rozwiazanie2=simpson(n[i],0,float(pi))
	print ''
	print 'uzywajac metody Simpsona, dla n =',n[i]
	print 'Wartosc calki to:',rozwiazanie2
