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
@app.route('/heap')
def heap_sort_code():
    heap_sort_code = """
import java.util.*;

public class Main {
    public static void sort(int arr[]) {
        int N = arr.length;
        for (int i = N / 2 - 1; i >= 0; i--)
            heapify(arr, N, i);
        for (int i = N - 1; i > 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);
        }
    }

    static void heapify(int arr[], int N, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < N && arr[l] > arr[largest])
            largest = l;
        if (r < N && arr[r] > arr[largest])
            largest = r;
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
            heapify(arr, N, largest);
        }
    }

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = s.nextInt();
        sort(arr);
        System.out.println("Sorted array is");
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
}
"""
    return heap_sort_code

@app.route('/binomial')
def binomial():
    code = """
import java.util.*;

class BinomialHeapNode {
    int key, degree;
    BinomialHeapNode parent;
    BinomialHeapNode sibling;
    BinomialHeapNode child;

    public BinomialHeapNode(int k) {
        key = k;
        degree = 0;
        parent = null;
        sibling = null;
        child = null;
    }

    public BinomialHeapNode reverse(BinomialHeapNode sibl) {
        BinomialHeapNode ret;
        if (sibling != null)
            ret = sibling.reverse(this);
        else
            ret = this;
        sibling = sibl;
        return ret;
    }

    public BinomialHeapNode findMinNode() {
        BinomialHeapNode x = this, y = this;
        int min = x.key;
        while (x != null) {
            if (x.key < min) {
                y = x;
                min = x.key;
            }
            x = x.sibling;
        }
        return y;
    }

    public BinomialHeapNode findANodeWithKey(int value) {
        BinomialHeapNode temp = this, node = null;
        while (temp != null) {
            if (temp.key == value) {
                node = temp;
                break;
            }
            if (temp.child == null)
                temp = temp.sibling;
            else {
                node = temp.child.findANodeWithKey(value);
                if (node == null)
                    temp = temp.sibling;
                else
                    break;
            }
        }
        return node;
    }

    public int getSize() {
        return (1 + ((child == null) ? 0 : child.getSize()) + ((sibling == null) ? 0 : sibling.getSize()));
    }
}

class BinomialHeap {
    private BinomialHeapNode Nodes;
    private int size;

    public BinomialHeap() {
        Nodes = null;
        size = 0;
    }

    public boolean isEmpty() {
        return Nodes == null;
    }

    public int getSize() {
        return size;
    }

    public void makeEmpty() {
        Nodes = null;
        size = 0;
    }

    public void insert(int value) {
        if (value > 0) {
            BinomialHeapNode temp = new BinomialHeapNode(value);
            if (Nodes == null) {
                Nodes = temp;
                size = 1;
            } else {
                unionNodes(temp);
                size++;
            }
        }
    }

    private void merge(BinomialHeapNode binHeap) {
        BinomialHeapNode temp1 = Nodes, temp2 = binHeap;
        while ((temp1 != null) && (temp2 != null)) {
            if (temp1.degree == temp2.degree) {
                BinomialHeapNode tmp = temp2;
                temp2 = temp2.sibling;
                tmp.sibling = temp1.sibling;
                temp1.sibling = tmp;
                temp1 = tmp.sibling;
            } else {
                if (temp1.degree < temp2.degree) {
                    if ((temp1.sibling == null) || (temp1.sibling.degree > temp2.degree)) {
                        BinomialHeapNode tmp = temp2;
                        temp2 = temp2.sibling;
                        tmp.sibling = temp1.sibling;
                        temp1.sibling = tmp;
                        temp1 = tmp.sibling;
                    } else
                        temp1 = temp1.sibling;
                } else {
                    BinomialHeapNode tmp = temp1;
                    temp1 = temp2;
                    temp2 = temp2.sibling;
                    temp1.sibling = tmp;
                    if (tmp == Nodes)
                        Nodes = temp1;
                }
            }
        }
        if (temp1 == null) {
            temp1 = Nodes;
            while (temp1.sibling != null)
                temp1 = temp1.sibling;
            temp1.sibling = temp2;
        }
    }

    private void unionNodes(BinomialHeapNode binHeap) {
        merge(binHeap);
        BinomialHeapNode prevTemp = null, temp = Nodes, nextTemp = Nodes.sibling;
        while (nextTemp != null) {
            if ((temp.degree != nextTemp.degree) || ((nextTemp.sibling != null) && (nextTemp.sibling.degree == temp.degree))) {
                prevTemp = temp;
                temp = nextTemp;
            } else {
                if (temp.key <= nextTemp.key) {
                    temp.sibling = nextTemp.sibling;
                    nextTemp.parent = temp;
                    nextTemp.sibling = temp.child;
                    temp.child = nextTemp;
                    temp.degree++;
                } else {
                    if (prevTemp == null)
                        Nodes = nextTemp;
                    else
                        prevTemp.sibling = nextTemp;
                    temp.parent = nextTemp;
                    temp.sibling = nextTemp.child;
                    nextTemp.child = temp;
                    nextTemp.degree++;
                    temp = nextTemp;
                }
            }
            nextTemp = temp.sibling;
        }
    }

    public int findMinimum() {
        return Nodes.findMinNode().key;
    }

    public void delete(int value) {
        if ((Nodes != null) && (Nodes.findANodeWithKey(value) != null)) {
            decreaseKeyValue(value, findMinimum() - 1);
            extractMin();
        }
    }

    public void decreaseKeyValue(int old_value, int new_value) {
        BinomialHeapNode temp = Nodes.findANodeWithKey(old_value);
        if (temp == null)
            return;
        temp.key = new_value;
        BinomialHeapNode tempParent = temp.parent;
        while ((tempParent != null) && (temp.key < tempParent.key)) {
            int z = temp.key;
            temp.key = tempParent.key;
            tempParent.key = z;
            temp = tempParent;
            tempParent = tempParent.parent;
        }
    }

    public int extractMin() {
        if (Nodes == null)
            return -1;
        BinomialHeapNode temp = Nodes, prevTemp = null;
        BinomialHeapNode minNode = Nodes.findMinNode();

        while (temp.key != minNode.key) {
            prevTemp = temp;
            temp = temp.sibling;
        }
        if (prevTemp == null)
            Nodes = temp.sibling;
        else
            prevTemp.sibling = temp.sibling;
        temp = temp.child;
        BinomialHeapNode fakeNode = temp;
        while (temp != null) {
            temp.parent = null;
            temp = temp.sibling;
        }
        if ((Nodes == null) && (fakeNode == null))
            size = 0;
        else {
            if ((Nodes == null) && (fakeNode != null)) {
                Nodes = fakeNode.reverse(null);
                size = Nodes.getSize();
            } else {
                if ((Nodes != null) && (fakeNode == null))
                    size = Nodes.getSize();
                else {
                    unionNodes(fakeNode.reverse(null));
                    size = Nodes.getSize();
                }
            }
        }
        return minNode.key;
    }

    public void displayHeap() {
        System.out.print("\nHeap : ");
        displayHeap(Nodes);
        System.out.println("\n");
    }

    private void displayHeap(BinomialHeapNode r) {
        if (r != null) {
            displayHeap(r.child);
            System.out.print(r.key + " ");
            displayHeap(r.sibling);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        BinomialHeap binHeap = new BinomialHeap();
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for (int i = 0; i < n; i++)
            binHeap.insert(s.nextInt());
        System.out.println("Size:" + binHeap.getSize());
        binHeap.displayHeap();
        binHeap.delete(s.nextInt());
        System.out.println("Size:" + binHeap.getSize());
        binHeap.displayHeap();
        System.out.println(binHeap.isEmpty());
        binHeap.makeEmpty();
        System.out.println(binHeap.isEmpty());
    }
}
"""
    return code

