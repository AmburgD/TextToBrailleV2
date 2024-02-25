# https://docs.google.com/presentation/d/1s_8gcGfFDEHnqS7U-TkC4xp9T49fblb2_EWRpsd-v_I/edit#slide=id.g7d81a7112a_0_5
# https://github.com/colbrydi/Lithophane/blob/master/README.md

# pip install
#   numpy-stl
#   pillow
#   PyQt5

from math import ceil
from numpy import char
import lithophane as LI
from PIL import Image, ImageDraw, ImageFont, ImageOps
from PyQt5.QtWidgets import QApplication
import sys
import os

#all of our characters

a = [
    ['•', ' '],
    [' ', ' '],
    [' ', ' ']
]

b = [
    ['•', ' '],
    ['•', ' '],
    [' ', ' ']
]

c = [
    ['•', '•'],
    [' ', ' '],
    [' ', ' ']
]

d = [
    ['•', '•'],
    [' ', '•'],
    [' ', ' ']
]

e = [
    ['•', ' '],
    [' ', '•'],
    [' ', ' ']
]

f = [
    ['•', '•'],
    ['•', ' '],
    [' ', ' ']
]

g = [
    ['•', '•'],
    ['•', '•'],
    [' ', ' ']
]

h = [
    ['•', ' '],
    ['•', '•'],
    [' ', ' ']
]

i = [
    [' ', '•'],
    ['•', ' '],
    [' ', ' ']
]

j = [
    [' ', '•'],
    ['•', '•'],
    [' ', ' ']
]

k = [
    ['•', ' '],
    [' ', ' '],
    ['•', ' ']
]

l = [
    ['•', ' '],
    ['•', ' '],
    ['•', ' ']
]

m = [
    ['•', '•'],
    [' ', ' '],
    ['•', ' ']
]

n = [
    ['•', '•'],
    [' ', '•'],
    ['•', ' ']
]

o = [
    ['•', ' '],
    [' ', '•'],
    ['•', ' ']
]

p = [
    ['•', '•'],
    ['•', ' '],
    ['•', ' ']
]

q = [
    ['•', '•'],
    ['•', '•'],
    ['•', ' ']
]

r = [
    ['•', ' '],
    ['•', '•'],
    ['•', ' ']
]

s = [
    [' ', '•'],
    ['•', ' '],
    ['•', ' ']
]

t = [
    [' ', '•'],
    ['•', '•'],
    ['•', ' ']
]

u = [
    ['•', ' '],
    [' ', ' '],
    ['•', '•']
]

v = [
    ['•', ' '],
    ['•', ' '],
    ['•', '•']
]

w = [
    [' ', '•'],
    ['•', '•'],
    [' ', '•']
]

x = [
    ['•', '•'],
    [' ', ' '],
    ['•', '•']
]

y = [
    ['•', '•'],
    [' ', '•'],
    ['•', '•']
]

z = [
    ['•', ' '],
    [' ', '•'],
    ['•', '•']
]

capital_letter = [
    [' ', ' '],
    [' ', ' '],
    [' ', '•']
]

period = [
    [' ', ' '],
    ['•', '•'],
    [' ', '•']
]

question_mark = [
    [' ', ' '],
    ['•', ' '],
    ['•', '•']
]

exclamation_mark = [
    [' ', ' '],
    ['•', '•'],
    ['•', ' ']
]

comma = [
    [' ', ' '],
    ['•', ' '],
    [' ', ' ']
]

number_sign = [
    [' ', '•'],
    [' ', '•'],
    ['•', '•']
]

space = [
    [' ', ' '],
    [' ', ' '],
    [' ', ' ']
]

# Initialize empty strings for each line
lineOne: str = ""
lineTwo: str = ""
lineThree: str = ""

def displayChar(character, row, col):
    """ Display a 2 by 3 2d array

    Args:
        character (_type_): the 2 by 3 2d array
        row (_type_): an integer of the number of rows in the 2d array
        col (_type_): an integer of the number of columns in the 2d array

    Returns:
        _type_: three strings that each represent a row of the 2d array
    """
    # Referencing the global variables
    global lineOne
    global lineTwo
    global lineThree

    # Using / or \ in the algorithm causes a filepath reveal. For security,
    # adding a case to abort program if the slash is discovered 
    if char == "/" or char == "\\":
        sys.exit

    # Run through each row of the array
    for i in range(row):
        # For each row, concatenate the characters into the respective lines
        for j in range(col):
            if i == 0:
                lineOne += character[i][j]
            elif i == 1:
                lineTwo += character[i][j]
            elif i == 2:
                lineThree += character[i][j]
    # Add a space in-between each character if it isnt a space
    if character != ' ':
        lineOne += " "
        lineTwo += " "
        lineThree += " "
    # return line_one,line_two,line_three

