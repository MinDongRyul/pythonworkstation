from itertools import combinations 
# 조합 : 서로 다른 n개에서 순서에 상관없이 다른 r개를 선택하는 것

# from intertools import permutations
# 순열 : 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것 

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())
# 가능한 암호를 사전식으로 출력하여 하므로 입력 이후에 정력
data = input().split(' ')
data.sort()

# 길이가 L인 모든 암호 조합을 확인
for password in combinations(data, l):
    # 패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    # 최소 1개의 모음과 2개의 자음이 있는 경우를 출력
    if count >= 1 and count <= l - 2:
        print(''.join(password))