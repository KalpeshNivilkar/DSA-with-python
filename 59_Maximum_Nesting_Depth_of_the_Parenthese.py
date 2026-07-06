# Example 1

'''Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: The deepest valid nesting is "((8)/4)" which has depth 3.'''

def maximum_nesting_depth_of_parantheses(s):
    curr_dept = 0
    max_dept = 0

    for ch in s:
        if ch == '(':
            curr_dept += 1
            max_dept = max(max_dept,curr_dept)
        elif ch == ')':
            curr_dept -= 1
    return max_dept
s = "(1+(2*3)+((8)/4))+1"
print(maximum_nesting_depth_of_parantheses(s))



def maximum_nesting_depth(s):
    curr_dept = 0
    max_dept = 0
    for ch in s:
        if ch == '(':
            curr_dept += 1
            max_dept = max(max_dept,curr_dept)
        elif ch == ')':
            curr_dept -= 1
    return max_dept
s = "(1+(2*3)+((8)/4))+1"
print(maximum_nesting_depth(s))