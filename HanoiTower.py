import time
count = 0
def hanoi_tower(n,fr,tmp,to) :
    global count
    count += 1
    if(n==1):
        print("원판 1 : %s --> %s"%(fr,to))
    else :
        hanoi_tower(n-1,fr,to,tmp)
        print("원판 %d: %s --> %s"%(n,fr,to))
        hanoi_tower(n-1,tmp,fr,to)
n = int(input("탑의 최대 층수를 입력하세요 : "))
start = time.time()
hanoi_tower(n,'A','B','C')
end = time.time()
print("실행시간 : ",end-start)
print("함수 호출 횟수 : ",count)