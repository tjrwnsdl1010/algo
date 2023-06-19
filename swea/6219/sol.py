number = int(input())

count = 0

for i in range(1, number+1):
    if number % 1 == 0:
        print(f"약수입니다")
        count += 1

if count == 2:
    print("소수입니다")