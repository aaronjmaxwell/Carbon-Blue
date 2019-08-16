#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "func.h"
float inter(float a, float b, int n){
	FILE *fl;
	int i;
	float x,y,dy,Dx,Iy,s,e,o;
	s=0.;
	fl=fopen("int.dat","w");
	Dx=(b-a)/n;
	for(i=0;i<n;i++){
		x=a+Dx*(i+0.5);
		Iy=Iy+fx(x)*Dx;
		e=Iy-ifx(x+Dx/2.);
		o=Dx*Dx/8.*fxp2(x);
		s=s+e*e;
		fprintf(fl,"%7.4f %7.4f %8.6f %8.6f\n",x,Iy,e,o);
	}
	fclose(fl);
	return s;
}
