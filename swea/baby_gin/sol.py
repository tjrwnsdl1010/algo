import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    counter = [0 for i in range(10)]
    numbers = list(map(int,input()))
    is_babygin = 0
    
    for number in numbers:
        counter[number]+=1

    idx = 0
    while idx < len(counter):
        # 1 triplet 검증
        if counter[idx] >= 3:
            is_babygin += 1
            counter[idx] -= 3
            continue
            

        # 2 run 검증
        if idx < len(counter) -2 :
        
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                is_babygin +=1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                continue

        idx += 1


    if is_babygin == 2:
        result = True
    else :
        result  = False
   
    print(f'#{tc} {result}')