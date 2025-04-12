void coin_change_greedy(int coins[], int n, int amount) {
    for (int i = 0; i < n; i++) {
        while (amount >= coins[i]) {
            amount -= coins[i];
        }
    }

}
