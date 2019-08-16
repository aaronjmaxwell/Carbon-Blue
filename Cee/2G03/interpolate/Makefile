CC = gcc
CFLAGS = -O0 -lm
out: main.o interp.o lookup.o
	$(CC) $(CFLAGS) main.o interp.o lookup.o -o out.o
main.o: main.c interp.h
	$(CC) $(CFLAGS) main.c -c
lookup.o: lookup.c interp.h
	$(CC) $(CFLAGS) lookup.c -c
interp.o: interp.c interp.h
	$(CC) $(CFLAGS) interp.c -c
clean:
	rm -f *.o
