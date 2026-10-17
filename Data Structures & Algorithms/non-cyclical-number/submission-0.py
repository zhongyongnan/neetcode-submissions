class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        # 如果形成了一个loop且不含1, 那就不是happy number
        while n not in visit:
            visit.add(n)
            n=self.sumOfSquares(n)
            if n==1:
                return True
        return False
    
    def sumOfSquares(self, n:int)->int:
        output=0

        while n:
            digit=n%10
            digit=digit**2
            output+=digit
            n=n//10
        return output
