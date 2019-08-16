/* Takes a single string and uses char math to reset from upper to lowercase */
#include <stdio.h>
int main(int argc, char *argv[]){
   int i;
   char l;
   if (argc != 2) {
      printf("Only one argument permitted!\n");
      return 1;
   }
   for (i = 0; argv[1][i] != '\0'; i++) {
      l = argv[1][i];
      if (l >= 65 && l <= 90) {
         l += 32;
      }
      argv[1][i] = l;
   }
   printf("%s\n",argv[1]);
   return 0;
}
