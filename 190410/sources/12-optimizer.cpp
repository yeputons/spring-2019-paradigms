#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#pragma GCC optimize("-O2")
#pragma optimize("t", on)

int data;
void* worker(void*) {
    for (;;) {
        data++;
    }
}

int main() {
    pthread_t id;
    assert(pthread_create(&id, NULL, worker, NULL) == 0);
    while (data < 100);
    printf("Done\n");
    assert(pthread_join(id, NULL) == 0);
    return 0;
}
