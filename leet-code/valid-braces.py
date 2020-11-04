from collections import deque

def isOpenBrace(s):
    return (s == '(' or s == '{' or s == '[')

def isCloseBrace(s):
    return (s == ')' or s == '}' or s == ']')

def matched(s):
    if (s == ')'):
        return '('
    elif (s == '}'):
        return '{'
    else:
        return '['

def isValid(s) -> bool:
    stack = deque()

    if (len(s) == 0):
        return False

    if (isCloseBrace(s[0])):
        return False

    for i in s:
        if (isOpenBrace(i)):
            stack.append(i)
    
        if (isCloseBrace(i)):
            if (stack[-1] == matched(i)):
                stack.pop()

    if (len(stack) == 0):
        return True
    else:
        return False

print(isValid("(){}}{"))