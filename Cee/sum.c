#include <stdio.h>
#include <math.h>
float fsum(float *arr, int arrlen){
	int i;
	float sum = 0.;
	for (i = 0; i < arrlen; i++){
		sum = sum + arr[i];
	}
	return sum;
}

int isum(int *arr, int arrlen){
	int i, sum = 0;
	for (i = 0; i < arrlen; i++){
		sum = sum + arr[i];
	}
   return sum;
}
