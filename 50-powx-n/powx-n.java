class Solution {
    public double myPow(double x, int n) {
        long k = n;
        double res = 1.0;

        if (k < 0) {
            x = 1 / x;
            k = -k;
        }

        while (k > 0) {
            if ((k & 1) == 1) {
                res *= x;
            }

            x *= x;
            k >>= 1;
        }

        return res;
    }
}