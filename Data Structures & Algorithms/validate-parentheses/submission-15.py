class Solution:
    def isValid(self, s: str) -> bool:
        left = '({['
        right = ')}]'

        arr = []
        dic = {'(':')', '{':'}', '[':']'}


        for i in s:
            if i in left:
                arr.append(i)
            if i not in left:
                if len(arr) == 0:
                    return False
                else:
                    pair = arr.pop()

                    if dic[pair] != i:
                        return False
        if len(arr) >0:
            return False
        
        return True



        