@app.route('/kary')
def kary_heap_code():
    code = """
public class Main {
    public static void main(String[] args) {
        final int capacity = 100;
        int[] arr = new int[capacity];
        arr[0] = 4;
        arr[1] = 5;
        arr[2] = 6;
        arr[3] = 7;
        arr[4] = 8;
        arr[5] = 9;
        arr[6] = 10;
        int n = 7;
        int k = 3;
        buildHeap(arr, n, k);
        System.out.println("Built Heap: ");
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
        int element = 3;
        insert(arr, n, k, element);
        n++;
        System.out.println("Heap after insertion of " + element + ": ");
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
        System.out.println("Extracted max is " + extractMax(arr, n, k));
        n--;
        System.out.println("\n\nHeap after extract max: ");
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
    }

    public static void buildHeap(int[] arr, int n, int k) {
        for (int i = (n - 1) / k; i >= 0; i--)
            restoreDown(arr, n, i, k);
    }

    public static void insert(int[] arr, int n, int k, int elem) {
        arr[n - 1] = elem;
        restoreUp(arr, n - 1, k);
    }

    public static int extractMax(int[] arr, int n, int k) {
        int max = arr[0];
        arr[0] = arr[n - 1];
        restoreDown(arr, n - 1, 0, k);
        return max;
    }

    public static void restoreDown(int[] arr, int len, int index, int k) {
        int[] child = new int[k + 1];
        while (true) {
            for (int i = 1; i <= k; i++)
                child[i] = (k * index + i) < len ? (k * index + i) : -1;
            int maxChild = -1, maxChildIndex = 0;
            for (int i = 1; i <= k; i++) {
                if (child[i] != -1 && arr[child[i]] > maxChild) {
                    maxChildIndex = child[i];
                    maxChild = arr[child[i]];
                }
            }
            if (maxChild == -1)
                break;
            if (arr[index] < arr[maxChildIndex])
                swap(arr, index, maxChildIndex);
            index = maxChildIndex;
        }
    }

    public static void restoreUp(int[] arr, int index, int k) {
        int parent = (index - 1) / k;
        while (parent >= 0) {
            if (arr[index] > arr[parent]) {
                swap(arr, index, parent);
                index = parent;
                parent = (index - 1) / k;
            } else
                break;
        }
    }

    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
"""
    return code

