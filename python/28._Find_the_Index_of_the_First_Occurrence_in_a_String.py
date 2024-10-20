class Solution(object):
    def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < 1:
            return -1
        for char in range(len(haystack) - len(needle) + 1):
            if haystack[char:len(needle) + char] == needle:
                return char 
        return -1
    print(strStr("hello","ll"))