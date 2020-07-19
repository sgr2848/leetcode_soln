#Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands
class Graph:
    def __init__(self,row, col, graph):
        self.row = row
        self.col = col
        self.graph = graph
    def is_safe(self, i, j, visited):
        return (i >= 0 and i < self.row and j>= 0 and j < self.col and not visited[i][j] and self.graph[i][j])
    def dfs(self, i, j, visited):
        neigh_row = [-1, -1, -1,  0, 0,  1, 1, 1]
        neigh_col = [-1,  0,  1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        # going through each neighbour
        for k in range(8):
            if self.is_safe(i + neigh_row[k], j + neigh_col[k], visited):
                print(
                    f'({i + neigh_row[k], j + neigh_col[k]})', end=" ,")
                self.dfs(i + neigh_row[k], j + neigh_col[k], visited)
    def count_island(self):
        count = 0 
        visited = [[False for j in range(self.col)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j] ==False and self.graph[i][j] == 1:
                    print(f"{i,j}",end= "::")
                    self.dfs(i, j, visited)
                    print(" ")
                    count += 1
        return count
if __name__ == "__main__":
    matrix = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]

    graph = Graph(len(matrix), len(matrix[0]), matrix)
    island_count = graph.count_island()
    print(f"The total number of island is {island_count}")

        
                
