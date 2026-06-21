def remove_paranthesis(s):
    count = 0
    result = ""
    for ch in s:
        if ch == "(":
            if count > 0:
                result += ch
            count += 1
        
        else:
            count -= 1
            if count > 0:
                result += ch
    return result

s = "(())(())"
print(remove_paranthesis(s))

        
def removeOuterParentheses(s):
    result = ""
    count = 0
    for ch in s:
        if ch == "(":
            count += 1
            if count > 1:
                result += ch
        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s = "(())(())"
print(removeOuterParentheses(s))


def remove_parantheses(s):
    count = 0
    result = ""
    for ch in s:
        if ch == "(":
            count += 1
            if count > 1:
                result += ch
        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s = "(())(())"
print(remove_parantheses(s))
