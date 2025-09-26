decimalnumber = int(input("Enter a decimal number: "))
def decimal_to_binary_manual(n):
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary
binarynumber = decimal_to_binary_manual(decimalnumber)
print("Binary number is: ",binarynumber)

