from datetime import datetime, date
import random
from subprocess import call

__author__ = 'Tobias Wooldridge'

def getPixels (image):
    return map(lambda row: list(row), image.split("\n"))[1:-1]

def getImage (pixels):
    return "\n".join(map(lambda row: "".join(row), pixels))

image = """
____________________________________
_MMMMM__MMM___MMMM___M__MMMM__MMMM__
___M___M___M__M___M__M__M__M__M_____
___M___M___M__MMMM___M__MMMM__MMMM__
___M___M___M__M___M__M__M__M_____M__
___M____MMM___MMMM___M__M__M__MMMM__
____________________________________
"""

pixels = getPixels(image)


dayStarted = date(2013, 12, 15)
today = date(2013, 12, 23)
# today = date.today()

weeksRunning = int((today - dayStarted).days / 7)
weekIndex = weeksRunning % len(pixels[0])

# Get day's number; 0 = Sunday, 1 = Monday..
dayIndex = today.isocalendar()[2] % 7

todaysPixel = pixels[dayIndex][weekIndex]

print (weekIndex, dayIndex)
print (todaysPixel)

pixels[dayIndex][weekIndex] = 'o'

print (getImage(pixels))

if todaysPixel == "M":
    for i in range(1, 30):
        f = open('meep', 'w+')
        f.write(".")
        f.close()

        call(["git commit .", "-am 'tick'"])


    call(["git", "push"])

