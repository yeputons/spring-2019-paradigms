#include <assert.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
     assert(argc == 2);
     float x;
     assert(sscanf(argv[1], "%f", &x) == 1);

     int* xi = (int*)&x;
     for (int i = 31; i >= 0; i--) {
         printf("%d", (*xi >> i) & 1);
         if (i % 4 == 0) {
             printf(" ");
         }
     }
     printf("\n");
     return 0;
}
