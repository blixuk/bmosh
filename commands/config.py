# file: bmo/commands/config.py

import types

from config import Config

class Command:
	'''
	config
	'''

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None

	def default(self, args:list) -> None:
		'''
		print a list of configs
		'''
		print([item for item in Config().list()])
		return None

	def list(self, args:list) -> None:
		'''
		print a list of configs and their values
		'''
		print([item for item in Config().list_full()])
		return None

def run() -> Command:
	return Command()
