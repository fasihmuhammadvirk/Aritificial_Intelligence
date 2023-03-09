#Data Set Required for the Task
class data_set():
            
    # Define the graph using an adjacency list
    graph = {
        'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
        'Zerind': {'Arad': 75, 'Oradea': 71},
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Sibiu': {'Arad': 140, 'Oradea': 151, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
        'Dobreta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
        'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
        'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Bucharest': {'Pitesti': 101, 'Fagaras': 211, 'Giurgiu': 90, 'Urziceni': 85},
        'Giurgiu': {'Bucharest': 90},
        'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Eforie': {'Hirsova': 86},
        'Vaslui': {'Iasi': 92, 'Urziceni': 142},
        'Iasi': {'Vaslui': 92, 'Neamt': 87},
        'Neamt': {'Iasi': 87}
    }
    

#Depth First Search Class
class Depth_First_Search(data_set):

    def __init__(self,source, destination):
        self.graph = data_set.graph
        self.source = source 
        self.destination = destination

    # Finding the Shortest Path Using the Depth First Search
    def finding_shortest_path(self):
        stack = [(self.source, [self.source], 0)]
        visited = set()

        while stack:
            (current, path, distance) = stack.pop()
            visited.add(current)

            if current == self.destination:
                return path, distance

            for neighbor, weight in self.graph[current].items():
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], distance + weight))

        return None
    
    def output_shortest_path(self):
        
        print('The Shortest Path Found Using the Depth First Search is: ', self.finding_shortest_path(),'\n')


#Breadth First Search Algorithm Class
class Breadth_First_Search(data_set):

    def __init__(self, source , destination):
        self.graph = data_set.graph
        self.source = source 
        self.destination = destination

    # Finding the Shortest Path Using the Breadth First Search
    def finding_shortest_path(self ):
        queue = [(self.source , [self.source ], 0)]
        visited = set()

        while queue:
            (current, path, distance) = queue.pop(0)
            visited.add(current)

            if current == self.destination:
                return path, distance

            for neighbor, weight in self.graph[current].items():
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], distance + weight))

        return None   

    def output_shortest_path(self):
        
        print('The Shortest Path Found Using the Breadth First Search is: ', self.finding_shortest_path(),'\n')


#Checking Which Give the Shortest path and Outperformed the Other
def outperform_other(bfs,dfs):
    if bfs[1] < dfs[1]:
        print('Breadth First Search Outperformed the Depth First Search\n')
    elif bfs[1] == dfs[1]:
        print('Both Gave the Same Answer\n')
    else:
        print('Depth First Search Outperformed the Breadth First Search\n')
        
#Main
if __name__ == '__main__':
    
    #Starting Point
    source = 'Arad'
    #Goal 
    destination = 'Bucharest'

    #Object of the Breadth First Search Class
    bfs = Breadth_First_Search(source,destination)
    #Object of the Depth First Search Class
    dfs = Depth_First_Search(source,destination)
    
    #Printing the Shortest Path Using the BFS 
    bfs.output_shortest_path()
    #Printing the Shortest Path Using the DFS 
    dfs.output_shortest_path()
    
    #Checking the Performance
    outperform_other(bfs.finding_shortest_path(),dfs.finding_shortest_path())