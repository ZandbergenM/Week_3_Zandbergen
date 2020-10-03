#Week 3 Zandbergen
#6.3

def first(word):
    return word[0]

print(first('Hello'))


def last(word):
    return word[-1]

print(last('December'))


def middle(word):
    return word[1:-1]
print(middle('Tomorrow'))

#1
#Call middle with a string of two letters - returns a blank space with ' '
print(middle('hi'))
#Call middle with a string of one letter - returns a blank space with ' '
print(middle('h'))
#Call middle with no letters - returns a blank space with ' '
print(middle(' '))
#Call middle
print(middle('Hello'))
#Call First
print(first('Hello'))
#Call Last
print(last('Hello'))

#2

def is_palindrome(word):
    if word == word[:: -1]:
        return True
    else:
        return False
print(is_palindrome('redivider'))
print(is_palindrome('noon'))
print(is_palindrome('October'))



