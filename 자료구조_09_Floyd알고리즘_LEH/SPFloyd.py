# 코드 11.16: Floyd 알고리즘 수정
INF = 9999
def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if A[i][j] == INF:
                print(" INF ", end='')
            else:
                print("%4d " % A[i][j], end='')
        print("")

def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)  # 정점의 개수

    A = list(adj)  # 2차원 배열(리스트의 리스트)의 복사
    for i in range(vsize):
        A[i] = list(adj[i])

    path = [[-1] * vsize for _ in range(vsize)]  # 경로 추적을 위한 리스트

    for i in range(vsize):
        for j in range(vsize):
            if adj[i][j] != INF and i != j:
                path[i][j] = i

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = path[k][j]
        printA(A)  # 진행상황 출력용

    return A, path

def print_path(path, start, end, vertex):
    if path[start][end] == -1:
        print("경로가 존재하지 않습니다.")
        return
    result = []
    while end != start:
        result.append(end)
        end = path[start][end]
    result.append(start)
    result.reverse()
    print(" * 최단 경로 : ", " -> ".join(vertex[i] for i in result))

if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0, 7, INF, INF, 3, 10, INF],
        [7, 0, 4, 10, 2, 6, INF],
        [INF, 4, 0, 2, INF, INF, INF],
        [INF, 10, 2, 0, 11, 9, 4],
        [3, 2, INF, 11, 0, 13, 5],
        [10, 6, INF, 9, 13, 0, INF],
        [INF, INF, INF, 4, 5, INF, 0]
    ]

    print("Floyd 알고리즘에 의한 최단 경로")
    start_vertex = input("시작 정점: ").strip().upper()
    end_vertex = input("종료 정점: ").strip().upper()

    if start_vertex in vertex and end_vertex in vertex:
        start = vertex.index(start_vertex)
        end = vertex.index(end_vertex)

        A, path = shortest_path_floyd(vertex, weight)
        print(" * 최단 경로의 거리: ", A[start][end])
        print_path(path, start, end, vertex)
    else:
        print("입력한 정점이 그래프에 없습니다.")
