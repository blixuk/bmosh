# file: bmo/commands/help.py

import importlib
import types
import os

from logging import Log

class Command:
	'''
show help messages for commands\n
defualt:
	help:\t\t show a list of commands
	help <name>:\t show help for command
	'''

	commands = {}

	def __init__(self) -> None:
		for name in os.listdir("commands"):
			path = f"commands/{name}"
			if os.path.isfile(path):
				basename = os.path.basename(path)
				base, extension = os.path.splitext(path)
				if extension == ".py" and not basename.startswith("_"):
					Command.commands[name[:-3]] = base.replace("/", ".")
		return None

	def default(self, args:list=[]) -> None:
		if len(args) == 1 and args[0] in Command.commands:
			command = importlib.import_module(f"commands.{args[0]}")
			print(f"{args[0]}:\n\t{command.run().__doc__}")
		elif len(args) == 0:
			print("    ".join(Command.commands))
		else:
			Log().error("help", f"unable to find help for '{args[0]}'")
		return None

def run() -> Command:
	return Command()
