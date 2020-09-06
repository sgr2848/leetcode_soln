#No. 1 Is unique
def isUnique(some_string):
    #keep a hashmap to keep count of char in string
    char_map = {}
    string_list = [i for i in some_string]
    for i in string_list:
        if i in char_map:
            return False
        else:
            char_map[i] = True
#No. 2 Check Permutation
# Given two string check if one is permutation of another one
def isPermutation(string_a, string_b):    
    try:
        assert (len(string_a) == len(string_b))
    except:
        return False
    string_a = string_a.lower()
    string_b = string_b.lower()
    sorted_str_a = "".join(sorted(list(string_a)))
    sorted_str_b = "".join(sorted(list(string_b)))
    if sorted_str_b == sorted_str_a:
        return True
    else:
        return False
# print(isPermutation('hello', 'ehlli'))
#No 3
def urlify(some_string):
    return "%20".join(list(filter(None, some_string.split(" "))))

#Given a string write a function to check if it is a permutation of a palindrome (doesn't need to be a valid word)
# input types tacocoa -> True
#No 4
 
def isPalindromePermutation(some_string: str) -> bool:
    map = {}    
    some_string = "".join(list(some_string.lower().split(" ")))    
    odd = 0 
    for i in some_string:
        if i in map.keys():
            map[i] += 1
        else:
            map[i] = 1
    print(map)
    for i in map.keys():
        if map[i] % 2 != 0:
            odd += 1
            if odd >= 2:
                return False
            else:
                pass
        else:
            pass
    return True

# print(isPalindromePermutation("Tact Coa"))
# print(isPalindromePermutation("aa b"))\
# No 6
def string_compression(some_string):
    map = {}
    for i in some_string:
        if i in map.keys():
            map[i] += 1
        else:
            map[i] = 1
        
    return_string = "".join(list(f'{key}{value}' for key, value in map.items()))
    if len(some_string) <= len(return_string):
        return some_string
    else:
        return return_string
print(string_compression("aaabbddde"))
#No 7
def rotateMatrix(matrix):
    rex = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
    return rex

def rotateMatrixInplace(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            a = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = a
matrix = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
print(matrix)
matrix = rotateMatrix(matrix)
print(matrix)
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
print(matrix)
rotateMatrixInplace(matrix)
print(matrix)
#No 8
def zero_matrix(m, n):
    return [[0.]*m]*n
print(zero_matrix(5,6))
