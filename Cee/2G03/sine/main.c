#include <stdio.h>
#include <math.h>
#include "sine.h"
#include "const.h"
int main(){
	float x;
	printf("Input a real number\n");
	scanf("%f",&x);
	printf("sin(%f)=%f\n",x,sin(x));
	printf("sine(%f)=%f\n",x,sine(x));
	printf("diff=%f\n",fabs(sine(x)-sin(x)));
}
