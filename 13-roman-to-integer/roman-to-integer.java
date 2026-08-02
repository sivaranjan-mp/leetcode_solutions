class Solution {
    public int romanToInt(String s) {
        int a,j,i,v,x,l,c,d,m;
        i=0;v=0;x=0;l=0;c=0;d=0;m=0;
        a=s.length();
        char[] arr=s.toCharArray();
        int sum=0;

        for(j=0;j<a;j++){
            if(arr[j]=='I'){
                i=1;
                sum+=i;
            }
            else if(j>0 && arr[j]=='X' && arr[j-1]=='I' ){
                x=8;
                sum+=x;
            }
            else if(arr[j]=='X' ){
                x=10;
                sum+=x;
            }
            else if(j>0 && arr[j]=='V' && arr[j-1]=='I'){
                i=3;
                sum+=i;
            }
            else if(arr[j]=='V'){
                v=5;
                sum+=v;
            }
            else if( j>0 && arr[j]=='L' && arr[j-1]=='X'){
                l=30;
                sum+=l;
            }
            else if(arr[j]=='L'){
                l=50;
                sum+=l;
            }
             else if(j>0 && arr[j]=='C' && arr[j-1]=='X'){
                c=80;
                sum+=c;
            }
            else if(arr[j]=='C'){
                c=100;
                sum+=c;
            }
            else if(j>0 && arr[j]=='D' && arr[j-1]=='C'){
                d=300;
                sum+=d;
            }
            else if(arr[j]=='D'){
                d=500;
                sum+=d;
            }
            else if(j>0 && arr[j]=='M' && arr[j-1]=='C'){
                m=800;
                sum+=m;
            }
            else if(arr[j]=='M'){
                m=1000;
                sum+=m;
            }
        }

        return sum;
        
    }
}