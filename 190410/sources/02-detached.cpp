#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int data = 1234;
void* worker(void*) {
    printf("Hello from thread! data=%d\n", data);
    data += 10;
    return NULL;
}

int main() {
    pthread_t id;
    assert(pthread_create(&id, NULL, worker, NULL) == 0);
    assert(pthread_detach(id) == 0);
    // assert(pthread_join(id, NULL) == 0);
    printf("data is %d\n", data);
    pthread_exit(NULL);
    return 0;
}
