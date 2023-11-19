class Solution :
    def TwoSums(num: list[int] , target : int) -> list[int] :
        res = [] 
        index_map = {}

        for i , n in enumerate(num):
            difference = target - n
            if difference in index_map:
                res.append(i)
                res.append(index_map[difference])
                break 
            else :
                index_map[n] = i
        return res
    
num = [2 , 7 , 9 , 12]
target = 9     
res = Solution.TwoSums(num , target)
print(res)