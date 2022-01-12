# file: bmo/commands/clear.py

import lib.style as style

class Comamnd:

	def default(self, args:list) -> None:
		print("\033[H\033[J")
		return None

	def help(self, args:list) -> None:
		help = {
			"name": "clear",
			"description": "clear the terminal window",
			"default": {"clear" : "clear the terminal window"},
		}
		print(style.help(help))
		return None

def run() -> str:
	return Comamnd()