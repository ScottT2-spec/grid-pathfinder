# 0 = free, 1 = wall
grid = [
    [0,0,0,0,1,0,0],
    [1,1,0,0,1,0,1],
    [0,0,0,1,0,0,0],
    [0,1,0,0,0,1,0],
    [0,0,0,1,0,0,0]
]

start = (0,0)
goal = (4,6)

rows = len(grid)
cols = len(grid[0])

# BFS
def bfs_search():
    queue = [start]
    parents = {start: None}
    visited_nodes = []

    while queue:
        current = queue.pop(0)
        visited_nodes.append(current)

        if current == goal:
            break

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            r_new = current[0] + dr
            c_new = current[1] + dc
            neighbor = (r_new, c_new)

            if 0 <= r_new < rows and 0 <= c_new < cols and grid[r_new][c_new]==0 and neighbor not in parents:
                parents[neighbor] = current
                queue.append(neighbor)

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parents.get(cur)
    path.reverse()
    return visited_nodes, path

# DFS
def dfs_search():
    stack = [start]
    parent_map = {start: None}
    visited = []

    while stack:
        n = stack.pop()
        visited.append(n)

        if n == goal:
            break

        for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            r_new = n[0] + dr
            c_new = n[1] + dc
            neigh = (r_new,c_new)

            if 0 <= r_new < rows and 0 <= c_new < cols and grid[r_new][c_new]==0 and neigh not in parent_map:
                parent_map[neigh] = n
                stack.append(neigh)

    path = [goal]
    while path[-1] in parent_map and parent_map[path[-1]] is not None:
        path.append(parent_map[path[-1]])
    path.reverse()
    return visited, path

# A* search
def astar_search():
    open_list = [(0,start)]
    costs = {start:0}
    parents = {start: None}
    visited_nodes = []

    def manhattan(a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while open_list:
        open_list.sort()
        current = open_list.pop(0)[1]
        visited_nodes.append(current)

        if current == goal:
            break

        for move in [(1,0),(0,1),(-1,0),(0,-1)]:
            r = current[0]+move[0]
            c = current[1]+move[1]
            neighbor = (r,c)

            if 0 <= r < rows and 0 <= c < cols and grid[r][c]==0:
                new_cost = costs[current] + 1
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    priority = new_cost + manhattan(neighbor,goal)
                    open_list.append((priority, neighbor))
                    parents[neighbor] = current

    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parents.get(cur)
    path.reverse()
    return visited_nodes, path
def print_grid(path):
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            if (r,c) == start:
                row_str += "S "
            elif (r,c) == goal:
                row_str += "G "
            elif (r,c) in path:
                row_str += "* "
            elif grid[r][c] == 1:
                row_str += "# "
            else:
                row_str += ". "
        print(row_str)
    print("\n")
# BFS search
b_vis, b_path = bfs_search()
print("\nBFS Pathfinding:")
print("Visited nodes count:", len(b_vis))
print("Path length:", len(b_path))
print_grid(b_path)

# DFS search
d_vis, d_path = dfs_search()
print("\nDFS Pathfinding:")
print("Visited nodes count:", len(d_vis))
print("Path length:", len(d_path))
print_grid(d_path)

# A*
a_vis, a_path = astar_search()
print("\nA* Pathfinding:")
print("Visited nodes count:", len(a_vis))
print("Path length:", len(a_path))
print_grid(a_path)
