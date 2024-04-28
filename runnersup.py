import math
import sys
n = int(input())
arr =list(map(int, input().split()))
arr =  [i for i in arr if i != max(arr)]
print(max(arr))
