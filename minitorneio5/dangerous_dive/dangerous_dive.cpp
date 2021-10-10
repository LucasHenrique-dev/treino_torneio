#include <bits//stdc++.h>

using namespace std;

int dangerous_dive() {

    int n, r, index = 0;
    int mergulhadores[10009];

    while (cin >> n) {

        cin >> r;

        int falta[n];

        for (int i = 0; i < r; ++i) {
            cin >> mergulhadores[i];
        }

        sort(&mergulhadores[0], &mergulhadores[r]);

        if (mergulhadores[0] != 1) {
            for (int i = 1; i < mergulhadores[0]; ++i) {
                falta[index++] = i;
            }
        }

        for (int i = 1; i < r; ++i) {
            if (mergulhadores[i] != mergulhadores[i-1]+1) {
                for (int j = mergulhadores[i-1] + 1; j < mergulhadores[i]; ++j) {
                    falta[index++] = j;
                }
            }
        }

        if (r != n) {
            if (r + index != n) {
                for (int i = mergulhadores[r - 1] + 1; i <= n; ++i) {
                    falta[index++] = i;
                }
            }
            for (int i = 0; i < index; ++i) {
                printf("%d ", falta[i]);
            }
        } else cout << "*";

        printf("\n");

        index = 0;
    }

    return 0;
}