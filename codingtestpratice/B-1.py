import math
n, m = map(int, input().split())

array = [True for i in range(m + 1)]
array[1] = 0 # 1은 소수가 아님

for i in range(2, int(math.sqrt(m)) + 1): # 2부터 m의 제곱근까지의 모든 수를 확인
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        j = 2
        while i * j <= m:
            array[i * j] = False
            j += 1

for i in range(n, m + 1): # n부터 m까지의 모든 소수 출력 
    if array[i]:
        print(i)

  
    
