import numpy as np 
import matplotlib.pyplot as plt 

f_wave = 2 #actual frequency of the wave
omega = 2*np.pi*f_wave
t = np.arange(0, 2, 0.001)

#signal = np.sin(omega*t)
signal = np.cos(2*omega*t)+np.sin(10*omega*t)

# plt.plot(t, signal, color='b')
# plt.savefig('Signal_Wrap/cos2+sin10.png')

min_freq = 0
max_freq = 10

f_list = np.arange(min_freq, max_freq, 0.2)

for f_idx, f in enumerate(f_list):	

	r, theta = [], []
	
	for idx in range(len(t)):	
		r.append(signal[idx])
		theta.append(2*np.pi*f*t[idx])

	x, y = [], []

	for idx in range(len(t)):
		x.append(r[idx]*np.cos(theta[idx]))
		y.append(r[idx]*np.sin(theta[idx]))
		
	plt.figure(figsize=(5,5))
	plt.xlim(-2.1,2.1)
	plt.ylim(-2.1,2.1)
	plt.plot(x, y, color='r')
	plt.title("Frequency = "+str(round(f_list[f_idx],1))+" Hz", size=15)
	plt.savefig('Signal_Wrap/signal_wrap_%d.png'%f_idx)
	plt.clf()


#Convert to GIF in order
#convert -delay 30 signal_wrap_{0..49..1}.png sine.gif