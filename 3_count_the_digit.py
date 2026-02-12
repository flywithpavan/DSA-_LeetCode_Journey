# Count the Digits That Divide a Number
# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.
# Difficulty: Easy
# Topics: mid level math and logic


class Solution:
    def countDigits(self, num: int) -> int:
        temp =num
        ans=0
        while temp >0:
            r=temp%10
            if num%r==0:
                ans+=1
            temp//=10

        return ans

        

        

 