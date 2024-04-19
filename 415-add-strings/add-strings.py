import sys

class Solution:
    
    def addStrings(self, num1: str, num2: str) -> str:


        

        # Set the maximum number of digits for the string representation of integers
        max_digits = 50000  # You can specify any integer value as the limit
        sys.set_int_max_str_digits(max_digits)

        b = int(num2)
        a = int(num1)
        
        c = a+b
        return str(c)