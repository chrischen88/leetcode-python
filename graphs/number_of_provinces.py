from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    visited = [False] * len(isConnected)
    num_prov = 0
    for i in range(len(visited)):
        if not visited[i]:
            queue = [i]
            visited[i] = True
            while queue:
                cur = queue.pop(0)
                for j in range(len(isConnected)):
                    if not visited[j] and isConnected[cur][j] == 1:
                        queue.append(j)
                        visited[j] = True
            num_prov += 1
    return num_prov