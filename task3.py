#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''

import math

def split(input):
    '''
    parameters
    str input - string to be split
    
    return
    str new string with line break in the middle
    '''
    
    x = len(input)

    half1 = input[0:math.floor(x/2)]
    half2 = input[math.floor(x/2):x]

    if half1[math.floor(x/2)-1]==" " or half2[0]==" ":
        pass
    else:
        half1 = half1 +"-"
        

    modified = half1 + '\n' + half2

    return modified

if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(sentence) == "There is a big ball-\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a\n fat cat"
    
    print("Done")