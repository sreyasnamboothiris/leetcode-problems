class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        right = k
        left = 0
        count = 0
        for i in blocks[left:right]:
            if i == 'W':
                count += 1
        print(blocks[left:right],count)
        low = count
        for i in range(len(blocks) - (k-1)):
            count = blocks[left:right].count('W')
            print(count,blocks[left:right])
            if count < low:
                low = count
            left += 1
            right += 1
        return low


            

            


        