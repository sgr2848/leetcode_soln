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
    pass-
    