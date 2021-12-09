# file: bmo/commands/clear.py

class Comamnd:
	'''
clear the terminal window\n
defualt:
	clear:\t\t clear the terminal window
	'''

	def default(self, args:list) -> None:
		print("\033[H\033[J")
		return None

def run() -> str:
	return Comamnd()