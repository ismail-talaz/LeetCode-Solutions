class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x,y=0,int(math.sqrt(c))

        while (x<=y):
            if (x*x+y*y)==c:return True
            elif (x*x+y*y)<c:x+=1
            else:y-=1
        return False
