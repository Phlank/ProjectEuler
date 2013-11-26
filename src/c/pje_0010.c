#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main() {
	static const MAX = 2000000;
        long primes[MAX/4];
        primes[0] = 2;
        primes[1] = 3;
        long long n = 3;
        long long sum = 5;
        int t = 2;
        while (primes[t-1] < MAX) {
                n += 2;
                int x;
                bool isPrime = true;
                long max = (int) (ceil(sqrt(n)));
                for (x = 0; x < t && primes[x] <= max; x++) {
                        if (n%primes[x] == 0)
                                isPrime = false;
                }
                if (isPrime) {
                        primes[t] = n;
                        t++;
                        sum += n;
                }
        }
        printf("%lld\n", sum);
        return 0;
}
