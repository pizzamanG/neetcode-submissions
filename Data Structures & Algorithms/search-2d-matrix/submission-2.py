class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(l, r, array, target):
            if l > r:
                return False
            median = l + (r-l) //2
            if array[median] == target:
                return True
            elif array[median] < target:
                return binary_search(median+1, r, array, target)
            
            return binary_search(l, median-1, array, target)

        for arr in matrix:
            res = binary_search(0, len(arr)-1, arr, target)
            if res == True:
                return True

        return False
        
        