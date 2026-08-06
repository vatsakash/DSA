class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(1,n+1):
            a.append(str(i))
        for j in range(1,len(a)+1):
            if j % 3 == 0 and j % 5 == 0:
                a[j-1] = "FizzBuzz"
            elif j % 3 == 0:
                a[j-1] = "Fizz"
            elif j % 5 == 0:
                a[j-1] = "Buzz"
            else:
                pass
        return a 

        