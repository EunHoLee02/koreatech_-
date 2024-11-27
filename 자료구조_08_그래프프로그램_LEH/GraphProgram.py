# 그래프 표현 및 탐색 알고리즘  
from BFS import BFS_AL
from DFS import DFS
from CC_DFS import find_connected_component
from ST_DFS import ST_DFS

# 주어진 이미지에 기반한 그래프 데이터
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjList = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 5], [2, 6, 7], [3], [4, 7], [4, 6]]
adjMat = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

# 깊이 우선 탐색 (DFS)
print("깊이 우선 탐색 (DFS) 시작:")
visited_dfs = [False] * len(vertex)
dfs_result = []
DFS(vertex, adjMat, 0, visited_dfs)
for i in range(len(visited_dfs)):
    if visited_dfs[i]:
        print(f"방문: {vertex[i]}")
        dfs_result.append(vertex[i])
print('DFS 결과:', ' - '.join(dfs_result))

# 너비 우선 탐색 (BFS)
print("\n너비 우선 탐색 (BFS) 시작:")
# BFS_AL 함수 내부에서 방문한 노드들을 리스트로 반환하도록 보장합니다.
bfs_result = BFS_AL(vertex, adjList, 0)
if bfs_result is None:
    bfs_result = []
if bfs_result:
    for node in bfs_result:
        print(f"방문: {node}")
    print('BFS 결과:', ' - '.join(bfs_result))
else:
    print('BFS 결과가 없습니다.')

# 연결 성분 찾기
print("\n연결 성분 찾기:")
connected_components = find_connected_component(vertex, adjMat)
for i, component in enumerate(connected_components):
    component_names = [vertex[idx] for idx in component]
    print(f"연결 성분 {i + 1}: {component_names}")
connected_components_names = [[vertex[idx] for idx in component] for component in connected_components]
print('연결 성분 (BFS):', connected_components_names)

# DFS를 이용한 신장 트리 구성
print("\n깊이 우선 탐색을 이용한 신장 트리 구성:")
visited_st = [False] * len(vertex)
# ST_DFS 함수에서 방문한 간선들을 리스트로 반환하도록 보장합니다.
spanning_tree_edges = []
ST_DFS(vertex, adjMat, 0, visited_st)
for i in range(len(visited_st)):
    if visited_st[i]:
        for j in range(len(vertex)):
            if adjMat[i][j] != 0 and visited_st[j]:
                spanning_tree_edges.append((vertex[i], vertex[j]))
if spanning_tree_edges:
    for edge in spanning_tree_edges:
        print(f"신장 트리의 간선: {edge}")
    print('신장 트리 (DFS):', spanning_tree_edges)
else:
    print('신장 트리 결과가 없습니다.')
