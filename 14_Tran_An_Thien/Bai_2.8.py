# Write a function on_all that applies a function to every element of a list.
# Use it to print the first twenty perfect squares.
# The perfect squares can be found by multiplying each natural number with itself.
# The first few perfect squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16.
# Twelve for example is not a perfect square because there is no natural number m so that m*m=12.
# (This question is tricky if your programming language makes it difficult to pass functions as arguments.)

"""
Chúng ta chỉ cần lấy căn bậc hai của 'a' và căn bậc hai của 'b' và đếm các ô vuông hoàn hảo giữa chúng bằng cách sử dụng
floor (sqrt (b)) - ceil (sqrt (a)) + 1
Chúng ta lấy sàn của sqrt (b) vì chúng ta cần xem xét các số trước b.
Chúng tôi lấy trần của sqrt (a) vì chúng tôi cần xem xét các số sau a.

Ví dụ: đặt b = 24, a = 8. floor (sqrt (b)) = 4,
ceil (sqrt (a)) = 3. Và số lượng hình vuông là 4 - 3 + 1
= 2. Hai số là 9 và 16.
"""
import math


def CountSquares(a, b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)


# Driver Code
a = 9
b = 25
print("Count of squares is:", int(CountSquares(a, b)))
