# 2. Count Odd Numbers in an Interval Range
#       Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Difficulty: Easy
# Topics: mid level math and logic


class Solution:
    def countOdds(self, low: int, high: int) -> int:
       return (high+1)//2 - (low//2)
        