# Random Number file writer.
# 7/14/17
# CTI-110 M6HW1 - Random Number File Writer
# Patricia Hicks
#
import random

afile = open("Random.txt", "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 500))
    afile.write(line)
    print(line)

afile.close()

print("\nReading the file now." )
afile = open("Random.txt", "r")
print(afile.read())
afile.close()
