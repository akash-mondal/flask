from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():    
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/dial')
def dial():
    code = """
import java.util.*;

public class Graph {

    static final int INF = Integer.MAX_VALUE;

    private int V;
    private ArrayList<ArrayList<Tuple> > adj;

    public Graph(int v){
        this.V = v;
        this.adj = new ArrayList<ArrayList<Tuple> >();
        for (int i = 0; i < v; i++)
            this.adj.add(new ArrayList<Tuple>());
    }

    public void AddEdge(int u, int v, int w){
        adj.get(u).add(new Tuple(v, w));
        adj.get(v).add(new Tuple(u, w));
    }

    public void shortestPath(int src, int W){
        int[] dist = new int[V];
        Arrays.fill(dist, INF);
        ArrayList<Integer>[] B = new ArrayList[W * V + 1];
        for (int i = 0; i < W * V + 1; i++)
            B[i] = new ArrayList<Integer>();
        B[0].add(src);
        dist[src] = 0;
        int idx = 0;
        while (true) {
            while (B[idx].size() == 0 && idx < W * V)
                idx++;
            if (idx == W * V)
                break;
            int u = B[idx].get(0);
            B[idx].remove(0);
            for (Tuple i : adj.get(u)) {
                int v = i.v;
                int weight = i.w;
                int du = dist[u];
                int dv = dist[v];
                if (dv > du + weight) {
                    dist[v] = du + weight;
                    dv = dist[v];
                    B[dv].add(0, v);
                }
            }
        }
        System.out.println("Vertex Distance from Source");
        for (int i = 0; i < V; ++i)
            System.out.println(i + "\t\t" + dist[i]);
    }

    static class Tuple {
        int v, w;
        Tuple(int v, int w){
            this.v = v;
            this.w = w;
        }
    }

    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        int V = s.nextInt();
        Graph g = new Graph(V);
        int e=s.nextInt();
        int st,en,d;
        for(int i=0; i<e; i++){
            st=s.nextInt();
            en=s.nextInt();
            d=s.nextInt();
            g.AddEdge(st,en,d);
        }
        g.shortestPath(0,e);
    }
}
"""
    return code

@app.route('/bellman')
def bellman():
    code = """
import java.util.*;

class Main {

    class Edge {
        int src, dest, weight;
        Edge(){
            src = dest = weight = 0;
        }
    };

    int V, E;
    Edge edge[];

    Main(int v, int e){
        V = v;
        E = e;
        edge = new Edge[e];
        for (int i = 0; i < e; ++i)
            edge[i] = new Edge();
    }

    void BellmanFord(Main graph, int src){
        int V = graph.V, E = graph.E;
        int dist[] = new int[V];
        for (int i = 0; i < V; ++i)
            dist[i] = Integer.MAX_VALUE;
        dist[src] = 0;
        for (int i = 1; i < V; ++i) {
            for (int j = 0; j < E; ++j) {
                int u = graph.edge[j].src;
                int v = graph.edge[j].dest;
                int weight = graph.edge[j].weight;
                if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v])
                    dist[v] = dist[u] + weight;
            }
        }
        for (int j = 0; j < E; ++j) {
            int u = graph.edge[j].src;
            int v = graph.edge[j].dest;
            int weight = graph.edge[j].weight;
            if(dist[u]!=Integer.MAX_VALUE && dist[u]+weight<dist[v]){
                System.out.println(-1);
                return;
            }
        }
        for(int i = 0; i < V; ++i)
            if(dist[i]!=Integer.MAX_VALUE)
                System.out.print(dist[i]+" ");
            else
                System.out.print(-1+" ");
    }

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int V = sc.nextInt();
        int E = sc.nextInt();
        Main graph = new Main(V,E);
        for(int i=0;i<E;i++){
            int u=sc.nextInt();
            int v=sc.nextInt();
            int w=sc.nextInt();
            graph.edge[i].src = u;
            graph.edge[i].dest = v;
            graph.edge[i].weight = w;
        }
        graph.BellmanFord(graph, 0);
    }
}
"""
    return code

@app.route('/topo')
def topo():
    code = """
import java.util.*;

class TopologicalSort {

    private boolean detectCycleUtil(List<List<Integer>> adj, int[] visited, int v) {
        if (visited[v] == 1)
            return true;
        if (visited[v] == 2)
            return false;
        visited[v] = 1;
        for (int i = 0; i < adj.get(v).size(); ++i)
            if (detectCycleUtil(adj, visited, adj.get(v).get(i)))
                return true;
        visited[v] = 2;
        return false;
    }

    private boolean detectCycle(List<List<Integer>> adj, int n) {
        int[] visited = new int[n];
        for (int i = 0; i < n; ++i)
            if (visited[i] == 0)
                if (detectCycleUtil(adj, visited, i))
                    return true;
        return false;
    }

    private void dfs(List<List<Integer>> adj, int v, boolean[] visited, Stack<Integer> mystack) {
        visited[v] = true;
        for (int i = 0; i < adj.get(v).size(); ++i)
            if (!visited[adj.get(v).get(i)])
                dfs(adj, adj.get(v).get(i), visited, mystack);
        mystack.push(v);
    }

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++)
            adj.add(new ArrayList<>());
        for (int i = 0; i < prerequisites.length; ++i)
            adj.get(prerequisites[i][1]).add(prerequisites[i][0]);
        int[] ans = new int[numCourses];
        if (detectCycle(adj, numCourses))
            return new int[0];
        Stack<Integer> mystack = new Stack<>();
        boolean[] visited = new boolean[numCourses];
        for (int i = 0; i < numCourses; ++i)
            if (!visited[i])
                dfs(adj, i, visited, mystack);
        int index = 0;
        while (!mystack.isEmpty()) {
            ans[index++] = mystack.pop();
        }
        return ans;
    }

    public static void main(String[] args) {
        TopologicalSort solution = new TopologicalSort();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of courses: ");
        int numCourses = scanner.nextInt();
        System.out.print("Enter the number of prerequisites: ");
        int n = scanner.nextInt();
        int[][] prerequisites = new int[n][2];
        System.out.println("Enter prerequisite pairs (course, prerequisite):");
        for (int i = 0; i < n; i++) {
            prerequisites[i][0] = scanner.nextInt();
            prerequisites[i][1] = scanner.nextInt();
        }
        int[] result = solution.findOrder(numCourses, prerequisites);
        System.out.println("Topological order of courses:");
        System.out.println(Arrays.toString(result));
    }
}
"""
    return code

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
