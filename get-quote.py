import random

def primary():
	# print("Keep it logically awesome.")

	f = open("quotes.txt", "r+")
	quotes = f.readlines()
	f.close()

	last = 13
	rnd = random.randint(0, last)
	print(quotes[rnd])


if __name__== "__main__":
	primary()
