#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "func.h"
float differ(float a, float b, int n){
	FILE *fl;
	int i;
	float x,y,dy,Dx,Dy,s,e,o;
	s=0.;
	fl=fopen("der.dat","w");
	Dx=(b-a)/n;
	for(i=0;i<n;i++){
		x=a+Dx*i;
		y=fx(x);
		Dy=fx(x+Dx);
		dy=(Dy-y)/Dx;
		e=dy-fxp(x);
		o=0.5*Dx*fxp2(x);
		s=s+e*e;
		fprintf(fl,"%7.4f %7.4f %8.6f %8.6f\n",x,dy,e,o);
	}
	fclose(fl);
	return s;
}
