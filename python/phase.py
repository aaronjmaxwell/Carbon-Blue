import math
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
gs = gridspec.GridSpec(4,4)
gs1 = gridspec.GridSpec(4,4)
gs2 = gridspec.GridSpec(4,4)
gs1.update(left = 0.1,right = 0.8)
gs2.update(left = 0.2,right = 0.9)
ogloc = '/1/home/maxwelaj/work/Papers/THESIS/SupplementaryMaterial/'
fl = np.genfromtxt(ogloc + 'phase.dat',usecols = [0,1,2],dtype = [('S14'),('f4'),('f8')],names = ['fl','t','m'])
a = 0.7
e = 0.3
L = a*(1 - e)*np.sqrt((1 + e)/(1 - e)/a)
phi = np.arange(100)/100.*2*3.14159
r = L*L/(1 + e*np.cos(phi))
v = np.sqrt(1 + 2*e*np.cos(phi) + e**2)/L
E = 0.5*v**2. - 1/r
for i in range(0,918):
#for i in range(0,1):
	dat = np.genfromtxt(ogloc + fl['fl'][i],usecols = [0,1,2,3],dtype = [('f4'),('f4'),('f4'),('f4')],names = ['x','y','vx','vy'])
##### ORBITS ##################################################################
#	ax = plt.subplot(gs[1:4,:])
#	plt.scatter(r*np.cos(phi),r*np.sin(phi),s = 0.25,color = 'black')
#	plt.scatter(dat['x'],dat['y'],s = 0.75,color = 'red')
#	plt.xlim(-2,2)
#	plt.ylim(-2,2)
#	plt.xlabel('x')
#	plt.ylabel('y')
#	plt.text(-1.8,1.8,'t  =  ' + '{:5.3f}'.format(fl['t'][i]))
##### PHASES ##################################################################
	rr = np.sqrt(dat['x']**2 + dat['y']**2)
	vv = np.sqrt(dat['vx']**2 + dat['vy']**2)
	EE = 0.5*vv**2.-1/rr
	LL = dat['x']*dat['vy']-dat['y']*dat['vx']
	ee = np.sqrt(1 + 2*EE*LL**2.)
	pphi = np.arctan(y/x)
	ind = np.where(dat['y'] < 0)
	pphi[ind] = 2*math.pi-pphi[ind]
	ax = plt.subplot(gs1[1:4,0:2])
	plt.scatter(r,v,s = 0.25,color = 'black')
	plt.scatter(rr,vv,s = 0.75,color = 'red')
	plt.xlabel('r')
	plt.ylabel('v')
	plt.xlim(0.4,1.0)
	plt.ylim(0.7,1.7)
	ax = plt.subplot(gs2[1:4,2:4])
	plt.scatter(phi,E,s = 0.25,color = 'black')
	plt.scatter(pphi,EE,s = 0.75,color = 'red')
	plt.xlabel('$\phi$')
	plt.ylabel('E')
	plt.xlim(-0.9,2.1*math.pi)
	plt.ylim(-0.75,-0.695)
###############################################################################
	ax = plt.subplot(gs[0,:])
	plt.scatter(fl['t'],fl['m'],marker = ',',s = 0.1)
	plt.scatter(fl['t'][i],fl['m'][i])
	plt.xlim(-0.2,18.5)
	plt.xlabel(' ')
	plt.ylim(0.95,1.01)
	plt.yticks(0.95 + np.arange(7)/100.,('0.95',' ',' ',' ',' ','1.0',' '))
	plt.ylabel('m')
	j = i + 1
	if (j < 10):
		imfl = 'v00' + str(j) + '.png'
	elif(j > = 10 and j < 100):
		imfl = 'v0' + str(j) + '.png'
#	elif(j > = 100 and j < 1000):
#		imfl = 'v0' + str(j) + '.png'
	else:
		imfl = 'v' + str(j) + '.png'
	plt.savefig(imfl)
	plt.clf()
