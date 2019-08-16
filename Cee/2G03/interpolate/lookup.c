int lookup(float x, float *px){
	int i,j;
	for(j=0;j<12;j++){
		if (px[j]<x && px[j+1]>x){
			i=j;
		}
	}
	return i;
}	
