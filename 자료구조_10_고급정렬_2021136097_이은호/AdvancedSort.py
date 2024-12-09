from RadixSort import radix_sort
from ShellSort import shell_sort
from HeapSort import heap_sort
from mergeSort import merge_sort
from QuickSort import quick_sort

# Selection Sort
def selection_sort(A):
    n = len(A)
    comparisons, movements = 0, 0
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            comparisons += 1
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        movements += 2
    return comparisons, movements

# Insertion Sort
def insertion_sort(A):
    n = len(A)
    comparisons, movements = 0, 0
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            comparisons += 1
            A[j + 1] = A[j]
            movements += 1
            j -= 1
        A[j + 1] = key
        movements += 1
    return comparisons, movements

# Bubble Sort
def bubble_sort(A):
    n = len(A)
    comparisons, movements = 0, 0
    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            comparisons += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                movements += 2
                bChanged = True
        if not bChanged:
            break
    return comparisons, movements

# 결과 출력 함수
def display_result(algorithm, data, comparisons, movements):
    print(f"\n>> Algorithm: {algorithm}")
    print(f"Sorted Data: {data}")
    print(f">> Number of Comparisons: {comparisons}")
    print(f">> Number of Data Movements: {movements}")

# 메인 프로그램
def main():
    print("Target Sorting Algorithm List")
    print("Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE),")
    print("Heap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")

    data = list(map(int, input("\n* Please input a data list ex) 5, 8, 1, 3, 4: ").split(',')))
    algorithm = input("\n* Select sorting algorithm: ").strip().upper()

    sorted_temp = [0] * len(data)
    comparisons, movements = 0, 0

    if algorithm == "SEL":
        comparisons, movements = selection_sort(data)
    elif algorithm == "INS":
        comparisons, movements = insertion_sort(data)
    elif algorithm == "BUB":
        comparisons, movements = bubble_sort(data)
    elif algorithm == "SHE":
        comparisons, movements = shell_sort(data)  # ShellSort.py에서 가져옴
    elif algorithm == "HEA":
        comparisons, movements = heap_sort(data)  # HeapSort.py에서 가져옴
    elif algorithm == "MER":
        comparisons, movements = merge_sort(data, 0, len(data) - 1,sorted_temp)  # mergeSort.py에서 가져옴
    elif algorithm == "QUI":
         comparisons, movements = quick_sort(data)  # QuickSort.py에서 가져옴
    elif algorithm == "RAD":
        comparisons, movements = radix_sort(data)  # RadixSort.py에서 가져옴
    else:
        print("Invalid algorithm choice.")
        return

    # 결과 출력
    display_result(algorithm, data, comparisons, movements)

if __name__ == "__main__":
    main()
