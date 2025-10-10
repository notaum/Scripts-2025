import sys
sys.set_int_max_str_digits(900000000)
x = int(input("Number Please: "))
y = 1

with open(f"{x}Pattern.txt", "w") as file:
    while y <= 12:
        x = x * x
        file.write(str(x) + "\n \n---------------------------------------------------\n \n")  # Write value of x and two newlines into file
        y += 1

