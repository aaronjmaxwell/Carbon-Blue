/*Declare variables and print them with formatting.

Variable definitions must have an associated (static) type, but can be assigned values upon
definition.  If they are not assigned a value, they are not treated as `null`, but instead inherit
the value determined by the bits allocated from the stack.  Use the -W flag at compile time to catch
variables that have not been initialized. Also note that there is no limit on the number of
characters used in variable names.
*/
#include <stdio.h>
int main(){
	int age = 10;
	int height = 72;
	printf("I am %d years old.\n", age);
	printf("I am %d inches tall.\n", height);
	return 0;
}
