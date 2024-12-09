from queue import Queue
from collections import deque

def printStep(arr, val) :
    print("step%2d " % val, end='')
    print(arr)


# 코드 12.12: 기수 정렬
def radix_sort(A) :
    comparisons = 0
    movements = 0
    queues = []
    BUCKETS = 10
    max_value = max(A)
    DIGITS=len(str(max_value))
    for i in range(BUCKETS) :
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS) :
        for i in range(n) : 	            # 자릿수에 따라 큐에 삽입
            queues[(A[i]//factor) % BUCKETS].put(A[i])
            movements += 1
        i = 0
        for b in range(BUCKETS) :		    # 버킷에서 꺼내어 list로 합친다.
            while not queues[b].empty() :
                A[i] = queues[b].get()
                movements += 1
                i += 1
        factor *= 10					    # 그 다음 자리수로 간다.
        printStep(A, d + 1)			        # 중간 과정 출력용 문장
    return comparisons,movements

# 코드 12.13: 기수 정렬 테스트 프로그램




