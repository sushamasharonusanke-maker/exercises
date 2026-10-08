numbers=[5,6,7,1,2,9,5,4,7,3,2,1,5,6,9,12,13,53,73,77,-3,-2,-57]

smallest = largest = numbers[0]
total = 0

for number in numbers:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
    total += number

average = total / len(numbers)

squared_deviation_total = 0
for number in numbers:
    difference = number - average
    squared_deviation_total += difference * difference

standard_deviation = (squared_deviation_total / len(numbers)) ** 0.5

print("Minimum:", smallest)
print("Maximum:", largest)
print("Mean:", average)
print("Population standard deviation:", standard_deviation)