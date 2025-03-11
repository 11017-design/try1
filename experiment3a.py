i=20
if i<15:
    print("i is smaller than 15")
    print("I'm in if Block")
else:
    print("i is greater than 15")
    print("I'm in else Block")
print("I'm not in if and not in else Block.\n")

if i>=0:
    if i==0:
        print("Zero\n")
    else:
        print("Positive number\n")
else:
    print("Negative number\n")
if(i==20):
    if i<25:
        print("i is smaller than 25.")
        if i<19:
            print("i is smaller than 19 too.\n")
        else:
            print("i is greater than 19 and smaller than 25\n")
        

pointsScored=[26,18,9,12,21,26]
if len(pointsScored)>3:
    pointsSum=0
    for score in pointsScored:
        pointsSum+=score
    if pointsSum>45:
        print("Nice, those", pointsSum, "points are more than the needed 45!\n")
    else: 
        print("Ouch! Not enough points yet!\n")
        
import datetime
now=datetime.datetime.today()
print("Today is",now)
if now.hour<12:
    if now.month>6:
        print("We're in the second half of",now.year,"already!")
    else:
        print("This year isn't even 6 months old.")