class Solution:
    def convertToBase7(num: int) -> str:
        if num == 0:
            return "0"
        result:str = ""
        isNegative:bool = False 
        if num<0:
            isNegative = True
            num = abs(num)
        while num!=0:
            result = "".join([str(num % 7),result])
            num = num // 7
        if isNegative:
            result = "".join(["-",result])
        return result
    print(convertToBase7(-100))

