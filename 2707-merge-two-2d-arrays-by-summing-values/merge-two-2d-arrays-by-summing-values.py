class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        hash_table = {}
        n1 = 0
        n2 = 0
        length = nums1[-1][0] if nums1[-1][0] > nums2[-1][0] else nums2[-1][0]
        print(length)
        for i in range(length+1):
            if len(nums1) > n1 and nums1[n1][0] == i:
                if i in hash_table:
                    hash_table[i] += nums1[n1][1]
                else:
                    hash_table[i] = nums1[n1][1]
                n1 += 1
            if len(nums2) > n2 and nums2[n2][0] == i:
                if i in hash_table:
                    hash_table[i] += nums2[n2][1]
                else:
                    hash_table[i] = nums2[n2][1]
                n2 += 1
        l = []
        print(hash_table)
        for key,value in hash_table.items():
            m = []
            m.append(key)
            m.append(value)
            l.append(m)
        return l






        