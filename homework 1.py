odd_squares = []
even_squares = []

start = int(input("enter starting range : "))
end = int(input("enter a ending range : "))
for num in range(start, end + 1):
    if (num%2)== 0:
        even_squares.append(num ** 2)
    else:
        odd_squares.append(num ** 2)

print("Even Squares are : ", even_squares)
print("Odd Squares are : ", odd_squares)