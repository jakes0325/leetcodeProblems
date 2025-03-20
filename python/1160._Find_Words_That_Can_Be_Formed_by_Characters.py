class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        result:int = 0
        flag:bool = True
        for Index,word in enumerate(words):
            n:int = len(word)
            i:int = 0
            flag = True
            # for i in range(n):
            while i<n and flag == True :
                if word[i] not in chars or word.count(word[i]) > chars.count(word[i]):
                    flag=False
                i+=1
            if flag == True:
                result += n
        return result

print(Solution.countCharacters(0,["cat","bt","hat","tree"],"ataerch"))