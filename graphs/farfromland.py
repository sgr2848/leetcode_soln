import queue
class Graph:
    def __init__(self, row, col, grid):
        self.row = row
        self.col = col
        self.grid = grid
        self.visited = [[False for i in range(self.col)] for j in range(self.row)]
    def bfs(self):
        qu = queue.Queue()
        qu.put((0, 0))
        while qu.empty() == False:
            x = qu.get()
            n = x[0]
            m = x[1]
            if (n >= 0 and m >= 0 and n < self.row and m < self.col and not self.visited[n][m]):
                self.visited[n][m] =True
                print(self.grid[n][m],end =" ")
                qu.put((n,m-1))
                qu.put((n, m+1))
                qu.put((n-1, m))
                qu.put((n+1, m))

if __name__ == "__main__":
    a = [[1,2,4],[5,-23,121],[33,-11,0]]
    gr = Graph(len(a), len(a[0]), a)
    gr.bfs()
    
