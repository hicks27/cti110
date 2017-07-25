#Age Classifier.
#6/18/17
#CTI-110 M3HW1 - Age Classifier
#Patricia Hicks
#
userAge = int( input( "Please enter your age:") )

if userAge <= 1:
    print( "You are a infant" )
elif userAge < 13:
    print( "You are a child" )
elif userAge < 20:
    print( "You are teenager" )
elif userAge >= 20:
    print( "You are a adult" )
    
