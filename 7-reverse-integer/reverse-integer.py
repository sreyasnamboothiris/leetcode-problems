class Solution:
    @staticmethod
    def is_outside_32bit_range(num):
        INT32_MIN = -2_147_483_648
        INT32_MAX = 2_147_483_647
        return num < INT32_MIN or num > INT32_MAX


    def reverse(self, x: int) -> int:
        flag_negative = False
        if x < 0:
            x = x * -1
            flag_negative = True
        
        r = str(x)
        r = r[::-1]
        reversed_int = int(r)
        if flag_negative:
            reversed_int = reversed_int * -1
        tr = Solution.is_outside_32bit_range(reversed_int)
        print(tr)
        if tr:
            return 0
        else:
            return reversed_int
    
        