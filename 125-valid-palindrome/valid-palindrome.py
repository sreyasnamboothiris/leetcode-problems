class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ''
        tr = True
        
        for i in s:
            if i.isalnum():
                k += i
        
        k=k.casefold()
        print(k)
        if k == "" or len(k)<2:
            print('hj')
            return True
        
        for i in range(int(len(k)/2)):
            if k[i] != k[len(k)-i-1]:
                print(k,k[i],k[len(k)-i-1])
                tr = False
                break
        return tr
                
                
        