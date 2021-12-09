# file: bmo/commands/test.py

import types

class Command:
	'''
	test command
	'''

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None

	def default(self):
		print('default')
		return None

	def test(self, args:list) -> None:
		print("test")
		return None

	def hello(self, args:list) -> None:
		print(args)
		return None

def run() -> Command:
	return Command()
