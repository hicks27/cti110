#Bugs Collected
#6/18/17
#CTI-110 M4T1 - Bugs Collected
#Patricia Hicks
#
totalDays = 5
totalNumberOfBugs = 0

for currentDay in range( 1, totalDays + 1):
    bugsCollected = int( input( "How many days were collected on day " + \
                                str(currentDay) + ": ") )
    totalNumberOfBugs += bugsCollected
print( "The total number of bugs collected for all", totalDays, "days is",\
       totalNumberOfBugs )

    
