#n = int(input("Enter a number: "))
#print(("divisible", "not divisible")[n % 3 == 0 or n % 5 == 0])
# Output: Even
#
n = int(input("Enter a number: "))
print(("Not divisible by 3, 5, or 7", "Divisible by at least one")[n % 3 == 0 and n % 5 == 0])