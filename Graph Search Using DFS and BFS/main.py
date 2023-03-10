
class data_set():

    maze = [
        
            ['A',1,1,1],
            [0,1,1,0],
            [0,0,0,0],
            [0,1,1,0],
            [1,0,0,'G']
            
            ]

class Breadth_First_Search(data_set):

    def __init__(self) :
        self.maze = data_set.maze 
    
    def find_path(self):
        queue = [(0, 0, [])]  
        visited = set()
        rows, cols = len(self.maze), len(self.maze[0])

        while queue:
            row, col, path = queue.pop(0)
            if (row, col) not in visited:
                visited.add((row, col))
                if self.maze[row][col] == 'G':
                    return path + [(row, col)]
                for r, c in ((row-1, col), (row, col+1), (row+1, col), (row, col-1)):
                    if 0 <= r < rows and 0 <= c < cols and self.maze[r][c] != 1 and (r, c) not in visited:
                        queue.append((r, c, path + [(row, col)]))

        return None  
    
    def output_path(self):
        lst = []
        path = self.find_path()
        for i,j in path:
            lst.append(self.maze[i][j])    
        print("Path: ",lst)


class Depth_First_Search(data_set):
        
    def __init__(self):
        self.maze = data_set.maze
    
    def find_path(self):
        stack = [(0, 0, [])]  
        visited = set()
        rows, cols = len(self.maze), len(self.maze[0])

        while stack:
            row, col, path = stack.pop()
            if (row, col) not in visited:
                visited.add((row, col))
                if self.maze[row][col] == 'G':
                    return path + [(row, col)]
                for r, c in ((row-1, col), (row, col+1), (row+1, col), (row, col-1)):
                    if 0 <= r < rows and 0 <= c < cols and self.maze[r][c] != 1 and (r, c) not in visited:
                        stack.append((r, c , path + [(row, col)]))

        return None  

    def output_path(self):
        lst = []
        path = self.find_path()
        for i ,j in path:
            lst.append(self.maze[i][j])
        print("Path: ",lst)

if __name__ == '__main__':
    bfs = Breadth_First_Search()
    dfs = Depth_First_Search()

    print("Breadth First Search")
    print("Nodes: " , bfs.find_path())
    bfs.output_path()
    print()
    print("Depth First Search")
    print("Nodes: ",dfs.find_path())
    dfs.output_path()


