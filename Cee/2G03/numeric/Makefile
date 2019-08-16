CC = gcc
CFLAGS = -O0 -lm
out: main.o func.o inter.o differ.o
	$(CC) $(CFLAGS) main.o func.o inter.o differ.o -o out.o
main.o: main.c numeric.h
	$(CC) $(CFLAGS) main.c -c
inter.o: inter.c func.h
	$(CC) $(CFLAGS) inter.c -c
differ.o: differ.c func.h
	$(CC) $(CFLAGS) differ.c -c
func.o: func.c
	$(CC) $(CFLAGS) func.c -c
clean:
	rm -f *.o
