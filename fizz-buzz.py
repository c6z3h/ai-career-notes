class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int        {1;10^4}
        :rtype: List[str]
        """
        answer = [0]*n
        # Fizz if divisible by 3
        # Buzz if divisble by 5
        # FizzBuzz if both
        for i in range(1,n+1):      # IF N = 3, i = 0,1,2
            if i % 3 == 0 and i % 5 == 0:
                answer[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                answer[i-1] = "Fizz"
            elif i % 5 == 0:
                answer[i-1] = "Buzz"
            else:
                answer[i-1] = str(i)
        return answer
