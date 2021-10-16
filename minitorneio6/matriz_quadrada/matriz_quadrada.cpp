#include <bits/stdc++.h>

using namespace std;

int matriz_quadrada() {

    int n = -1;
    int matriz[109][109];

    while (true) {
        cin >> n;

        if (n == 0) break;

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (i == j) matriz[i][j] = 1;
                else if (j > i) matriz[i][j] = j - i + 1;
                else matriz[i][j] = i - j + 1;
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (j == 1) printf("%3d", matriz[i][j]);
                else printf(" %3d", matriz[i][j]);
            }
            printf("\n");
        }
        printf("\n");

    }

    return 0;
}