import java.io.*;

public class KthSmallest {
    static class FastReader 
        { 
            BufferedReader br; 
            StringTokenizer st; 
      
            public FastReader() 
            { 
                br = new BufferedReader(new
                         InputStreamReader(System.in)); 
            } 
      
            String next() 
            { 
                while (st == null || !st.hasMoreElements()) 
                { 
                    try
                    { 
                        st = new StringTokenizer(br.readLine()); 
                    } 
                    catch (IOException  e) 
                    { 
                        e.printStackTrace(); 
                    } 
                } 
                return st.nextToken(); 
            } 
      
            int nextInt() 
            { 
                return Integer.parseInt(next()); 
            } 
      
            long nextLong() 
            { 
                return Long.parseLong(next()); 
            } 
      
            double nextDouble() 
            { 
                return Double.parseDouble(next()); 
            } 
      
            String nextLine() 
            { 
                String str = ""; 
                try
                { 
                    str = br.readLine(); 
                } 
                catch (IOException e) 
                { 
                    e.printStackTrace(); 
                } 
                return str; 
            } 
        } 
    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        FastReader sc = new FastReader();
        int t = sc.nextInt();
        for(int i=0; i<t; i++){
            int n = sc.nextInt();
            PriorityQueue<Integer> heap = new PriorityQueue<Integer>(n);
            for(int j=0; j<n; j++){
                heap.add(sc.nextInt());
            }
            int k = sc.nextInt();
            for(int l=0; l<k-1; l++){
                heap.poll();
            }
            System.out.println(heap.poll());
        }        
    }
}