#include <stdio.h>
#include <math.h>
#include "const.h"
float sine(float x){
	float sx,a;
	int cs,sgn;
	if(x > 2*PI){/* shifts numbers greater than 2PI*/
		a=x/(2*PI);
		x=x-floorf(a)*2*PI;
		printf("converting x to %f\n",x);
	}
	cs=floorf(2*x/PI);
	switch(cs){
	case 0:
		a=0.;
		sgn=+1;
		break;
	case 1:
		a=PI;
		x=a-x;
		sgn=+1;
		break;
	case 2:
		a=PI;
		x=x-a;
		sgn=-1;
		break;
	case 3:
		a=2*PI;
		x=a-x;
		sgn=-1;
		break;
	}
	sx=sgn*(x-x*x*x/6.+x*x*x*x*x/120.);
	return sx;
}
