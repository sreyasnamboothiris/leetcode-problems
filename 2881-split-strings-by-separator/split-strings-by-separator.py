class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        alpha = []
        x = []
        for i in words:
             x += i.split(separator)
             
        str_list = list(filter(None, x))
        print(str_list)
        return str_list

        