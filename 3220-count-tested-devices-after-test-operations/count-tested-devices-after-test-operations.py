class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        bt = batteryPercentages
        count = 0
        for i in range(len(bt)):
            if bt[i] > 0:
                count+=1
                for j in range(i,len(bt)):
                    bt[j] = bt[j]-1

        return count