#include <stdio.h>
#include <math.h>

#define INT_MIN -2,147,483,648
#define INT_MAX 2,147,483,647

int reverse(int x){
    int n,digit,i;
    int reversed=0;
    for (i=1,n=x;i<15;i++) {
        n/=10;
        if (abs(n)<10 && abs(n)>0) break;  /* This for loop provides us to find number of digits -1 */
        else if (n==0)  {
            i=0;
            break; 
        } 
    } 
    while (x!=0) {
        digit=x%10;
        x/=10;
        if ((reversed+digit*pow(10,i))>INT_MAX || (reversed+digit*pow(10,i))<INT_MIN) return 0; /* In order to overcome overflow error, there is a if statement that checks INT_MIN & INT_MAX */
        reversed+=digit*(pow(10,i));
        i--;
    }
    return reversed;
}
