#!python3

"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""


def spacecount(string): #Using the number of spaces to determine how many words there are
    x = string.count(" ") + 1
    print(x)
    return(x)

def listcount(string):
    x = string.split()

    length = len(x)
    
    return length

def main():
    y="The quick brown fox jumps over the lazy dogs"
    assert spacecount(y) == 9

    lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    assert spacecount(lorem) == 69
    

    txt = "welcome to the jungle"
    assert listcount(txt) == 4

    txt2 = "hello there guys                           hi"
    assert listcount(txt2) == 4

    print('Done')


if __name__ == "__main__":
  main()

