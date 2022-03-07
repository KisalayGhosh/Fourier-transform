# Fourier Transforms



## Overview
Fourier Transforms are ubiquitous in mathematical areas which require the decomposition of a function into its constituent frequencies. 

This work attempts to capture the beautiful piece of mathematics that governs Fourier Transforms and is inspired by 3Blue1Brown's [video](https://www.youtube.com/watch?v=spUNpyF58BY). As explained in the video, wrapping input signals around a circle allows for varying patterns and when the centre of mass shifts from the origin (centre of the image), we see a pure frequency.

Some of the key features of this work include:

* Wrapping input signals in a circular fashion to capture the patterns that emerge for varying wrapping frequencies.
* Visualizing the aligned patterns that emerge when the signal frequency matches the wrapping frequency, thus indicating the pure frequencies of the signal.
* Visualization of the square wave and sawtooth wave approximated by their Fourier series.

All images were generated using Python, by using packages like Matplotlib, NumPy and SciPy.






## Code Usage

### Square and Sawtooth Wave Animations

Modify the following lines in *sawtooth_animation.py* and *square_wave_animation.py* to generate your own animations:

```
f = n

for series in range (min_terms, max_terms, step):

```
Here, *f* denotes the frequency of the wave, assigned using *n* and *series* denotes the number of fourier terms used, with variation from *min_terms* to *max_terms* in increments of *step*. 


### Signal Wrapping


Vary the following parameters in *signal_wrap.py* to generate your own wrappings for signals:

```

f_wave = n

signal = np.cos(k1*omega*t)+np.sin(k2*omega*t)

f_list = np.arange(min_freq, max_freq, step_size)

```
Here, *f_wave* denotes the frequency of the wave, *signal* denotes the actual signal to be wrapped and *(min_freq, max_freq, step_size)* denote the minimum and maximum frequency values to be used for the animation, with increments of *step_size*. 



