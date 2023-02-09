# Cole Halvorson
# OCR.py
# OCR functions for Boggle.py

import numpy as np
from PIL import Image
import pytesseract


# populate board with OCR text
def fillBoard(board, splitText):
    row = []

    for str in splitText:
        for char in str:
            row.append(char)

        board.append(row)
        row = []
            
# determine size of board based on what ocr returns
def boardSize(filename):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    splitText = text.split()

    return len(splitText)

# convert image to array
def analyzeImage(filename, board):

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    splitText = text.split()
    boardWidth = len(splitText)

    fillBoard(board, splitText)
    checkBoard(board, boardWidth)

# print board out
def printBoard(board):
    for row in board:
        print(row)

# check board for propper number of cells
def checkBoard(board, boardWidth):
    expectedSize = boardWidth * boardWidth    # num chars expected in the board
    count = 0

    for row in board:
        for char in row:
            count += 1

    if count != expectedSize:
        print('number of cells found:    ' + str(count))
        print('number of cells expected: ' + str(expectedSize))
        print('board found: ')
        printBoard(board)
        exit(1)

        