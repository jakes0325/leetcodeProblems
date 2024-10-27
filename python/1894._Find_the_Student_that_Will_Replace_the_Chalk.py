class Solution:
    def chalkReplacer(chalk: list[int], k: int) -> int:
        #k es igual a la cantidad de tiza que hay
        #y la lista es la cantidad de tiza que usan los alumnos empezando desde 0 a n-1
        # ejemplo chalk = [5,1,5], k = 22
        result:int
        k = k%sum(chalk)
        for i in range(len(chalk)):
            if k<chalk[i]:
                result = i
                break
            if k>=chalk[i]:
                k-=chalk[i]
        return result

    print(chalkReplacer([1],1000000000))