"""
File: boggle.py
Name: Luke
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = {}
board = []
found_list = []


def main():
	global board
	is_illegal = False  # For checking input and exiting program.
	read_dictionary()
	for i in range(4):
		char_list = input(f'{i+1} row of letters:').lower().strip().split()
		if len(char_list) != 4:
			is_illegal = True
		for char in char_list:  # Check each element contains only 1 char and is alphabetic string.
			if len(char) != 1 or char.isalpha() is False:
				is_illegal = True
				break
		if is_illegal is True:
			print('Illegal input')
			break
		else:
			board.append(char_list)
	if is_illegal is not True:  # Start word search.
		for i in range(4):
			for j in range(4):
				word = board[i][j]  # Start loop for each letter on board.
				path = [(i, j)]  # Log path so letters are not reused.
				find_word(i, j, word, path)  # Start recursive function.
		print(f'There are {len(found_list)} words in total.')


def find_word(i, j, word, path):
	"""
	Recursive function to find word on board and log path so letters are not reused.
	:param i: Row to run from, 0~3.
	:param j: Column to run from, 0~3.
	:param word: Current found string of letters.
	:param path: List of tuples of coordinates used during current word.
	:return: Nothing.
	"""
	global found_list
	word_length = len(word)
	if word in dictionary[word_length] and word not in found_list and word_length > 3:  # Base Case! Print word and append to list.
		print(f'Found "{word}"')
		found_list.append(word)
	if has_prefix(word) is True:  # Recursive Case condition is if current word is prefix of any dictionary word.
		for m in range(-1, 2):  # Go through adjacent columns.
			for n in range(-1, 2):  # Go through adjacent rows.
				x = i+m
				y = j+n
				if 0 <= x <= 3 and 0 <= y <= 3 and (x, y) not in path:  # Check position is on board and not used.
					word += board[x][y]  # Choose
					path.append((x, y))  # Log path
					find_word(x, y, word, path)  # Explore
					path.pop()  # Un-log path
					word = word[:-1]  # Un-choose


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			word_length = len(word)  # Word length will be used as dictionary key, so data will be grouped.
			if word_length not in dictionary:  # Create list if not existing for word_length.
				dictionary[word_length] = []
			dictionary[word_length].append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for key in dictionary.keys():
		for word in dictionary[key]:
			if word.startswith(sub_s) is True:
				return True
	return False


if __name__ == '__main__':
	main()
