import java.lang.*;
import java.io.*;
class GFG
 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            int n = sc.nextInt();
            int res = sc.nextInt();
            for(int i=1; i<n; i++){
                res^=sc.nextInt();
            }
            System.out.println(res);
        }
        
    }
}