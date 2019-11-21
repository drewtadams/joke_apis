# joke APIs pulled from https://www.programmableweb.com/category/humor/api
import joke_apis as j
import sys


def main():
	jokes = j.Jokes(sys.argv)
	print(f'\n\n{jokes.tell()}\n\n')
	# print(jokes.icanhazdadjoke())


if __name__ == '__main__':
	main()