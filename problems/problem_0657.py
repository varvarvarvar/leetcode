"""Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be
true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""


class Solution:
    def judgeCircle(self, moves):
        res_up = 0
        res_left = 0
        for move in moves:
            if move == "U":
                res_up += 1
            elif move == "D":
                res_up -= 1
            elif move == "L":
                res_left += 1
            elif move == "R":
                res_left -= 1
        return not res_up and not res_left
