#1초 = 1,000,000,000 (10억)

#DFS, O(N)
def dfs(gragh, start, visited):
    visited[start] = True
    for v in gragh[start] :
        #여기서 뭔가를 더 할 수 있음
        if not visited[v] :
            bfs(gragh, v, visited)


#BFS, O(N)
#DFS보다 빠른 탐색
from collections import deque
def bfs(gragh, start, visited):
    queue = deque([start])
    visited[start]= True
    while queue:
        v = queue.popleft()
        #여기서 뭔가를 더 할 수 있음
        for i in gragh[v]:
            if not visited[i] :
                queue.append(i)
                visited[i] = True

#선택정렬, O(N**2)
array = []
for i in range(len(array)) :
    min_index = i
    for j in range(1, i+1) :
        if array[min_index] > array[j] :
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

#삽입정렬, O(N**2)
for i in range(1, len(array)):
    for j in range(i, 0, -1) :
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]
        else :
            break

#퀵 정렬, O(NlogN)            
def q(array):
    if len(array) <= 1 :
        return array
    pivot = array[0] #피벗은 첫 번째 원소
    tail = array[1:] #피벗을 제외한 리스트
    left_side = [x for x in tail if x <=pivot]
    right_side = [x for x in tail if x > pivot]
    
    return q(left_side) + [pivot] +q(right_side)

        

