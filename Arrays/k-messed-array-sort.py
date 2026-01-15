from typing import List

'''
input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2
output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

heap : 1, 4, 5
for x in range(1,k+1):
    lis.append(i-x)

[i-k, i-2, i-1, i, i+1, i+2, i+3]

N*logN 
heaps

1 2 3 4 5 6 7 [8, 10, 9]
'''
import heapq

def sort_k_messed_array(arr: List[int], k: int) -> List[int]:
    
    temp = arr[0:k+1] # 5, 4, 1
    sorted_arr = []
    heapq.heapify(temp) # min heap
    for i in range(k+1, len(arr)):     
        sorted_arr.append(heapq.heappop(temp))
        heapq.heappush(temp, arr[i]) # insert element

        # heapq.heappop(list_name) # pops smallest
    
    while temp:
        sorted_arr.append(heapq.heappop(temp))
    
    return sorted_arr

# NlogN > NlogK using a heap

"""
[1, 4, 5, 2, 3, 7, 8, 6, 10, 9] 
temp: [ 8, 10, 9]
k = 4
sorted_arr: [1, 2, 3, 4, 5, 6, 7]
arr[i] = 9

  
# debug your code below
print(sort_k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))
"""
