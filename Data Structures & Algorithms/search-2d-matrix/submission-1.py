class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        mid = 0
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] < target:
                l = mid + 1
                if target <= matrix[mid][-1]:
                    break
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break

        row = mid
        print(row)
        l, r = 0, len(matrix[row])-1
        while l <= r: 
            mid = l + (r - l) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True

        return False