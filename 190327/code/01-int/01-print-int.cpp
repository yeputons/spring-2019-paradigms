#include <assert.h>
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>


void print_byte(char byte) {
    for (int bit = 7; bit >= 0; bit--) {
        printf("%d", (byte >> bit) & 1);
        if (bit == 4) printf(" ");
    }
}


int main(int argc, char* argv[]) {
    assert(argc == 2);
    int value = atoi(argv[1]);
    char *mem = reinterpret_cast<char*>(&value);

    printf("ADDR :  BYTE  0 | BYTE  1 | BYTE  2 | BYTE 3  \n");
    printf("BITS : 7654 3210|7654 3210|7654 3210|7654 3210\n");
    printf("BYTES: ");
    for (size_t i = 0; i < sizeof(value); i++) {
        if (i) {
            printf("|");
        }
        print_byte(mem[i]);
    }
    return 0;
}
