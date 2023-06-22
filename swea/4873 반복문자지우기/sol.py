import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    S = list(map(str,input()))
    stack = []
    for i in range(len(S)):
        if len(stack) == 0:
            stack.append(S[i])
        else:
            if S[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(S[i])
    print(f'{tc} {len(stack)}')