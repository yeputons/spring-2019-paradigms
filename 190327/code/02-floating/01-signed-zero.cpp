#include <stdio.h>

int main() {
    printf("%.18lf\n", (float)1.0 / (float)0.0);
    printf("%.18lf\n", (float)-1.0 / (float)0.0);
    printf("%.18lf\n", (float)1.0 / (float)-0.0);
    printf("%.18lf\n", (float)-1.0 / (float)-0.0);
    return 0;
}
