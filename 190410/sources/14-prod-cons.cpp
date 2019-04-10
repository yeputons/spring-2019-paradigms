#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

pthread_mutex_t m;
pthread_cond_t cond;

char str[100];
bool str_available;
void* producer(void*) {
    while (true) {
        fgets(str, sizeof str, stdin);
        pthread_mutex_lock(&m);
        str_available = true;
        pthread_cond_signal(&cond);
        pthread_mutex_unlock(&m);
    }
}

void* consumer(void*) {
    while (true) {
        pthread_mutex_lock(&m);
        while (!str_available) {
            pthread_cond_wait(&cond, &m);
        }
        char str_snapshot[sizeof str];
        strncpy(str_snapshot, str, sizeof str_snapshot);
        str_available = false;
        pthread_mutex_unlock(&m);

        printf("Got string: %s", str_snapshot);
        // Ждём две секунды (на Windows usleep работает не со всеми аргументами).
        for (int i = 0; i < 4; i++) {
          usleep(500000);
        }
        printf("Repeating: %s", str_snapshot);
    }
}

int main() {
    pthread_mutex_init(&m, NULL);
    pthread_cond_init(&cond, NULL);

    pthread_t id1, id2;
    assert(pthread_create(&id1, NULL, producer, NULL) == 0);
    assert(pthread_create(&id2, NULL, consumer, NULL) == 0);
    assert(pthread_join(id1, NULL) == 0);
    assert(pthread_join(id2, NULL) == 0);

    pthread_cond_destroy(&cond);
    pthread_mutex_destroy(&m);
    return 0;
}
