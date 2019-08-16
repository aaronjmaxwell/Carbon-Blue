#include <stdio.h>
#include <math.h>
float fx (float x){
	float f;
	f=1.0-x+4.0*x*x-x*x*x;
	return f;
}
float fxp (float x){
	float f;
	f=-1+8*x-3*x*x;
	return f;
}
float fxp2 (float x){
   float f;
   f=8-6*x;
   return f;
}
float ifx (float x){
	float f;
	f=x-0.5*x*x+4.0/3.0*x*x*x-x*x*x*x/4.;
	return f;
}
