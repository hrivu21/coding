import java.io.*;

public class FirstNonRepeatingChar{
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
        FastReader fr = new FastReader();
        int t = fr.nextInt();
        while(t-->0){
            int n = fr.nextInt();
            HashSet<String> set = new HashSet<String>();
            LinkedList<String> l = new LinkedList<String>();
            for(int i=0; i<n; i++){
                String s = fr.next();
                if (!set.contains(s)){
                    set.add(s);
                    l.add(s);
                }
                else{
                    l.remove(s);
                }
                if (l.size()>0) System.out.print(l.get(0)+" ");
                else System.out.print(-1+" ");
            }
            System.out.println();
        }
    }
}