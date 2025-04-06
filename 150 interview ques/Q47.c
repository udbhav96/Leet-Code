/*https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 (20min)
double myPow(double x, int n) {
    double a = 1;

    if (n > 0) {
        for (int i = 0; i < n; i++) {
            a = a * x;
        }
    } else {
        for (int i = 0; i < -n; i++) {
            a = a * (1.0 / x);
        }
    }

    return a;
}
//code is correct but not optimize complexity n
//Try 2 Final(seen)
double myPow(double x, int n) {
    double res = 1;

    while (n != 0) {
        if (n % 2 != 0) {
            if (n > 0)
                res *= x;
            else
                res /= x;
        }
        x *= x;
        n /= 2;
    }

    return res;
}
//Seen because buke lagi and niche dukan band hone wali complexity is low and better approch 

