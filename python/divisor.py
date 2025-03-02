number = int(input("Give me a number: "))

list_divisor = []
list_number = list(range(1, number+1))

for x in list_number:
    if number % x == 0:
        list_divisor.append(x)

print("This is a list of all the divisors of this number:",list_divisor)