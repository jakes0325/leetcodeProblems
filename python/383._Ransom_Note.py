class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n:int = len(ransomNote)
        flag:bool = True
        i:int = 0
        while i < n:
            if ransomNote.count(ransomNote[i]) > magazine.count(ransomNote[i]):
                flag=False
            i+=1
        return flag