import java.lang.*;
import java.io.*;

import java.util.Scanner;
class GFG{
    public static int fn(int a[],int n,int sum){
        int modulo = 1000000000+7;
        int dp[][]=new int[n+1][sum+1]; // denotes no. of subset till n having sum=sum
        
        for(int i=0;i<=n;++i)
            dp[i][0]=1;
            
        for(int i=1;i<=n;++i)
        {
            for(int j=1;j<=sum;++j)
            {
                dp[i][j]=dp[i-1][j] % modulo;//do not include 
                if(a[i-1]<=j)
                    dp[i][j]+=dp[i-1][j-a[i-1]] % modulo; // include sum
            }
        }
        return dp[n][sum]% modulo;
    }
 public static void main (String[] args)
 {
     Scanner ab=new Scanner(System.in);
     int t=ab.nextInt();
     while(t-->0)
     {
         int n=ab.nextInt();
         
         int arr[]=new int[n];
         for(int i=0;i<n;++i)
            arr[i]=ab.nextInt();
            
         int k=ab.nextInt();
         
         System.out.println(fn(arr,n,k));
     }
 }
}