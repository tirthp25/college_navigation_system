import json
import heapq
import math

def load_graph():
    with open('data/graph.json') as f:
        return json.load(f)

def heuristic(a, b):
    return math.dist(a, b)

def a_star(graph, positions, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + heuristic(positions[current], positions[neighbor])
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(positions[neighbor], positions[goal])
                heapq.heappush(open_set, (f_score, neighbor))

    return []