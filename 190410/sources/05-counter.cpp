#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

const int N = 500000000;
const int M = 1000;

int data;
void* worker(void*) {
    for (int i = 0; i < N; i++) {
        data++;
    }
    return NULL;
}

int main() {
    pthread_t id;
    assert(pthread_create(&id, NULL, worker, NULL) == 0);
    for (int i = 0; i < M; i++) {
        printf("data is %d (in progress)\n", data);
    }
    assert(pthread_join(id, NULL) == 0);
    printf("data is %d\n", data);
    return 0;
}
