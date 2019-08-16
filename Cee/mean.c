#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
	int i;
	float *g,mu,std;
	mu=0; std=0;
	g=(float *) calloc(5,sizeof(float));
	for(i=0;i<5;i++){
		scanf("%f",&g[i]);
		mu=mu+g[i];
	}
	mu=mu/5.;
	for(i=0;i<5;i++){
		std=std+(g[i]-mu)*(g[i]-mu);
	}
	printf("mu=%4.2f, stdev=%4.2f\n",mu,sqrt(std/4));
}