def textConvert(currentLetter, row, col):
    """This function takes in all of the potential characters
        from a string and converts it to its corresponding displayChar Function

    Args:
        currentLetter (_type_): any char
        row (_type_): the value 3
        col (_type_): the value 2
    """
    match currentLetter:
        case 'a':displayChar(a, row, col),
        case 'b':displayChar(b, row, col),
        case 'c':displayChar(c, row, col),
        case 'd':displayChar(d, row, col),
        case 'e':displayChar(e, row, col),
        case 'f':displayChar(f, row, col),
        case 'g':displayChar(g, row, col),
        case 'h':displayChar(h, row, col),
        case 'i':displayChar(i, row, col),
        case 'j':displayChar(j, row, col),
        case 'k':displayChar(k, row, col),
        case 'l':displayChar(l, row, col),
        case 'm':displayChar(m, row, col),
        case 'n':displayChar(n, row, col),
        case 'o':displayChar(o, row, col),
        case 'p':displayChar(p, row, col),
        case 'q':displayChar(q, row, col),
        case 'r':displayChar(r, row, col),
        case 's':displayChar(s, row, col),
        case 't':displayChar(t, row, col),
        case 'u':displayChar(u, row, col),
        case 'v':displayChar(v, row, col),
        case 'w':displayChar(w, row, col),
        case 'x':displayChar(x, row, col),
        case 'y':displayChar(y, row, col),
        case 'z':displayChar(z, row, col),
        case '.':displayChar(period, row, col),
        case '!':displayChar(exclamation_mark, row, col),
        case '?':displayChar(question_mark, row, col),
        case ',':displayChar(comma, row, col),
        case ' ':displayChar(space, row, col),
        case '0':[displayChar(number_sign, row, col), displayChar(j, row, col)],
        case '1':[displayChar(number_sign, row, col), displayChar(a, row, col)],
        case '2':[displayChar(number_sign, row, col), displayChar(b, row, col)],
        case '3':[displayChar(number_sign, row, col), displayChar(c, row, col)],
        case '4':[displayChar(number_sign, row, col), displayChar(d, row, col)],
        case '5':[displayChar(number_sign, row, col), displayChar(e, row, col)],
        case '6':[displayChar(number_sign, row, col), displayChar(f, row, col)],
        case '7':[displayChar(number_sign, row, col), displayChar(g, row, col)],
        case '8':[displayChar(number_sign, row, col), displayChar(h, row, col)],
        case '9':[displayChar(number_sign, row, col), displayChar(i, row, col)]

def pt_to_px(pt: int = 11):
    """A function to covert font in Points to Pixels
    This is so that the sizing of the font can be more consistent to the 
    screen dimensions. It uses the PyQt5 library to detect screen DPI.
    (Default is 11Pt font)
    Args:
        pt (int): The Font size in Points

    Returns:
        Pixels [Int]: The font size in Pixels
    """
    app = QApplication(sys.argv)
    screen = app.screens()[0]
    dpi = screen.physicalDotsPerInch()
    app.quit()
    return int((pt / 72) * dpi)

# Globally determine the font size to prevent the GUI error
fontSize = pt_to_px(20)

def textToImage(textToConvert: str, outputFileName: str ):
    """A function to convert a text strng to an image file.

    Args:
        textToConvert (str): input string to be converted
        outputFileName (str): name of the output file
    """
    # we are going to need to come up with a formula to calculate the number 
    # of pixels wide and tall each character is

    # Split the string into lines at each '\n' 
    lines = textToConvert.split('\n')

    #Initialization
    numChars = 0
    numLines = 0

    # Iterate through each line and find the longest line
    for line in lines:
        #get the total number of lines
        numLines += 1
        if len(line) > numChars:
            #use ::2 to get each braille character of two chars (count every 2 chars)
            numChars = len(line[::2])
            
    #print("Number of chars: " + str(numChars))#?DEBUG

    # get a font (Font Choice is important for correct output, must use monospace fixed width)
    # size is the size in pixels, use the pt_to_px function to get the correct size
    fnt = ImageFont.truetype("consolasB.ttf", size = fontSize)
    
    # Get the dimension coordinates of a single character in the specified font size
    width, height, width2, height2 = fnt.getbbox(text = '•')
    # print("Width (x) of char: " + str(width) +", " + str(width2),"height (y) of char: " + str(height)+", " + str(height2))#?DEBUG
    
    # Calculate the width and the height based on the coordinates
    charWidth = width2-width
    charHeight = height2 - height

    #! OLD METHOD
    # (60,105) = size of 1 char, test using char q to get full size
    # multiply X by the number of character then subtract away (number of hangover bits * # of chars)
    # multiply y by the number of lines then subtract (that value / 3 because it treats each character as 3 rows)*2 for 2/3


    # Pixel dimentions of the resulting image (x, y) 
    size = ((charWidth*3) * numChars) , ceil(((charHeight*3) * numLines)/2)
    # create an image (mode, size, color)
    out = Image.new("RGB", size , (255, 255, 255))

    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw multiline text
    d.multiline_text((0, 0), textToConvert, font=fnt, spacing = .2,  fill=(0, 0, 0))

    # save the image
    ImageOps.contain(out, size).save(outputFileName + ".jpg")

    out.show()

