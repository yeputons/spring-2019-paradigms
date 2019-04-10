#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

pthread_mutex_t m;
void writeln(const char* s) {
    pthread_mutex_lock(&m);
    for (int i = 0; s[i]; i++) {
        putc(s[i], stdout);
    }
    putc('\n', stdout);
    pthread_mutex_unlock(&m);
}

void* worker(void*) {
    for (;;) {
        writeln("Hello from the second thread");
    }
}

int main() {
    pthread_t id;
    pthread_mutex_init(&m, NULL);
    assert(pthread_create(&id, NULL, worker, NULL) == 0);
    for (;;) {
        writeln("Hello from the main thread");
    }
}
