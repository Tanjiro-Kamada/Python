def square_area():
    side_length = float(input("Enter the length of the side of the square: "))
    area = side_length ** 2
    return area

s1 = square_area()
print(s1)

def rectangle_area(length, width):
    area = length * width
    return area

s2 = rectangle_area(5, 3)
s3 = rectangle_area(10, 4)
s4 = rectangle_area(7, 2)
s5 = rectangle_area(6, 8)

print(s2)
print(s3)
print(s4)
print(s5)