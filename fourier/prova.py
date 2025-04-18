
def longestpalindrome(s):
    p1 =0
    p2 = len(s)-1
    while p1<len(s):
        if s[p1] == s[p2]:
            if s[p1:p2+1] == s[p1:p2+1][::-1]:
                sol = s[p1:p2+1]
                return sol[0:len(sol)//2]
            p2 -= 1
        else:
            p1+=1
        p1 +=1

    return '' 
        
print(longestpalindrome('cbbd'))



