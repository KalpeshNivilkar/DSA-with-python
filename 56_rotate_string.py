# brute-force approach 

'''def rotate_string(s,goal):
    if len(s) != len(goal):
        return False
    curr_s = s
    n = len(curr_s)

    for i in range(n):
        if curr_s == goal:
            return True
        curr_s = curr_s[-1] + curr_s[:-1]
    return False
s = "lobpzonj"
goal = "zonjlobp"

print(rotate_string(s,goal))'''

# optimal approach 

def rotate_string(s,goal):
    if len(s) != len(goal):
        return True
    double_s = s + s
    if goal in double_s:
        return True
    return False
s ="zonjlobp"
goal = "lobpzonj"

print(rotate_string(s,goal))

        