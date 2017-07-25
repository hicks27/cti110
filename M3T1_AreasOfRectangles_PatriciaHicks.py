#Area of Rectangles.
#6/18/17
#CTI-110 M3T1 - Area of Rectangles
#Patricia hicks
#
rectangle1Length = float( input( "Please enter the lenght of rectangle 1: " ) )
rectangle1Width = float( input( "Please eneter the width of rectangle 1: ") )
rectangle2Length = float( input( "Please enter the length of rectangle 2: " ) )
rectangle2Width = float( input( "Pleace enter the width of rectangle 2: ") )
rectangle1Area = rectangle1Length * rectangle1Width
rectangle2Area = rectangle2Length * rectangle2Width

if rectangle1Area > rectangle2Area:
    print( "Rectangle 1 is bigger than Rectangle 2" )
elif rectangle2Area > rectangle1Area:
    print( "Rectangle 2 is bigger than rectanglr 1" )
else:
    print( "Both rectangles are equal" )
