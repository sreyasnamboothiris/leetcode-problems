class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        length = len(word1) if len(word1) < len(word2) else len(word2);
        word1_index = 0
        word2_index = 0
        updated_string = ''
        for i in range(length):
            updated_string += word1[i]
            updated_string += word2[i]

        updated_string += word1[i+1:]
        updated_string += word2[i+1:]
        return updated_string
            
        
            
            
        


        
        