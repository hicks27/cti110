# Random Number file reader.
# 7/14/17
# CTI-110 M6HW2 - Random Number File Reader
# Patricia Hicks
#

import random

random_numbers = open('ran_numbers file writer.txt', 'w')
numberOfNumbers = int(input("How many numbers do you want written to the file?: "))
print("Your random numbers are: ")
for count in range (numberOfNumbers):
    number = random.randint(1,500)
    print(number)
random_numbers.write(str(number)+ '\n')
random_numbers.close()

random_numbers = open('ran_numbers.txt', 'r')
number = 0
total = 0
print("List of numbers:")
for line in random_numbers.readlines():
        print(line)
        total = total+int(line)
        number +=1
print("The Sum of the numbers = "+str(total))
print("The total amount of numbers read are "+str(number))
