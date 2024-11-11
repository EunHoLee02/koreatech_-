from ArrayList import ArrayList

# 배열구조의 리스트를 이용한 라인 편집기 프로그램
list = ArrayList(1000)
while True :
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=> ")

    if command == 'i' :
        pos = int( input("  입력행 번호: ") )
        str = input("  입력행 내용: ")
        list.insert(pos, str)

    elif command == 'd' :
        pos = int( input("  삭제행 번호: ") )
        list.delete(pos)

    elif command == 'r' :
        pos = int( input("  변경행 번호: ") )
        str = input("  변경행 내용: ");
        list.replace(pos, str)

    elif command == 'p' :
        print('Line Editor')
        for line in range (list.size) :
            print('[%2d] '%line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q' : exit()

    elif command == 'l' :
        # filename = input("  읽어들일 파일 이름: ")
        filename = 'test.txt'
        infile = open(filename , "r")
        lines = infile.readlines();
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()

    elif command == 's' :
        # filename = input("  저장할 파일 이름: ")
        filename = 'test.txt'
        outfile = open(filename , "w")
        len = list.size
        for i in range(len) :
            outfile.write(list.getEntry(i)+'\n')
        outfile.close()
    elif command == 'm':
        word_count = {}
        for i in range(list.size):
            words = list.getEntry(i).split()  # 공백을 기준으로 단어 분리
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        filename = 'dic.txt'
        with open(filename, "w") as outfile:
            for word, count in word_count.items():
                outfile.write(f"{word}: {count}\n")

        # dic.txt 파일에 있는 내용을 출력
        print("\n[dic.txt 파일 출력]")
        with open(filename, "r") as infile:
            print(infile.read())


