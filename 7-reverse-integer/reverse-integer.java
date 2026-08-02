class Solution {
    public int reverse(int x) {
        int a,b,c;
        int max=Integer.MAX_VALUE;
        int min=Integer.MIN_VALUE;
        c=x;
        if(c<0 ){x=x*-1;}
        b=0;
        while(x>0){
            a=x%10;
            if (b > max / 10 || (b == max / 10 && a > 7)) {
                return 0;
            }
            if (b < min / 10 || (b == min / 10 && a < -8)) {
                return 0;
            }
            b=(b*10)+a;
            x=x/10;

        }
        if(c<0 && b<=max){
            return (b*-1);}
        
        else if(c>0 && b>=min){
            return b;
        }
        
        else{
            return 0;
        }
    }
}