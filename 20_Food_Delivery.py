import sys
import csv
import itertools

csvFile = open("files/3_2_delivery_service.csv")

data = [row for row in csv.reader(csvFile)]

waypoints = ['work', 'r1',  'r2',  'r3',  'r4',  'r5',  'c1',  'c2',  'c3',  'c4',  'c5', 'home']

durationMin = sys.maxsize
routeMin = []

for subset in itertools.permutations(waypoints[1:-1], 10):

    subset = list(subset)
    subset = ["work"] + subset + ["home"]

    if(subset.index("c1") < subset.index("r1") or
    subset.index("c2") < subset.index("r2") or
    subset.index("c3") < subset.index("r3") or
    subset.index("c4") < subset.index("r4") or
    subset.index("c5") < subset.index("r5")):
        continue

    # Only one shop per type allowed.
    mealCounter = 0
    mealLoadError = 0

    for i in range(1,10):
    
        if('r' in subset[i]):
            mealCounter += 1
        elif('c' in subset[i]):
            mealCounter -= 1
        
        if(mealCounter > 3 or mealCounter < 0):
            mealLoadError = 1
            break

    if mealLoadError:
        continue
    
    durationWholeWay = 0
    routeValid = 1
    for i in range(0,11):
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