@app.route('/winner')
def winner_tree_code():
    code = """
import java.util.*;
class Node {
    int idx;
    Node left, right;
}
class Main {
    static Node createNode(int idx) {
        Node t = new Node();
        t.left = t.right = null;
        t.idx = idx;
        return t;
    }
    static void traverseHeight(Node root, int[] arr, int[] res) {
        if (root == null || (root.left == null && root.right == null))
            return;
        if (res[0] > arr[root.left.idx] && root.left.idx != root.idx) {
            res[0] = arr[root.left.idx];
            traverseHeight(root.right, arr, res);
        }
        else if(res[0]>arr[root.right.idx]&& root.right.idx!=root.idx){
            res[0] = arr[root.right.idx];
            traverseHeight(root.left, arr, res);
        }
    }
    static void findSecondMin(int[] arr, int n) {
        List<Node> li = new LinkedList<>();
        Node root = null;
        for (int i = 0; i < n; i += 2) {
            Node t1 = createNode(i);
            Node t2 = null;
            if (i + 1 < n) {
                t2 = createNode(i + 1);
                root = (arr[i] < arr[i + 1]) ? createNode(i) : createNode(i + 1);
                root.left = t1;
                root.right = t2;
                li.add(root);
            } 
            else
                li.add(t1);
        }
        int lsize = li.size();
        while (lsize != 1) {
            int last = (lsize & 1) == 1 ? lsize - 2 : lsize - 1;
            for (int i = 0; i < last; i += 2) {
                Node f1 = li.remove(0);
                Node f2 = li.remove(0);
                root = (arr[f1.idx] < arr[f2.idx]) ? createNode(f1.idx) : createNode(f2.idx);
                root.left = f1;
                root.right = f2;
                li.add(root);
            }
            if ((lsize & 1) == 1) {
                li.add(li.get(0));
                li.remove(0);
            }
            lsize = li.size();
        }
        int[] res = {Integer.MAX_VALUE};
        traverseHeight(root, arr, res);
        System.out.println("Minimum: " + arr[root.idx] + ", Second minimum: " + res[0]);
    }
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int arr[] = new int[n];
        for(int i=0; i<n; i++)
            arr[i]=s.nextInt();
        findSecondMin(arr, n);
    }
}
"""
    return code

