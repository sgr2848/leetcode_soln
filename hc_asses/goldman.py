# Suppose, we have an array 1 2 1 2 1 3. The Sum of first three elements is 1 + 2 + 1 = 4 and sum of last three elements is 2 + 1 + 3 = 6
from itertools import combinations
def balancedSum(arr):
    n = len(arr)
    total_sum = sum(arr)
    current_ = arr[0]
    for i in range(1, n):
        if (current_ == total_sum - current_ - arr[i]):
            return i
        current_ += arr[i]
    return 0
# find the total number of unique palindrome sub-string in a given string
# ex : for string mokkori, the output should be 7
# explanation : [m,o,k,r,i,kk,okko]
def palindrome(s):
    pal_set = set()     
    for i in range(len(s)):
        nor = rev = ''
        for j in range(i, len(s)):
            nor = nor + s[j]
            rev = s[j] + rev
            if (rev == nor):
                pal_set.add(nor)
    return len(pal_set)
#another apporach
def palindrome_second(s):
    sub_strs = set([s[x:y] for x, y in combinations(
        range(len(s) + 1), r=2)])
    count = 0
    for i in sub_strs:
        if i.lower() == i[::-1].lower():
            count += 1
    return count

palindrome_second("mokkori")
