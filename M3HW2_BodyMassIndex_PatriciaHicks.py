#Body Mass Index.
#CTI-110 M3HW2 - Body Mass Index
#6/18/17
#Patricia Hicks
#

userWeight = float( input( "Please enter your weight: " ) )
userHeight = float( input( "Please enter your height: " ) )
userBmi = ( userWeight * 703 ) /( userHeight ** 2 )

print()

if userBmi < 18.5:
    print( "A person with ami of " + format( userBmi, ".2f" ) + " is underweight")
elif userBmi < 26:
    print( "A person with a Bmi of " + format( userBmi, ".2f" ) + \
           " has an optinal weight")
else:
    print( "A person with a Bmi of " + format( userBmi, ".2f" ) + \
          " is overweight")
