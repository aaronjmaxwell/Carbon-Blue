#include <stdio.h>
#include <math.h>
#include "dist.h"
float dist (struct point i, struct point j){
	float d;
	d=sqrt(powf(j.x-i.x,2)+powf(j.y-i.y,2)+powf(j.z-i.z,2));
	return d;
}
