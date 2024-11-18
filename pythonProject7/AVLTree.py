from BinaryTree import *
from BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)

# 코드 9.14: AVL 트리의 LL회전
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

# 코드 9.15: AVL 트리의 RR회전
def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")



from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# AVL 트리의 삭제 연산
def delete_avl(parent, key):
    if parent is None:
        return None

    # 키를 기준으로 삭제할 노드 탐색
    if key < parent.key:
        parent.left = delete_avl(parent.left, key)
    elif key > parent.key:
        parent.right = delete_avl(parent.right, key)
    else:  # 삭제할 노드 발견
        if parent.left is None:  # 오른쪽 자식만 있거나 리프 노드인 경우
            return parent.right
        elif parent.right is None:  # 왼쪽 자식만 있는 경우
            return parent.left
        else:  # 두 자식이 있는 경우
            # 오른쪽 서브트리에서 가장 작은 노드를 찾아 교체
            min_larger_node = find_min(parent.right)
            parent.key = min_larger_node.key
            # 대체한 노드를 삭제
            parent.right = delete_avl(parent.right, min_larger_node.key)

    # 삭제 후 재균형 수행
    return reBalance(parent)

# 오른쪽 서브트리에서 최소값 노드 찾기 함수
def find_min(node):
    while node.left is not None:
        node = node.left
    return node

# AVL 트리 테스트 프로그램 (삭제 추가)
if __name__ == "__main__":
    node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    root = None
    for i in node:
        n = BSTNode(i)
        if root is None:
            root = n
        else:
            root = insert_avl(root, n)
        print("AVL(%d): " % i, end='')
        levelorder(root)
        print()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))

    # 삭제 연산 테스트
    delete_keys = [3, 7, 8]  # 삭제할 키 목록
    for key in delete_keys:
        print(f"\n키 {key} 삭제 후:")
        root = delete_avl(root, key)
        print("AVL: ", end='')
        levelorder(root)
        print()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))



