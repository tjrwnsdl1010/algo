import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N : 화덕크기, M : 피자갯수
    N, M = list(map(int, input().split()))
    # 피자에 올려진 치즈 갯수
    cheeze = list(map(int, input().split()))

    # 완성전 피자 (피자 넘버링과정)
    before = []
    for i in range(M):
        before.append([cheeze[i], i])

    # 비어있는 화덕 생성
    queue = [0] * N

    # 완성된 피자
    after = []

    # 완성된 피자가 만들어야 하는 피자 갯수랑 같아질때까지
    while len(after) != M:

        # 화덕 입구에 공간이 비었다면
        if queue[0] == 0:
            # 넣을피자가 있는지 확인
            if len(before) != 0:
                # c : 초기 치즈값 / i : 피자 번호
                c, i = before.pop(0)
                # 피자를 화덕에 넣기
                queue.append([c, i])
                # 화덕 돌리기
                queue.pop(0)
            # 넣을피자가 없다면 화덕 돌리기
            else:
                queue.pop(0)
                queue.append(0)
        # 입구에 피자가 있는경우 (피자를 넣을 공간이 없는경우)
        else:
            # 치즈 절반 감소
            queue[0][0] //= 2

            # 현재 다 완성된 피자인지 확인
            if queue[0][0] == 0:
                # 완성된 피자 꺼내기
                pizza = queue.pop(0)
                # 완성 리스트에 피자 번호 추가
                after.append(pizza[1])

                # 넣을피자 있는지 확인
                if len(before) != 0:
                    # 남은 첫번째 피자 (c:초기치즈, i:피자번호)
                    c, i = before.pop(0)
                    # 화덕에 넣기
                    queue.append([c, i])
                else:
                    queue.append(0)
            # 아직 완성되지 않은 피자라면
            else:
                # 아직 완성되지 않은 피자를 제일 뒤로 돌려주기
                pi = queue.pop(0)
                queue.append(pi)

    print(after)
      