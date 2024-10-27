class Solution:
    def removeStars(s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if '*' == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
    
    print(removeStars("leet**cod*e"))