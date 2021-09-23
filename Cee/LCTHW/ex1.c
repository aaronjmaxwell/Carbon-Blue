/* Write a simple string to the terminal.

The basic structure of a C program is given here. External definitions
are included as header files - such as input/output - and the main
namespace is what is executed first. Function definitions in C require
a type declaration that matches the return type.
*/
#include <stdio.h>

int main(int argc, char *argv[]){
    /* The default main program.

    Main is a protected namespace in C, and is the point of entry of
    every script. This function takes two inputs: the number of arguments,
    and the arguments themselves as a character buffer. It then uses the
    stdio.puts to 'put a string to the screen'.

	Arguments
    ---------
    argc: the number of arguments to main
    argv: the arguments themselves
    */

	puts("Hello world.");
	return 0;
}
