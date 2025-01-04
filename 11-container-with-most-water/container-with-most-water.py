class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        maxx = 0
        r = len(height)-1
        while l < r:
            if height[l] > height[r]:
                if maxx < height[r] * (r-l):
                    maxx = height[r] * (r-l)
                r-=1
            elif height[r] > height[l]:
                if maxx < height[l] * (r-l):
                    maxx = height[l] * (r-l)
                l += 1
            else:
                if maxx < height[l] * (r-l):
                    maxx = height[l] * (r-l)
                r -=1
                l +=1
        return maxx
                 
        
        
        