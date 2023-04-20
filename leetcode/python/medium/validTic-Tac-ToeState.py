'''
794. Valid Tic-Tac-Toe State

Difficulty: Medium


Given a Tic-Tac-Toe board as a string array board,
return true if and only if it is possible to reach this board
position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'.
The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:
 - Players take turns placing characters into empty squares ' '.
 - The first player always places 'X' characters, while the second player always places 'O' characters.
 - 'X' and 'O' characters are always placed into empty squares, never filled ones.
 - The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
 - The game also ends if all squares are non-empty.
 - No more moves can be played if the game is over.
 
 
Example 1
Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".


Example 2
Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.


Example 3
Input: board = ["XOX","O O","XOX"]
Output: true
'''
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        #intitilize variables
        xCount = 0
        oCount = 0

        #total count for each letter
        for row in board:
            xCount += row.count('X')
            oCount += row.count('O')

        if oCount != xCount and xCount != oCount + 1:
            return False

        def winCon(letter):
            #Row Win Check
            for i in range(3):
                rowWin = True
                for j in range(3):
                    if board[i][j] != letter:
                        rowWin = False
                        break
                if rowWin:
                    return True
            
            #column win check
            for j in range(3):
                colWin = True
                for i in range(3):
                    if board[i][j] != letter:
                        colWin = False
                        break
                if colWin:
                    return True
            
            #diagional top left to bot right check
            if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
                return True

            #diagional top right to bot left check
            if board[0][2] == letter and board[1][1] == letter and board[2][0] == letter:
                return True
            
            #if no win conditon met, return false
            return False
        

        if winCon('X') and xCount != oCount + 1:
            return False

        if winCon('O') and xCount != oCount:
            return False


        return True