def getBFContent(brailleFileName: str):

    """ Get Braille File Content: \n
    A method of getting the braille text out of the file to be converted to an image
    Do not worry about adding the .TXT to the content of the input, it will automagically do it

    Args:
        brailleFileName (str): name of the braille file
    """
    
    with open(brailleFileName + ".txt", "r") as file:
        wholeFile = ""
        for line in file:
            #concatenate the whole file into a single string (it knows new line because it stores \n)
            wholeFile += line
        #print(wholeFile)#?DEBUG
        return wholeFile
    
def convert2STL(fileName: str):
    """This is a function using the Lithophane Library. It is modified from the example provided by the library author.

    Args:
        fileName (str): name of the image file the user wants to convert to a lithophane
    """
    #Generate xyz point cloud
    imagefile = fileName
    width: int = 102 #Width in mm
    #Depth controls the height of the dots. Set to .9 for ADA compliance.
    x,y,z = LI.jpg2stl(imagefile, width=width, depth= .9, offset= 1)
    #Generate stl model from pointcloud and save
    model = LI.makemesh(x,y,z)
    filename=imagefile[:-4] + '_Flat.stl'
    model.save(filename)

# Clear everything before starting the main
lineOne = ""
lineTwo = ""
lineThree = ""


#MAIN

#to initialize the loop 
running = True

while running:
    choice = input("Translate From input(1), Translate from file(2), help(3)  or end(4): ")
    # print(choice)#?DEBUG
    toBeConverted: str = " "
    if choice == "1":
        toBeConverted = input("What would you like to translate? ")
        for character in toBeConverted:
            # print(character)#?DEBUG
            # print(toBeConverted)#?DEBUG
            if character.isupper():
                character = character.lower()
                # print(character)#?DEBUG
                displayChar(capital_letter, 3, 2)
                textConvert(character, 3, 2)
            else:
                textConvert(character, 3,2)
        print(lineOne)
        print(lineTwo)
        print(lineThree)
        # Add all of the lines to a single string so it can be converted to an image
        toImage = lineOne + "\n" + lineTwo + "\n" + lineThree + "\n"
        textToImage(toImage, toBeConverted + "Translated")
        convert2STL(toBeConverted + "Translated.jpg")
        with open(toBeConverted + "Translated.txt", "w") as file:
            # Write to file and then clear input
            file.write(lineOne + "\n")
            file.write(lineTwo + "\n")
            file.write(lineThree + "\n")
            lineOne = ""
            lineTwo = ""
            lineThree = ""
        
        # Clear strings for next input
        lineOne = ""
        lineTwo = ""
        lineThree = ""
    elif choice == "2":
        # writeFileName = input("What would you like to name the output file: ")# User no longer gets a choice 1/2/24
        fileInputLoop = True
        while fileInputLoop == True:
            fileName = input("What is the name of the file you would like to translate. Be sure to enter it EXACTLY as it is found without the .txt: ")
            if os.path.exists(fileName+".txt"):
                fileInputLoop = False
            else:
             print("File not found. Please enter a valid file name.")
       
       
        with open(fileName+"Translated.txt","w") as writeableFile:
            with open(fileName + ".txt", "r") as file:
                for line in file:
                    print(line)
                    for character in line:
                         # print(character)#?DEBUG
                         # print(toBeConverted)#?DEBUG
                        if character.isupper():
                            character = character.lower()
                            # print(character)#?DEBUG
                            displayChar(capital_letter, 3, 2)
                            textConvert(character, 3, 2)
                        else:
                            textConvert(character, 3,2)
                    print(lineOne)
                    print(lineTwo)
                    print(lineThree)
                    writeableFile.write(lineOne + "\n")
                    writeableFile.write(lineTwo + "\n")
                    writeableFile.write(lineThree + "\n")
                    # add a blank line inbetween lines of text
                    writeableFile.write("\n")
                    lineOne = ""
                    lineTwo = ""
                    lineThree = ""
        contentString:str = getBFContent(fileName+"Translated")
        textToImage(contentString, fileName + "Translated")
        convert2STL(fileName + "Translated.jpg")
    elif choice == "3":
        print("Translate from input allows the user to translate a string they type. \nTranslate from file allows the user to select a file that they want to translate.")
    elif choice == "4":
        break