import numpy as np
def smooth(y, w, sigma, kern):
	
    if (kern = 'box'):
		box = np.ones(w) / w
		ys = np.convolve(y, box, mode = 'same')
	
    if (kern = 'gauss'):
		x = (np.arange(w + 1)/w - 0.5) * sigma
		box = np.exp(-x ** 2 / sigma ** 2)
		ys = np.convolve(y, box, mode = 'same')
	
    return ys
