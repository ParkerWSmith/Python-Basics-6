#Parker Smith
#2/26/2018
#CCIS 1505-02
#Program 6

#Code for testing
#lstWeekDays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

#allow the user to add days of the week
lstWeekDays = []
blnDone = False
while blnDone == False:
    strName = input ("Enter days of the week one at a time, press enter when done: ")
    if len(strName) == 0:
        blnDone = True
        print ()
    else:
        lstWeekDays.append(strName.title())

#print the days added
for day in lstWeekDays:
    print(day)
print()

#reverse the days
#lstWeekDays.reverse()
for day in reversed(lstWeekDays):
    print(day)
print()

#show the sorted days
#lstWeekDays.sort()
for day in sorted(lstWeekDays):
    print (day)
print ()

#slice days to show first 3 letters
for day in lstWeekDays:
    print(day + " = " + day[0:3])
print ()

#show days that startwith t
for day in lstWeekDays:
    if day.startswith("T"):
        print(day)
print()

dctCourses = { 1000:"Intro to IS", 1505: "Fundamentals of Programming",
              1515:"Web Programming Overview", 2575:".NET Programming 1",
              2585:".NET Programming 2", 2701:"Database Design & SQL"}

#show value
#dctCourses.sort()
for value in sorted(dctCourses.values()):
    print (value)
print()

#show keys
for key in sorted(dctCourses.keys()):
    print(key)
print()

#print course 1505
course = dctCourses.get(1505)
print (course)
