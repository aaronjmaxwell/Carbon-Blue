#include <stdio.h>
#include <math.h>
#include "interp.h"
int main(){
	FILE *pfl;
	float px[11],py[11];
	float x,y;
	int i;
	pfl=fopen("data.txt","r");
   for(i=0;i<12;i++){
		fscanf(pfl,"%f%f",&px[i],&py[i]);
	}
	printf("please enter the value of the interpolation point\n");
	scanf("%f",&x);
	i=lookup(x,px);
	y=interpolate(x,px,py,i);
//	printf("A linear interpolation of p.x between %7.5f and %7.5f yields %7.5f\n",px[i],px[i+1],y);
	printf("%5.2f & %10.4f & %10.4f & %i\n",x,0.75*x*x+5,y,i);
}
