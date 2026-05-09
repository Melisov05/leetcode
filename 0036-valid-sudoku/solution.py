from typing import List

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        collapsed_array = []
        for row in board:
            for element in row:
                collapsed_array.append(element)
        
        return self._check_rows_and_columns(collapsed_array) and self._check_squares(collapsed_array)
        

    def _check_rows_and_columns(self, collapsed_array: List[str]) -> bool:
        set_for_rows = set()

        for i in range(len(collapsed_array)):
            # if checking one row is done we reset the set
            if i % 9 == 0 and i != 0:
                set_for_rows.clear()

            if collapsed_array[i] != ".":

                if collapsed_array[i] not in set_for_rows and self.in_range(collapsed_array[i]):
                    set_for_rows.add(collapsed_array[i])
                else:
                    return False
            
            #the moment i gets to 9 we covered all of the columns
            if (i <= 8):
                set_for_columns = set()
                j = i
                while j < len(collapsed_array):
                    value = collapsed_array[j]
                    
                    if value != ".":
                        if not self.in_range(value):
                            return False

                        if value in set_for_columns:
                            return False
                        set_for_columns.add(value)
                    j += 9
        
        return True
    

    def in_range(self, num):
        num = int(num)
        return 1 <= num and num <= 9
            
    def _check_squares(self, my_list):
        
        for box_row in range(0, 9, 3):
            for box_col in range(0,9,3):
                square_set = set()

                for row_shift in range(3):
                    for col_shift in range(3):
                        row = box_row + row_shift
                        col = box_col + col_shift
                        index = row * 9 + col 

                        if my_list[index] != ".":

                            if not self.in_range(my_list[index]):
                                return False

                            if my_list[index] in square_set:
                                return False
                            square_set.add(my_list[index])
        return True
                

solution = Solution()
print(solution.isValidSudoku(board=board))

