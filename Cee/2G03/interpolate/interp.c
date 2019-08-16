#include "interp.h"
float interpolate(float x, float *px, float *py, int i){
	float y;
	y=(py[i+1]-py[i])/(px[i+1]-px[i])*x+px[i];
	return y;
}	
