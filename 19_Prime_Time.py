validRoomNumbers = [1]
currentIndex = 0
primeFactors = [7, 11, 13]

while True:
    
    # Generate the next valid room number candidates from the allowed prime factors.
    candidates = []
    for primeFactor in primeFactors:
        candidates.append(validRoomNumbers[currentIndex] * primeFactor)

    # For each candidate, check if it already exists in the list. If not, append it and re-sort
    # the list to maintain ascending order.
    for candidate in candidates:
        if not candidate in validRoomNumbers:
            validRoomNumbers.append(candidate)
            validRoomNumbers.sort()
            if len(validRoomNumbers) > 199:
                # 200th room's room number is searched, print it.
                print(validRoomNumbers[-1])
                exit()

    currentIndex += 1