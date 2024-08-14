import os
import json
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        max_dist = -1
        max_node = v

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                dist, node = self.DFS(neighbor, visited)
                if dist > max_dist:
                    max_dist = dist
                    max_node = node

        return max_dist + 1, max_node

    def diameterOfTree(self, start):
        visited = [False] * (max(self.graph.keys()) + 1)
        _, farthest_node = self.DFS(start, visited)

        visited = [False] * (max(self.graph.keys()) + 1)
        diameter, _ = self.DFS(farthest_node, visited)

        return diameter, visited

    def diameterOfForest(self):
        visited = [False] * (max(self.graph.keys()) + 1)
        diameters = []

        for v in self.graph:
            if not visited[v]:
                diameter, vis = self.diameterOfTree(v)
                for i, x in enumerate(vis):
                    visited[i] = visited[i] or x
                diameters.append(diameter)

        return diameters


def cal_diameter(file):
    g = Graph()
    with open('../../output/auto/instructions/' + file, 'r') as f:
        data = json.load(f)

    argument_map = {}
    for i, d in enumerate(data):
        sentence = list(d.keys())[0]
        if isinstance(d[sentence], str):
            continue
        instruction = list(d[sentence].keys())[0]

        if "emit" not in d[sentence][instruction]:
            continue
        key = list(d[sentence][instruction]["emit"].keys())[0]
        argument_map[d[sentence][instruction]["emit"][key]] = i + 1

    for i, d in enumerate(data):
        sentence = list(d.keys())[0]
        if isinstance(d[sentence], str):
            continue
        instruction = list(d[sentence].keys())[0]

        if "slot" not in d[sentence][instruction]:
            continue
        key = list(d[sentence][instruction]["slot"].keys())
        for k in key:
            if isinstance(d[sentence][instruction]["slot"][k], list):
                for j in d[sentence][instruction]["slot"][k]:
                    if j in argument_map:
                        g.addEdge(i + 1, argument_map[j])
            elif isinstance(d[sentence][instruction]["slot"][k], str):
                if d[sentence][instruction]["slot"][k] in argument_map:
                    g.addEdge(i + 1, argument_map[d[sentence][instruction]["slot"][k]])

    print("File: " + file + "\nDiameter of the given forest is " + str(g.diameterOfForest()) + "\n")


# 使用上述类计算一个树的直径
if __name__ == '__main__':

    files = []
    for root, ds, fs in os.walk("../../output/auto/archive_4/"):
        files.extend(fs)

    for file in files:
        cal_diameter(file)
