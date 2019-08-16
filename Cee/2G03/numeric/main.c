#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "numeric.h"
int main(){
	int n;
	float a,b,rms;
	printf("please enter the number of terms, the lower bound, and the upper bound\n");
	scanf("%i %f %f",&n,&a,&b);
	rms=sqrt(differ(a,b,n)/n);
	printf("For %i points the RMS value of the derivative is %7.5f\n",n,rms);
	rms=sqrt(inter(a,b,n)/n);
	printf("For %i points the RMS value of the integral is %7.5f\n",n,rms);
}
