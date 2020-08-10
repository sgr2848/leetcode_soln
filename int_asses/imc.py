'''
 If  A  has buried artifacts underground.THey are hidden in area in NxN grid of square cell.The row are numbered 1 to N The columns are labeled with consecutive English upper-case letters (A, B, C, etc.). Each cell is identified by a string Composed of its row number followed by its column number: for example, "9C" denotes the third cell in the 9th row, and "150" denotes the fourth cell in the 15th row.
 
 B was out looking for the artifact pieces in this area. He chose some map cells in which to Search for artifacto pieces. He is able to reconstruct an artifact if he found all of the pieces of an artifact.
 
 The goal is to count the number of artifacts for which he has found all of the pieces, as well the number of artifacts for which he's found some but not all of the pieces,

 A hid the pieces of each artifact in adjacent cells of an area that is rectangular in shape and no larger than 4 cells in area, with at most one piece in each cell. The locations of the artifacts are given as a string artifacts, containing pairs of positions describing respectively the top-left and þottom-right corner cells where pieces of an artifact is buried. The artifacts' locations are Separated by a comma. 

 For example for the following input artifacts = "18 20,20 40", N = 4, the artifact pieces are as shown below (labeled with 1s and 2s) А B D Test Output 
 
 The coordinates where B searched are given as a string searched, containing positions pescribing the map cells where he searched for the map in the example shown above and searched - 2B 2D 3D 4D AA", he will have found artifact pieces in the cells marked with x and found nothing in the cells marked with 0.

 Assume that: 
 •is an integer within the range [1..26]; 
 •string artifacts contains the descriptions of rectangular areas where artifacts are buried, no greater than 4 cells in size,
 • there can be at most one piece located on any map cell; each map cell can appear in string searched at most once; 
 • string artifacts and string searched contains only valid positions given in specified format in your solution, 
'''
import re
import string
def solution(N, artifacts, searched):
    #keeping a hashmap of alphabet with value as nums to grab the index 
    alpha_list = list(string.ascii_uppercase)
    alpha_map ={}
    exists=[]
    for i in range(N):
        alpha_map[alpha_list[i]] = i
    artifact_list= [i.split(" ")for i in artifacts.split(",")]
    search_list = searched.split(" ")
    arti_map = {}
    index_search = []
    count = 1
    return_list =[]
    for i in artifact_list:
        arti_number = []
        for j in i:
            current_ind = list(j)                               
            actual_ind = [int(current_ind[0])-1,alpha_map[current_ind[1]]]
            arti_number.append(actual_ind)
            if [actual_ind[0]+1,actual_ind[1]] not in exists and actual_ind[0]+1 < N:
                arti_number.append([actual_ind[0]+1,actual_ind[1]])
            elif [actual_ind[0]-1,actual_ind[1]] not in exists and actual_ind[0]-1 < N and actual_ind[0]-1 >0:
                arti_number.append([actual_ind[0]-1,actual_ind[1]])
            elif [actual_ind[0],actual_ind[1]+1] not in exists and actual_ind[1]+1 < N:
                arti_number.append([actual_ind[0],actual_ind[1]+1])
            elif [actual_ind[0]-1,actual_ind[1]] not in exists and actual_ind[1]+1 < N and actual_ind[1]-1 >0:
                arti_number.append([actual_ind[0],actual_ind[1]-1])
        arti_map[count] = arti_number 
        arti_number= []
        count+=1
    for k in search_list:
        current_index = list(k)
        index_search.append([int(current_ind[0])-1,alpha_map[current_ind[1]]])
    for i in arti_map.values():
        contains = len(i)
        for j in index_search:
            if j in i:
                contains += 1
        if contains == 4:
            return_list.append(1)
        else:
            return_list.append(0)
        
    return return_list
solution(4, '1B 2C,2D 4D', '2B 2D 3D 4D 4A')
