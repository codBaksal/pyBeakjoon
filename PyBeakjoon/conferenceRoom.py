'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

첫줄에 회의 수
다음부터 회의 시간

13
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 8
8 9
8 11
8 12
2 13
12 14

출력
4
# confer = int(input())
# runTime = [tuple(map(int, input().split())) for _ in range(confer)]
# confer = 11
# runTime = [[1,4],[3,5],[0,6],[5,7],[3,8],[5,9],[6,10],[8,12],[8,12],[2,13],[12,14]]
'''
import sys

inputSys = sys.stdin.readline

conferAllCount = int(input())
conferTime = [(*map(int, input().split()),) for _ in range(conferAllCount)]
print(conferTime)
resultConCnt = 0
eachEndTime = 0

conferTime.sort(key=lambda x : x[0], reverse=False)
conferTime.sort(key=lambda x : x[1], reverse=False)

for i, j in conferTime:
    if i >= eachEndTime:
        resultConCnt += 1
        eachEndTime = j
print(resultConCnt)
        
# runTime = sorted(runTime, key=lambda x : (x[1],[0]), reverse=False)
# lastTime,count = 0, 0
# for i,j in runTime:
#     print(i,j)
#     if i >= lastTime:
#         count += 1
#         lastTime = j
# print(count)      
        

