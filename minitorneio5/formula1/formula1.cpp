#include <bits/stdc++.h>

using namespace std;

int formula1() {

    int g, p, sistemas, premiados, ponto, maior = -1, indice;
    int *maior_indice;
    int corridas[109][109];
    int corredores[109];

        while (true) {

        cin >> g >> p;
        
        if (p == 0 && g == 0) break;

        for (int i = 1; i <= p; ++i) {
            corredores[i] = 0;
        }

        for (int i = 0; i < g; ++i) {
            for (int j = 1; j <= p; ++j) {
                cin >> corridas[i][j];
            }
        }

        cin >> sistemas;

        for (int i = 0; i < sistemas; ++i) {
            cin >> premiados;
            for (int j = 0; j < premiados; ++j) {
                cin >> ponto;
                for (int k = 0; k < g; ++k) {
                    maior_indice = find(&corridas[k][0], &corridas[k][p], j+1);
                    indice = distance(corridas[k], maior_indice);
                    corredores[indice] += ponto;
                }
            }

            for (int j = 1; j <= p; ++j) {
                if (corredores[j] > maior) maior = corredores[j];
            }

            for (int j = 1; j <= p; ++j) {
                if (corredores[j] == maior) cout << j << " ";
                corredores[j] = 0;
            }

            cout << endl;
            maior = -1;
        }
    }

    return 0;
}
