# file: bmo/__main__.py

from command import Command
cmd = Command(description="BMO Shell")

class App:

	def __init__(self):
		pass

if __name__ == '__main__':
	cmd.parse()