import numpy as np
import math

def funkcja(x):
    return x**3 - 1

def hybryda(a, b, epislon, M, delta):
	if b < a:	
		a,b = b,a
	
	x_old=b
	x_older=a
	f_old=funkcja(x_old)
	f_older=funkcja(x_older)
	f_a=f_older
	f_b=f_old
	i=0
	bisekcja=0
	sieczne=0
   
	for i in range (M):
		c=x_old-f_old*(x_old-x_older)/(f_old-f_older)
	
		if c < a or c > b:
		
			bisekcja+=1
			c=a+0.5(b-a)
			f_c=funkcja(c)
	    
			if np.sign(f_a) != np.sign(f_c):
				b=c
				f_b=f_c
				x_new=c
				x_old=a
				f_old=f_a
	    
			else:
				a=c
				f_a=f_c
				x_new=c
				x_old=b
				f_old=f_b

		else:
			sieczne+=1
			f_c=funkcja(c)
	
			if np.sign(f_a) != np.sign(f_c):
				b=c
				f_b=f_c
	    
			else:
				a=c
				f_a=f_c
	
			x_new=c
	
		x_older=x_old
		x_old=x_new
		f_old=f_c
	
		if abs(x_old - x_older) < epsilon or f_c < delta:
			print"Bisekcja : ", bisekcja,"Sieczne : ", sieczne
    
	return c
a=-100
b=100
epsilon=0.0001
delta=0.0001
M=100

hybryda(a,b,epsilon,M,delta)
