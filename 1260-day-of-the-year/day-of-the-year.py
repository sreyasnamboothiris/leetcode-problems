class Solution:
    def dayOfYear(self, date: str) -> int:
        da = date.split('-')
        daa = datetime.date(int(da[0]),int(da[1]),int(da[2]))
        day_number = daa.timetuple().tm_yday
        print(day_number)
        return day_number
        