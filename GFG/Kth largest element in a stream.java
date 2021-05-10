import java.lang.*;
import java.io.*;
class GFG
 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        
        
        int t = sc.nextInt();
        while(t-- > 0){
            PriorityQueue<Integer> pQueue = new PriorityQueue<Integer>(); 
            int k = sc.nextInt();
            int n = sc.nextInt();
            
            for(int i=1; i<=n; i++){
                if (i <= k){
                    pQueue.add(sc.nextInt());
                }
                else{
                    int x = sc.nextInt();
                    if(x>=pQueue.peek()){
                        pQueue.poll();
                        pQueue.add(x);
                    }
                }
                if (i<k){
                    System.out.print(-1 + " ");
                }
                else{
                    System.out.print(pQueue.peek() + " ");
                }
            }
            System.out.println();
        }
        
    }
}