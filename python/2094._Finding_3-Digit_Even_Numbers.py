class Solution:
    def findEvenNumbers(digits: list[int]) -> list[int]:
        result:list[int] = []
        for i in range(100,999,2):
            # print(i)
            i = str(i)
            if int(i[0]) in digits and int(i[1]) in digits and int(i[2]) in digits and i.count(i[0]) <= digits.count(int(i[0])) and i.count(i[1]) <= digits.count(int(i[1])) and i.count(i[2]) <= digits.count(int(i[2])):
                result.append(int(i))

        return result










    print(findEvenNumbers([2,1,3,0]))
        
