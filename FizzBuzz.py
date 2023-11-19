class solution : 
    def FizzBuzz(n: int) -> list[str]:
        result = []

        for i in range(1 , n+1):
            temp = ''
            if i % 3 == 0 :
                temp += 'Fizz'
            if i % 5 == 0 :
                temp += 'Buzz'
            if i %3 != 0 and i % 5 != 0 :
                temp += f'{i}'
            result.append(temp)
        return result
    
res = solution.FizzBuzz(15)
print(res)
