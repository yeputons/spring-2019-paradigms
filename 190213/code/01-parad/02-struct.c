#include <assert.h>
int main(int argc, char* argv[]) {
    int val = 0, flag = 0;
    for (int i = 1; i < argc; i++) {
      if (!strcmp(argv[i], "--flag")) {
        flag = 1;
      } else if (!strcmp(argv[i], "--val")) {
        i++;
        assert(i < argc);
        val = atoi(argv[i]);
      }
    }
    printf("val=%d, flag=%d\n", val, flag);
    return 0;
}
