from collections import deque
def bfs(G,i):
    v=len(G)
    q=deque()
    q.append(i)
    visited=[False for i in range(v)]
    visited[i]=True
    vis=1
    while q:
        u=q.popleft()
        for e in G[u]:
            if not visited[e]:
                vis += 1
                visited[e] = True
                q.append(e)
    if vis==v: return True
    return False
def goodStart(G):
    for i in range(len(G)):
        if bfs(G,i):
            return True
    return False

G=[[3],[4],[0,3],[1],[]]
print(goodStart(G))
