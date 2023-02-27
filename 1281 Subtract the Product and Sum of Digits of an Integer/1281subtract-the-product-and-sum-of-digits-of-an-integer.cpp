class Solution {
public:
    int subtractProductAndSum(int n) {
        int digit,sum,product,dif;
        sum=0;
        product=1;
        while(n!=0){
            digit=n%10;
            sum = sum + digit;
            product = product * digit;
            n = n / 10;
        }
        dif = product - sum;
        
        return dif;
    }
};