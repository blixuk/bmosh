# file: bmo/commands/echo.py

import types

import lib.style as style

class Command:

	def __init__(self) -> None:
		pass

	def default(self, args:list) -> None:
		print("\n".join(args))
		return None

	def help(self, args:list) -> None:
		help = {
			"name": "echo",
			"description": "echo echo echo",
			"default": {"echo" : "echo..."},
		}
		print(style.help(help))
		return None

def run() -> Command:
	return Command()
