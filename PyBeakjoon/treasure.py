'''
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.


예제 입력 1 
5
1 1 1 6 0
2 7 8 3 1
예제 출력 1 
18

예제 입력 2 
3
1 1 3
10 30 20
예제 출력 2 
80

예제 입력 3 
9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1
예제 출력 3 
528


'''
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(key=None, reverse=True)
B.sort(key=None, reverse=False)

print(sum(map(lambda x : x[0] * x[1], zip(A, B))))


