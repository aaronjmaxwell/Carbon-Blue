CC = gcc
CFLAGS = -O0 -lm
out: main.o sine.o
	$(CC) $(CFLAGS) main.o sine.o -o out.o
main.o: main.c sine.h
	$(CC) $(CFLAGS) main.c -c
sine.o: sine.c sine.h
	$(CC) $(CFLAGS) sine.c -c
clean:
	rm -f *.o
