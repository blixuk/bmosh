# file: bmo/commands/alias.py

import types

import style
from alias import Alias

class Command:
	'''
	alias
	'''

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None
	
	def default(self, args:list=[]) -> None:
		if len(args) == 0:
			for alias in Alias().list():
				print(f"{style.green(alias)}")
		return None

	def load(self, args:list) -> None:
		Alias().load()
		return None

	def save(self, args:list) -> None:
		Alias().save()
		return None

	def list(self, args:list) -> None:
		if len(args) == 0:
			for alias in Alias().list():
				print(f"{style.green(alias)}")
		elif len(args) == 1 and args[0] == "full":
			for alias, value in Alias().list_full():
				print(f"[{style.yellow(alias)}] {style.green(value)}")
		return None

	def add(self, args:list) -> None:
		if len(args) >= 2:
			Alias().add(args[0], args[1:])

	def remove(self, args:list) -> None:
		if len(args) == 1:
			Alias().remove(args[0])

def run() -> Command:
	return Command()
