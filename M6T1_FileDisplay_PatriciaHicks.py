#File Display.
#7/8/17
#CTI-110 M6T1 File Display.
#Patricia Hicks.
#
def main():
    numbersFile = open( "numbers.txt", "r" )

    line = numbersFile.readline()

    while line != "":
        print( line.rstrip( "\n" ) )
        line = numbersFile.readline()

      # 45\n6\n7\n8\n

main()
