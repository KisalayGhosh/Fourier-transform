import numpy as np 
from scipy.signal import square
from matplotlib import pyplot as plt 

#Define the square wave to be approximated by specifying frequency f and the mean value
f = 5 #Frequency
T = 1/f
omega = (2*np.pi)/T

for series in range (1, 10, 2):

	t = np.linspace(0, 1, 5000, endpoint=False)
	fourier_terms = series

	def bn(n):
		if(n%2 != 0):
			return 4/(np.pi*n)
		else:
			return 0

	mean = 1
	sq_wave = mean + square(omega*t)

	#a0 = (1/T)*(integral of f(t)dt from 0 to T)
	a0 = mean #Integral of f(t)dt from 0 to T is value of (mean*2) from 0 to T/2

	fourier_y = []

	for tn in t:
		f_series = a0 #Sum of terms in f at each t
		for j in range(1,fourier_terms): #Number of terms in the Fourier series
			f_series += bn(j)*np.sin(omega*j*tn)
		fourier_y.append(f_series)


	plt.plot(t, sq_wave, color='blue')
	plt.ylim(-1,3)

	plt.plot(t, fourier_y, color='red')

	#plt.show()

	plt.savefig('SquareWave/fourier_sq_%d.png'%series)

	plt.clf()


