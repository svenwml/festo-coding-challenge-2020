import sys
import csv
import itertools

csvFile = open("files/2_2_christmas_shopping.csv")

data = [row for row in csv.reader(csvFile)]

waypoints = ['work', 's1',  's2',  'p1',  'p2',  'h1',  'h2',  'd1',  'd2',  't1',  't2', 'home']

durationMin = sys.maxsize
routeMin = []

for subset in itertools.permutations(waypoints, 7):
    
    # Only one shop per type allowed.
    if(('s1' in subset and 's2' in subset) or 
    ('p1' in subset and 'p2' in subset) or 
    ('h1' in subset and 'h2' in subset) or 
    ('d1' in subset and 'd2' in subset) or 
    ('t1' in subset and 't2' in subset) or
    (subset[0] != 'work') or
    (subset[6] != 'home')):
        continue
	
    durationWholeWay = 0
    routeValid = 1
    for i in range(0,6):
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
        routeMin = subset
        durationMin = durationWholeWay
	    
for waypoint in routeMin:
    if waypoint != 'work' and waypoint != 'home':
        print(waypoint, end = '')