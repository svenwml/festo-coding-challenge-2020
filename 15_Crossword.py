import re
import string
import itertools

# These are the regular expressions that the permutations of 3 characters
# generated from the pool of characters have to match.

patternsRows = []
patternsRows.append(r"(R|A|Z)+(AC|AI|CC|CF)+")
patternsRows.append(r"(Y|O|C)*K[LI]+")
patternsRows.append(r"[^RKC]{0,1}(I|F|ZE|R)+")

patternsColumns = []
patternsColumns.append(r"[RLY]{1,2}[RCKZ]{1,2}")
patternsColumns.append(r"[CODNG]+[CHALLENGE]+")
patternsColumns.append(r"^(?!.*?(.).*?\1)[FESTOAIR]*$")

# Get all permutations of 3 upper case characters.

characterPoolPermutations = []

for subset in itertools.permutations(string.ascii_uppercase, 3):
	characterPoolPermutations.append(subset)

# From the character pool permutations, for each row, get the
# permutations that match the given regular expression.

permutations_rows = [[],[],[]]

for subset in characterPoolPermutations:
	for i in range(len(patternsRows)):
		regex = re.compile(patternsRows[i])
		matches = regex.match(subset[0] + subset[1] + subset[2])
		
		if(matches):
			if(matches.span() == (0,3)):
				permutations_rows[i].append(subset)

# Generate all possible combinations for the rows

rowCombinations = []

for i in range(len(permutations_rows[0])):
	for j in range(len(permutations_rows[1])):
		for k in range(len(permutations_rows[2])):
			combination = permutations_rows[0][i] + permutations_rows[1][j] + permutations_rows[2][k]
			rowCombinations.append(combination)

# Now verify each column for each row combination
for i in range(len(rowCombinations)):
    
	matches = 0
	for j in range(3):
		column = rowCombinations[i][0+j] + rowCombinations[i][3+j] + rowCombinations[i][6+j]
	
		regex = re.compile(patternsColumns[j])
	
		matches = regex.match(column[0] + column[1] + column[2])
	
		if(matches and matches.span() == (0,3)):
			pass
		else:
			matches = 0
			break
			
	if(matches):
		for j in range(9):
			print(rowCombinations[i][j], end='')
			pass