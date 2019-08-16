#include <stdio.h>
#include <math.h>
#include "dist.h"
int main(){
	struct point p[3];
	float d;
	p[0].x=0.; 	p[0].y=0.; 	p[0].z=0.;
	printf("please input the first set of coords\n");
	scanf("%f %f %f",&p[1].x,&p[1].y,&p[1].z);
	printf("please input the second set of coords\n");
	scanf("%f %f %f",&p[2].x,&p[2].y,&p[2].z);
	d=dist(p[1],p[0]);
	printf("||d_1||=%7.5f\n",d);
	d=dist(p[2],p[0]);
	printf("||d_2||=%7.5f\n",d);
	d=dist(p[1],p[2]);
	printf("||d_1-d_2||=%7.5f\n",d);
}
