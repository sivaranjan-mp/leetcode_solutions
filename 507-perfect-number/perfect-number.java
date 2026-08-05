class Solution {
    public boolean checkPerfectNumber(int num) {
        int c=0;
        int i;
        for(i=1;i<=(num/2);i++){
            if(num%i==0){
                c+=i;
            }
        }
        if(c==num){
            return true;
        }
        else{
            return false;
        }
    }
}