#include <stdio.h>

double myPow(double x, int n) {    /* Time Complexity O(logn) - Space Complexity O(1) */

    if (n==0) return (double) 1;    /* Termination Condition */
    else if (n%2==0) {
        return n>0?(myPow(x,n/2)*myPow(x,n/2)):(myPow(x,n/2)*myPow(x,n/2));
    }
    else {    
        return n>0?(myPow(x,n/2)*myPow(x,n/2)*x):(myPow(x,n/2)*myPow(x,n/2)/x);
    }     

}
    