@app.route('/recover')
def recover_bst_code():
    code = """
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { 
        this.val = val; 
    }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class Solution {
    public void recoverTree(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;
        TreeNode lastProcessed = null;
        TreeNode[] swapped = new TreeNode[2];
        while (!stack.isEmpty() || current != null) {
            while (current != null) {
                stack.push(current);
                current = current.left;
            }
            current = stack.pop();
            if (lastProcessed != null && lastProcessed.val > current.val) {
                if (swapped[0] == null) {
                    swapped[0] = lastProcessed;
                    swapped[1] = current;
                } 
                else {
                    swapped[1] = current;
                    break;
                }
            }
            lastProcessed = current;
            current = current.right;
        }
        int temp = swapped[0].val;
        swapped[0].val = swapped[1].val;
        swapped[1].val = temp;
    }
    static void printInorder(TreeNode node)
    {
        if (node == null)
            return;
        printInorder(node.left);
        System.out.print(" " + node.val);
        printInorder(node.right);
    }
}
"""
    return code

@app.route('/views')
def views():
    code = """
import java.util.*;
import java.util.Map.Entry;

class Node {
    int data, hd;
    Node left, right;

    public Node(int data) {
        this.data = data;
        left = right = null;
        this.hd = Integer.MAX_VALUE;
    }
}

class Main {
    static Node root;
    private List<Integer> path1 = new ArrayList<>();
    private List<Integer> path2 = new ArrayList<>();

    static Node build(String s[]) {
        if (s[0] == "N" || s.length == 0)
            return null;
        Node root = new Node(Integer.parseInt(s[0]));
        Queue<Node> q = new LinkedList<Node>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < s.length) {
            Node curr = q.poll();
            String cval = s[i];
            if (!cval.equals("N")) {
                int h = Integer.parseInt(cval);
                curr.left = new Node(h);
                q.add(curr.left);
            }
            i++;
            if (i >= s.length)
                break;
            cval = s[i];
            if (!cval.equals("N")) {
                int h = Integer.parseInt(cval);
                curr.right = new Node(h);
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    // Right View
    void rightview(Node root) {
        if (root == null)
            return;
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                Node curr = q.peek();
                q.remove();
                if (i == n - 1) {
                    System.out.print(curr.data + " ");
                    if (curr.left != null)
                        q.add(curr.left);
                    if (curr.right != null)
                        q.add(curr.right);
                }
            }
        }
    }

    // Left View
    void leftview(Node root) {
        if (root == null)
            return;
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int n = queue.size();
            for (int i = 1; i <= n; i++) {
                Node temp = queue.poll();
                if (i == 1)
                    System.out.print(temp.data + " ");
                if (temp.left != null)
                    queue.add(temp.left);
                if (temp.right != null)
                    queue.add(temp.right);
            }
        }
    }

    // Top View
    static class QueueObj {
        Node node;
        int hd;

        QueueObj(Node node, int hd) {
            this.node = node;
            this.hd = hd;
        }
    }

    static void topview(Node root) {
        if (root == null)
            return;
        Queue<QueueObj> q = new LinkedList<>();
        Map<Integer, Integer> map = new HashMap<>();
        int min = 0;
        int max = 0;
        q.add(new QueueObj(root, 0));
        while (!q.isEmpty()) {
            QueueObj curr = q.poll();
            if (!map.containsKey(curr.hd))
                map.put(curr.hd, curr.node.data);
            if (curr.node.left != null) {
                min = Math.min(min, curr.hd - 1);
                q.add(new QueueObj(curr.node.left, curr.hd - 1));
            }
            if (curr.node.right != null) {
                max = Math.max(max, curr.hd + 1);
                q.add(new QueueObj(curr.node.right, curr.hd + 1));
            }
        }
        for (; min <= max; min++)
            System.out.print(map.get(min) + " ");
    }

    // Bottom View
    static void bottomview(Node root) {
        if (root == null)
            return;
        int hd = 0;
        Map<Integer, Integer> map = new TreeMap<>();
        Queue<Node> queue = new LinkedList<Node>();
        root.hd = hd;
        queue.add(root);
        while (!queue.isEmpty()) {
            Node temp = queue.remove();
            hd = temp.hd;
            map.put(hd, temp.data);
            if (temp.left != null) {
                temp.left.hd = hd - 1;
                queue.add(temp.left);
            }
            if (temp.right != null) {
                temp.right.hd = hd + 1;
                queue.add(temp.right);
            }
        }
        Set<Entry<Integer, Integer>> set = map.entrySet();
        Iterator<Entry<Integer, Integer>> iterator = set.iterator();
        while (iterator.hasNext()) {
            Map.Entry<Integer, Integer> me = iterator.next();
            System.out.print(me.getValue() + " ");
        }
    }

    // main method
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i;
        Main ob = new Main();
        String s[] = sc.nextLine().split(" ");
        root = build(s);
        ob.rightview(root);
        System.out.println();
        ob.leftview(root);
        System.out.println();
        ob.topview(root);
        System.out.println();
        ob.bottomview(root);
    }
}
"""
    return code
