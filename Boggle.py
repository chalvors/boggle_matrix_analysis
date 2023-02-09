# Cole Halvorson
# Boggle.py
# analyzes boggle board from image and returns valid words
# ONLY WORKS WITH SQUARE ARRAYS (2X2, 3X3, 4X4, ...)

import sys
import json
import time
from OCR import analyzeImage, boardSize
from _thread import start_new_thread


# initialize dictionary from json file
def initDictionary():
    f = open('dictionary.json', 'r')
    data = json.load(f)
    f.close()

    for word in data:    # remove all words less than 3 chars, capitalize
        if (len(word) > 2):
            dictionary.append(word.upper())

# Binary Search Function
def binarySearch(Str, low, high, arr):
    if high >= low:
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == Str:
            return True
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > Str:
            return binarySearch(Str, low, mid - 1, arr)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearch(Str, mid + 1, high, arr)
 
    else:
        # Element is not present in the array
        return False
 
# A recursive function to print all words present on boggle
def findWordsUtil(boggle, visited, i, j, Str, size):
    # Mark current cell as visited and
    # append current character to str
    visited[i][j] = True
    Str = Str + boggle[i][j]

    # if string has not already been found and is in dictionary 
    # add to list of found words
    # sort found for binary search
    if not(binarySearch(Str, 0, len(found) - 1, found)) and ((binarySearch(Str, 0, len(dictionary) - 1, dictionary))):     
        found.append(Str)
        found.sort()                                                        
     
    # Traverse 8 adjacent cells of boggle[i,j]
    row = i - 1
    while row <= i + 1 and row < size:
        col = j - 1
        while col <= j + 1 and col < size:
            if (row >= 0 and col >= 0 and not visited[row][col]):
                findWordsUtil(boggle, visited, row, col, Str, size)
            col+=1
        row+=1
     
    # Erase current character from string and
    # mark visited of current cell as false
    Str = "" + Str[-1]
    visited[i][j] = False
 
# find strings in board
def findWords(boggle, size):
   
    # Mark all characters as not visited
    visited = [[False for i in range(size)] for j in range(size)]
     
    # Initialize current string
    Str = ""
     
    # Consider every character and look for all words
    # starting with this character
    for i in range(size):
      for j in range(size):
        findWordsUtil(boggle, visited, i, j, Str, size)
 
# print found words
def printFound():
    elapsedTime = str(time.time() - startTime)
    numWords = str(len(found))

    print('found ' + numWords + ' words in ' + elapsedTime + ' seconds:')

    for word in found:                 # print found words
        print(word)                  

# print board
def printBoard(board, size):
    print('OCR recognized ' + str(size) + 'x' + str(size) + ' board:')
    print('')
    
    for row in board:
        print(row)

    print('')

# sort found list by string length, longest first
def sortFound():
    found.sort(key=len, reverse=True)                    

# print loading message
def printLoading(): 
    while True:
        for x in range(0,4):
            b = 'analyzing, please wait' + ' .' * x
            print(b, end='\r')
            time.sleep(1)

        sys.stdout.write('\x1b[2K')

# --------------------------------------------------------------------------------------------------
# Driver Code
# --------------------------------------------------------------------------------------------------
startTime = time.time()

dictionary = []
found = []
board = []

img = 'images/4x4.jpg'

initDictionary()
analyzeImage(img, board)
printBoard(board, boardSize(img))
start_new_thread(printLoading, ())
findWords(board, boardSize(img))
sortFound()
printFound()

