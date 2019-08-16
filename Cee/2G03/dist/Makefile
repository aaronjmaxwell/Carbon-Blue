CC = gcc
CFLAGS = -O0 -lm
out: main.o dist.o
	$(CC) $(CFLAGS) main.o dist.o -o out.o
main.o: main.c dist.h
	$(CC) $(CFLAGS) main.c -c
dist.o: dist.c dist.h
	$(CC) $(CFLAGS) dist.c -c
clean:
	rm -f *.o