@app.route('/vertical')
def vertical():
    code = """
import java.util.*;
import java.util.Map.Entry;

class Node {
    int data;
    Node left, right;
    public Node(int data){
        this.data = data;
        left = right = null;
    }
}

class Main {
    static Node root;
    private List<Integer> path1 = new ArrayList<>();
    private List<Integer> path2 = new ArrayList<>();
    static Node build(String s[]){
        if(s[0]=="N"||s.length==0)
            return null;
        Node root=new Node(Integer.parseInt(s[0]));
        Queue<Node> q=new LinkedList<Node>();
        q.add(root);
        int i=1;
        while(!q.isEmpty() && i<s.length){
            Node curr=q.poll();
            String cval=s[i];
            if(!cval.equals("N")){
                int h=Integer.parseInt(cval);
                curr.left=new Node(h);
                q.add(curr.left);
            }
            i++;
            if(i >= s.length)
                break;
            cval = s[i];
            if(!cval.equals("N")){
                int h=Integer.parseInt(cval);
                curr.right=new Node(h);
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }
    
    static void preOrderTraversal(Node root, long hd, long vd, TreeMap<Long, Vector<Integer> > m){
        if (root == null)
            return;
        long val = hd << 30 | vd;
        if (m.get(val) != null)
            m.get(val).add(root.data);
        else {
            Vector<Integer> v = new Vector<Integer>();
            v.add(root.data);
            m.put(val, v);
        }
        preOrderTraversal(root.left, hd - 1, vd + 1, m);
        preOrderTraversal(root.right, hd + 1, vd + 1, m);
    }

    void verticalOrder(Node root){
        TreeMap<Long, Vector<Integer> > mp = new TreeMap<>();
        preOrderTraversal(root, 0, 1, mp);
        int prekey = Integer.MAX_VALUE;
        for (Entry<Long, Vector<Integer> > entry :mp.entrySet()) {
            if(prekey!=Integer.MAX_VALUE && (entry.getKey()>>30)!= prekey)
                System.out.println();
            prekey = (int)(entry.getKey() >> 30);
            for (int x : entry.getValue())
                System.out.print(x + " ");
        }
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int i;
        Main ob = new Main();
        String s[]=sc.nextLine().split(" ");
        root = build(s);
        ob.verticalOrder(root);
    }
}
"""
    return code
