class Solution:
    def isValid(self, s: str) -> bool:
        
        item = {
            '(':')',
            '[':']',
            '{':'}'
        }
        # declare stack
        stack = []
        for character in s:# checking the charcter in the item(dict)
            if character in item:
                # push the element into stack if the charcter is key.
                stack.append(character) 
            else:
                if len(stack):
                    if item[stack[-1]] == character:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack):
            return False
        else:
            return True
                    



        