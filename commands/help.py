# file: bmo/commands/help.py

import importlib
import os

import style

from logging import Log

class Command:

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
			command.run().help([])
		elif len(args) == 0:
			print("    ".join(Command.commands))
		else:
			Log().error("help", f"unable to find help for '{args[0]}'")
		return None

	def help(self, args:list) -> None:
		help = {
			"name": "help",
			"description": "show help messages for commands",
			"default": {"help <op:name>" : "show a list of commands or help for a specified command"},
		}
		print(style.help(help))
		return None

def run() -> Command:
	return Command()