@app.route('/boundary')
def traversal_code():
    code = """
import java.util.*;
import java.util.Map.Entry;

class Node {
    int data;
    Node left, right;
    public Node(int data){
        this.data = data;
        left = right = null;
    }
}

class Main {
    static Node root;
    private List<Integer> path1 = new ArrayList<>();
    private List<Integer> path2 = new ArrayList<>();

    static Node build(String s[]){
        if(s[0]=="N"||s.length==0)
            return null;
        Node root=new Node(Integer.parseInt(s[0]));
        Queue<Node> q=new LinkedList<Node>();
        q.add(root);
        int i=1;
        while(!q.isEmpty() && i<s.length){
            Node curr=q.poll();
            String cval=s[i];
            if(!cval.equals("N")){
                int h=Integer.parseInt(cval);
                curr.left=new Node(h);
                q.add(curr.left);
            }
            i++;
            if(i >= s.length)
                break;
            cval = s[i];
            if(!cval.equals("N")){
                int h=Integer.parseInt(cval);
                curr.right=new Node(h);
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    //print the leaves
    void printLeaves(Node node){
        if (node == null)
            return;
        printLeaves(node.left);
        if (node.left == null && node.right == null)
            System.out.print(node.data + " ");
        printLeaves(node.right);
    }

    //left boundary
    void printBoundaryLeft(Node node){
        if (node == null)
            return;
        if (node.left != null) {
            System.out.print(node.data + " ");
            printBoundaryLeft(node.left);
        }
        else if (node.right != null) {
            System.out.print(node.data + " ");
            printBoundaryLeft(node.right);
        }
    }

    //right boundary
    void printBoundaryRight(Node node){
        if (node == null)
            return;
        if (node.right != null) {
            printBoundaryRight(node.right);
            System.out.print(node.data + " ");
        }
        else if (node.left != null) {
            printBoundaryRight(node.left);
            System.out.print(node.data + " ");
        }
    }

    void printBoundary(Node node){
        if (node == null)
            return;
        System.out.print(node.data + " ");
        printBoundaryLeft(node.left);
        printLeaves(node.left);
        printLeaves(node.right);
        printBoundaryRight(node.right);
    }

    //main method
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int i;
        Main ob = new Main();
        String s[]=sc.nextLine().split(" ");
        root = build(s);
        ob.printBoundary(root);
    }
}
    """
    return code
@app.route('/bfsgraph')
def tracode():
    code = """
import java.util.*;

class Node {
	int num;
	Node next;
	Node(int val) {
		num=val;
		next=null;
	}  
}

class Main {
    static Node insertNode(Node head, int val) {
        Node newNode = new Node(val);
        if(head==null) {
            head=newNode;
            return head;
        }
        Node temp=head;
        while(temp.next!=null)
            temp=temp.next;
        temp.next=newNode;
        return head;
    }

    static void display(Node head)  {
        Node temp = head;
        while(temp.next!=null)  {
            System.out.print(temp.num+"->");
            temp=temp.next;
        }
        System.out.println(temp.num+"->"+"NULL");
    }

    static void createCycle(Node head,int a,int b) {
        int cnta = 0,cntb = 0;
        Node p1 = head;
        Node p2 = head;
        while(cnta != a || cntb != b) {
            if(cnta != a) 
                p1 = p1.next; ++cnta;
            if(cntb != b) 
                p2 = p2.next; ++cntb;    
        }
        p2.next = p1;  
    }

    static boolean cycleDetect(Node head) {
        if(head == null) return false;
        Node fast = head;
        Node slow = head;
            
        while(fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if(fast == slow) return true;
        }
        return false;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        Node head = null;
        for(int i=0;i<n;i++) {
            int m=sc.nextInt();
            head=insertNode(head,m);
        }
        display(head);
        int a=sc.nextInt();
        createCycle(head,1,a); // creating cycle in the list
        if(cycleDetect(head) == true)
            System.out.println("Cycle detected");
        else
            System.out.println("Cycle not detected");
    }
}
    """
    return code


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
