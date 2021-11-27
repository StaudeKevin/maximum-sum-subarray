"""
task:

	The task is to assign each letter of the alphabet to a number, 
	so that A = -5, B = -4 ... until Z = 20. 

	Write a python program that allows people to enter a list of letters 
	and the code returns the greatest number possible from a consecutive substring of the letters.

	If the input letters were: ‘ACFTUTZB’, it would scan all consecutive substrings 
	and return ‘TUTZ’ as the consecutive string, with the greatest number = (14+15+14+20)

best solution:

	If you replace the string with an array whose each element is the value of character 
	you will get an array of integers. Now this problem is reduced to this:
	https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""

# import string to get the lowercase letters from a to z with string.ascii_lowercase
import string

def create_dictionary(start_number):
	"""Die Funktion ordnet jedem Buchstaben des Alphabets eine Zahl zu und speichert diese in d_abc"""
	abc = string.ascii_lowercase
	
	i = start_number
	for letter in abc:
		d_abc[letter] = i
		i += 1

def find_all_combinations(input_letters, a, b):
	"""
	Die rekursive Funktion findet jede mögliche Kombination der Buchstabenfolge der input_letters
	und fügt sie in die Liste combinations hinzu.

	1. Durchlauf: [0:1], [0:2], ..., [0:len(input_letters)]
	2. Durchlauf: [1:2], [1:3], ..., [1:len(input_letters)]
	...
	letzer Durchlauf: [len(input_letters)-1:len(input_letters)] -> letzer Buchstabe der input_letters

	Beispiel: input_letters = "abc" -> ['a', 'ab', 'abc', 'b', 'bc', 'c']
	"""
	input_letters = input_letters.lower()

	newb = b
	while b <= len(input_letters):
		combinations.append(input_letters[a:b])
		b += 1

	a += 1
	newb += 1
	if a < len(input_letters):
		find_all_combinations(input_letters, a, newb)
	else:
		pass

def get_value():
	"""
	Die Funktion weist (in d_combinations) jede Kombination aus combinations 
	ihren aufsummierten Wert anhand von d_abc zu.
	"""
	for combi in combinations:
		summe = 0
		for character in combi:
			summe += d_abc[character]
		d_combinations[combi] = summe

def get_max():
	"""
	Die Funktion findet die keys in d_combinations, die die höchste
	max_value haben. Diese werden in solutions zwischengespeichert.
	Der key mit der kürzeste Länge wird returned.

	Beispiel: solutions = ['ftutz', 'tutz'] mit jeweils value von 63 -> return tutz
	"""
	solutions = []
	max_value = max(d_combinations.values())

	for combi in d_combinations:
		if d_combinations[combi] == max_value:
			solutions.append(combi)
		else:
			pass

	return min(solutions, key=len)

def main():
	"""Die main Funktion um alle vier Teilschritte auszuführen"""
	create_dictionary(-5)
	find_all_combinations(input_letters, 0, 1)
	get_value()
	print(get_max().upper())


# dictionary of the alphabet with values
d_abc = {}

# list of all possible combinations
combinations = []

# dictionary of all possible combinations with values
d_combinations = {}

# the input letters or word
input_letters = "ACFTUTZB"

# main function
main()
