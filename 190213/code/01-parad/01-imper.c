#include <assert.h>
int main(int argc, char* argv[]) {
    int i = 0, val = 0, flag = 0;
  next_arg:
    i++;
    if (i >= argc) goto parsed;
    if (!strcmp(argv[i], "--flag")) goto process_flag;
    if (!strcmp(argv[i], "--val")) goto process_val;
    goto next_arg;
  process_flag:
    flag = 1;
    goto next_arg;
  process_val:
    i++;
    assert(i < argc);
    val = atoi(argv[i]);
    goto next_arg;

  parsed:
    printf("val=%d, flag=%d\n", val, flag);
    return 0;
}
