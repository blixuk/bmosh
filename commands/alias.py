# file: bmo/commands/alias.py

import types

import style
from alias import Alias

class Command:

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None
	
	def default(self, args:list=[]) -> None:
		if len(args) == 0:
			print("\n".join([f"{style.green(alias)}" for alias in Alias().list()]))
		return None

	def load(self, args:list) -> None:
		Alias().load()
		return None

	def save(self, args:list) -> None:
		Alias().save()
		return None

	def list(self, args:list) -> None:
		if len(args) == 0:
			print("\n".join([f"{style.green(alias)} -> {style.yellow(value)}" for alias, value in Alias().list_full()]))
		return None

	def add(self, args:list) -> None:
		if len(args) >= 2:
			Alias().add(args[0], args[1:])

	def remove(self, args:list) -> None:
		if len(args) == 1:
			Alias().remove(args[0])

	def help(self, args:list) -> None:
		help = {
			"name": "alias",
			"description": "alias manager",
			"default": {"alias" : "prints a list of all aliases"},
			"subcommands": {
				"list" : "prints a full list of all aliases",
				"add <name> <commands>" : "add an alias",
				"remove <name>" : "remove an alias",
			}
		}
		print(style.help(help))
		return None

def run() -> Command:
	return Command()
