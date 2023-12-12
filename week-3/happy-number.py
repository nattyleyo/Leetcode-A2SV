class Solution:
    def isHappy(self, n: int) -> bool:
        seen_sums = set()
        
        while n != 1 and n not in seen_sums:
            seen_sums.add(n)
            digit_squares_sum = 0
            
            while n > 0:
                digit = n % 10
                digit_squares_sum += digit * digit
                n //= 10
            
            n = digit_squares_sum
        
        return n == 1