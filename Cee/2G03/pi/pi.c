#include <stdio.h>
int main()
{/* Estimating Pi*/
	int n;
	float t, eps, s, pi;
	pi=3.141592653589793238462633383279502884197169399375105820974944e0;
	eps=0;
	do{
		printf("Please enter the minimum term (>0 please)\n");
		scanf("%f",&eps);
	} while (eps <= 0);
	n=1;
	t=1;
	s=t;
	for(;;){
		n++; /*increment by 1*/
		t=t*(n-1.)/(2*n-1);
		s=s+t;
		if(t <= eps) break;
	}
	s=2*s;
	printf("Program yields %25.20f\n",s);
	printf("This differs from true by %8.4e\n",pi-s);
	printf("The smallest term included was %8.4e\n",t);
	printf("The number of terms summed was %i\n",n);
}
