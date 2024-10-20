class Solution:
    def maximumSwap(num: int) -> int:
        def maxNumber(n:str,ind:int):
            dicmay = {"may":int(n[0]),"index":ind}
            for i in range(len(n)):
                if int(n[i]) > dicmay["may"]:
                    dicmay["may"] = int(n[i])
                    dicmay["index"] += i 
            return dicmay
        
        num :str = str(num)
        firstpart :str = ""
        middlepart :str = ""
        secondpart :str = ""
        dic:dict = {"may":0,"index":0}
        for i in range(len(num)):
            for f in range(i+1,len(num)):
                if int(num[i]) < int(num[f]):
                    if f < len(num)-1 :
                        dic = maxNumber(num[f+1:],f+1)
                    if int(num[f]) > dic["may"]:
                        if i == 0:
                            firstpart = num[1:f]
                            secondpart = num[f+1:]
                            num = num[f] + firstpart + num[i] + secondpart
                            return int(num)
                        else:
                            firstpart = num[0:i]
                            middlepart = num[i+1:f]
                            secondpart = num[f+1:]
                            num = firstpart + num[f] + middlepart + num[i] + secondpart
                            return int(num)
                    elif int(num[f]) == dic["may"] and f == dic["index"]:
                        firstpart = num[0:i]
                        middlepart = num[i+1:f]
                        secondpart = num[f+1:]
                        num = firstpart + num[f] + middlepart + num[i] + secondpart
                        return int(num)
                        
        return int(num)

    print(maximumSwap(1993))

