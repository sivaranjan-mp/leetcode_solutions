class Solution {
    public int addDigits(int num) {
        int sum=0;
        int x,b,y;
        y=0;
        if(num<=9){
            return num;
        }
        while(num>9){
            b=num%10;
            x=num/10;
            sum=b+x;
            if(sum>=1&&sum<=9){
                y=sum;
                break;
            }
            else if(sum==0){
                y=sum;
                break;

            }
            else{
                num=sum;
            }
        }

 return y;
    }
}