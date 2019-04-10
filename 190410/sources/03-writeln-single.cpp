#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void writeln(const char* s) {
    for (int i = 0; s[i]; i++) {
        putc(s[i], stdout);
    }
    putc('\n', stdout);
}

int main() {
    for (;;) {
        writeln("Hello from the main thread");
    }
}
