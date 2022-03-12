import sys
import csv
import itertools

csvFile = open("files/1_2_christmas_cards.csv")

data = [row for row in csv.reader(csvFile)]

waypoints = ['work',  'a',   'b',   'c',   'd',   'e',   'f',   'g',   'h',  'home']

durationMin = sys.maxsize
routeMin = []

for subset in itertools.permutations(waypoints, 10):
    
    durationWholeWay = 0
    routeValid = 1
    for i in range(0,9):
        # Define start and destination
        start = subset[i]
        destination = subset[i+1]
        # Get duration
        duration = data[waypoints.index(start)][waypoints.index(destination)]
        
        if "-" in duration:
            routeValid = 0
            break
        
        durationWholeWay = durationWholeWay + int(duration)
                
    if routeValid and durationWholeWay < durationMin:
        durationMin = durationWholeWay
        routeMin = subset
        
for waypoint in routeMin:
    if waypoint != 'work' and waypoint != 'home':
        print(waypoint, end = '')