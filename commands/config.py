# file: bmo/commands/config.py

import types

import style
from config import Config

class Command:

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None

	def default(self, args:list) -> None:
		print("\n".join([item for item in Config().list()]))
		return None

	def list(self, args:list) -> None:
		print("\n".join([item for item in Config().list_full()]))
		return None

	def help(self, args:list) -> None:
		help = {
			"name": "config",
			"description": "manage configs",
			"default": {"config" : "prints a list of configs"},
			"subcommands": {
				"list" : "print a list of configs and their values",
			}
		}
		print(style.help(help))
		return None

def run() -> Command:
	return Command()
