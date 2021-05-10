import java.lang.*;
import java.io.*;
class Number_pattern{

    public static void p(int[] arr){
        for(int i=0; i<arr.length; i++){
            System.out.print(arr[i]);
        }
        System.out.println();
    }

    public static int[] patternNo(String s){
        int[] res = new int[s.length()+1];
        int ind = s.indexOf("I");
        
        if (ind == -1){
            for(int j = 0; j<res.length; j++){
                res[j] = res.length-j;
            }
            return res;
        }
        
        res[ind] = 1;
        int m = 1;
        for(int i=ind - 1; i>=0; i--){
            res[i] = ++m;
        }
        
        ind = s.indexOf("I", ind+1);

        while (ind > -1){
            for(int j = ind; j>=0; j--){
                if(res[j] > 0) break;
                res[j] = ++m;       
            }
            ind = s.indexOf("I", ind+1);
        }

        for(int j=res.length-1; res[j]==0; j--){
            res[j] = ++m;
        } 
        return res;
    }

    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(; t>0; t--){
            String s = br.readLine();
            p(patternNo(s));
        }
        // StringTokenizer st = new StringTokenizer(br.readLine());
        
    }
}