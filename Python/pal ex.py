def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('asdsdsa'))

def pal(word):
    stack =[]
    for letter in word:
        stack.append(letter)
    for letter in word:
        if stack.pop() != letter:
            return False
    return True

print(pal('asdsdddda'))

def palindrome(word):
    s=[]
    for i in range(len(word)):
        s.append(word[i])
    for i in range(len(word)):
        if s.pop() != word[i]:
            return False
    return True

print(palindrome('RACECAR'))


def palin(word):
    s=[]
    for letter in word:
        s.append(letter)
    for letter in word:
        if s.pop() != letter:
            return False
    return True

print(palin('RACECAR'))
