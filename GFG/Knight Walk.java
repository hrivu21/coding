import java.io.*;

public class KnightWalk{
    static int steps[][] = {{2,1}, {2,-1}, {-2,1}, {-2,-1}, {1,2}, {1,-2}, {-1,2}, {-1,-2}};

    static boolean isValid(Node p, int n, int m){
        return (p.x>=0 && p.x<n && p.y>=0 && p.y<m);
    }
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

    static class Node{
        int x;
        int y;
        public Node(int x, int y){
            this.x = x;
            this.y = y;
        }
        public boolean isSame(Node n){
            return (this.x==n.x && this.y==n.y);
        }
    }

    public static int bfs(boolean[][] board, Node start, Node dest){
        int stepcount = 0;
        LinkedList<Node> queue = new LinkedList<Node>();

        queue.add(start);
        board[start.x][start.y] = true;
        int prevLayer = 1;
        int currLayer = 0;

        while(!queue.isEmpty()){
            start = queue.remove(0);
            prevLayer--;
            if(start.isSame(dest)){
                return stepcount;
            }
            for(int i = 0; i<8; i++){                
                Node next = new Node(start.x+steps[i][0], start.y+steps[i][1]);
                if (isValid(next, board.length, board[0].length) && !board[next.x][next.y]){
                    queue.add(next);
                    board[next.x][next.y] = true;
                    currLayer++;
                }
            }
            if(prevLayer == 0){
                stepcount++;
                prevLayer = currLayer;
                currLayer = 0;
            }          
        }
        return -1;
    }

    public static void main(String[] args) {
        FastReader fr = new FastReader();
        int t = fr.nextInt();
        while(t>0){
            int n = fr.nextInt();
            int m = fr.nextInt();
            int s1 = fr.nextInt()-1;
            int s2 = fr.nextInt()-1;
            int d1 = fr.nextInt()-1;
            int d2 = fr.nextInt()-1;

            boolean[][] board = new boolean[n][m];
            Node start = new Node(s1, s2);
            Node dest = new Node(d1, d2);
            System.out.println(bfs(board, start, dest));
            t--;
        }
    }
}