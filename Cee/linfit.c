#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
	FILE *fl;
	int n, i;
	float m, b, max, chi, dm, db, s, sx, sxx, sy, syy, sxy;
    float *x, *y, *e;
	sx = 0; sy = 0; sxx = 0; syy = 0; sxy = 0; chi = 0; max = 0; n = 12;
	
    x=(float *) calloc(n, sizeof(float));
	y=(float *) calloc(n, sizeof(float));
	e=(float *) calloc(n, sizeof(float));
	
    fl = fopen("data.dat","r");
	for(i = 0; i < n; i++){
		fscanf(fl, "%f%f", &x[i], &y[i]);
		sx = sx + x[i];
		sy = sy + y[i];
		sxx += x[i] * x[i];
		syy += y[i] * y[i];
		sxy += x[i] * y[i];
	}

	fclose(fl);
	
    m = (n * sxy - sx * sy) / (n * sxx - sx * sx);
	b = sy / n - m * sx / n;
	
    for(i = 0; i < n; i++){
		e[i] = (y[i] - b - m * x[i]);
		chi += e[i] * e[i];
		max = fmaxf(e[i], max);
	}

	s = (n * syy - sy * sy - m * m * (n * sxx - sx * sx)) / n / (n - 2);
	dm = n * s / (n * sxx - sx * sx);
	db = dm * sxx / n;
	
    printf("for the function y = mx + b\n");
	printf("b = %4.2f +/- %4.2f\n", b, sqrt(db));
	printf("m = %4.2f +/- %4.2f\n", m, sqrt(dm));
	printf("chi = %5.3f\n", chi);
	printf("max(e) = %4.2f\n", max);
}
