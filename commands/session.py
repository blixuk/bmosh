# file: bmo/commands/session.py

import types

import style
from session import Session

class Command:

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None

	def default(self, args:list) -> None:
		print([item for item in Session().get()])
		return None

	def list(self, args:list) -> None:
		if len(args) == 1 and args[0] == 'full':
			for item in Session().list_full():
				print(item)
		else:
			for item in Session().list():
				print(item)
		return None

	def save(self, args:list) -> None:
		if len(args) == 1:
			Session().save(str(args[0]))
		else:
			Session().save()
		return None
	
	def load(self, args:list) -> None:
		if len(args) == 1:
			Session().save(str(args[0]))
		else:
			Session().save()
		return None

	def help(self, args:list) -> None:
		help = {
			"name": "session",
			"description": "session manager",
			"default": {"session" : "print the current session"},
			"subcommands": {
				"list" : "print a list of the current session",
				"list full" : "print a full list of the current session",
				"save <op:name>" : "save the current session or a custom session",
				"load <op:name>" : "load the default session or load a custom session"
			}
		}
		print(style.help(help))
		return None

def run() -> Command:
	return Command()
