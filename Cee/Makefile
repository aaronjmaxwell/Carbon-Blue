CC = clang
CFLAGS = -O0 -lm
linfit: linfit.c
    $(CC) $(CFLAGS) linfit.c -o linfit.o
mean: mean.c
	$(CC) $(CFLAGS) mean.c -o mean.o
sum: sum.c
	$(CC) $(CFLAGS) -c sum.c
clean:
	rm -f *.o
