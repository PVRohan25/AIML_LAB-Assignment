#Part 1 – Implement Breadth First Search Algorithm using a Queue
from collections import deque

def bfs(graph, start):
    open_list = deque([start])  
    closed_list = set() 

    while open_list:
        current = open_list.popleft() 
        if current not in closed_list:
            print(current) 
            closed_list.add(current)  

            for neighbor in graph[current]:
                if neighbor not in closed_list:
                    open_list.append(neighbor)

print("BFS Traversal:")
graph = {
    0: [1, 3],
    1: [0, 2, 3],
    2: [1, 4, 5],
    3: [0, 1, 4],
    4: [2, 3, 5],
    5: [2, 4]
}
bfs(graph, 0)
print("\n")

#Part 2 – Implement Depth First Search Algorithm using a Stack
def dfs(graph, start):
    stack = [start]  
    visited = set()  

    while stack:
        current = stack.pop()  
        if current not in visited:
            print(current) 
            visited.add(current)  
            
            for neighbor in reversed(graph[current]): 
                if neighbor not in visited:
                    stack.append(neighbor)

print("DFS Traversal:")
graph = {
    'S': ['A', 'C', 'F'],
    'A': ['B', 'S'],
    'B': ['A'],
    'C': ['D', 'E', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['G', 'S'],
    'G': ['F'],
    'H': ['E']
}
dfs(graph, 'S')
print("\n")

#Part 3 – Implement A* Algorithm using Numpy
import numpy as np
from heapq import heappush, heappop

def manhattan_distance(state, final_state):
    distance = 0
    for i in range(1, 9):  
        xi, yi = np.where(state == i)
        xf, yf = np.where(final_state == i)
        distance += abs(xi - xf) + abs(yi - yf)
    return distance[0]

def a_star(initial_state, goal_state):
    open_set = []
    heappush(open_set, (manhattan_distance(initial_state, goal_state), initial_state.tolist(), 0))
    came_from = {}
    g_score = {str(initial_state.tolist()): 0}

    while open_set:
        current_f_score, current_state, current_g_score = heappop(open_set)
        current_state = np.array(current_state)

        if np.array_equal(current_state, goal_state):
            return reconstruct_path(came_from, current_state)

        zero_pos = tuple(np.argwhere(current_state == 0)[0])
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_zero_pos = (zero_pos[0] + dx, zero_pos[1] + dy)
            if 0 <= new_zero_pos[0] < 3 and 0 <= new_zero_pos[1] < 3:
                new_state = np.copy(current_state)
                new_state[zero_pos], new_state[new_zero_pos] = new_state[new_zero_pos], new_state[zero_pos]
                new_g_score = current_g_score + 1

                if str(new_state.tolist()) not in g_score or new_g_score < g_score[str(new_state.tolist())]:
                    g_score[str(new_state.tolist())] = new_g_score
                    f_score = new_g_score + manhattan_distance(new_state, goal_state)
                    heappush(open_set, (f_score, new_state.tolist(), new_g_score))
                    came_from[str(new_state.tolist())] = current_state.tolist()

    return None

def reconstruct_path(came_from, current):
    total_path = [current.tolist()]
    while str(current.tolist()) in came_from:
        current = np.array(came_from[str(current.tolist())])
        total_path.append(current.tolist())
    return total_path[::-1]  


initial = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
goal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

path = a_star(initial, goal)
for state in path:
    print(np.array(state))