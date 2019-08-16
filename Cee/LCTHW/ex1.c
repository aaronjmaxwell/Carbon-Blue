/*Write a simple string to the terminal.

The basic structure of a C program is given here.  External definitions are included as header
files - such as input/output - and the main namespace is what is executed first.  It takes two
inputs: the number of arguments as an `int`, and the arguments themselves as a `char` buffer.
Function definitions in C require a type declaration that matches the return type.
*/
#include <stdio.h>
int main(int argc, char *argv[]){
	// Use puts to put a string to the screen.
	puts("Hello world.");
	return 0;
}
