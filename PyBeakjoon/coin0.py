'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

N = 10
K = 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''
# N = 10
# K = 4790
# haveCoin = [1,5,10,50,100,500,1000,5000,10000,50000]
N, K = list(map(int, input().split()))
haveCoin = [int(input()) for _ in range(0, N)]
coinCnt = 0

for i in reversed(haveCoin):
    a = int(K) // i
    coinCnt += a
    K -= a * i
print(coinCnt)            


        
        
        
        