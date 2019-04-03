#include <vector>

using namespace std;

int main() {
    vector<int> x = {1, 2, 3};
    for (size_t i = x.size() - 1; i >= 0; i--) {
        printf("%d\n", x[i]);
    }
    int y[] = {1, 2, 3};
    y[i] == *(&y + i);
}
