# file: bmo/commands/test.py

import types

import style

class Command:

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None

	def default(self, args:list) -> None:
		print('default')
		return None

	def test(self, args:list) -> None:
		print("test")
		return None

	def hello(self, args:list) -> None:
		print(args)
		return None

	def help(self, args:list) -> None:
		help = {
			"name": "test",
			"description": "a test command to test the commands",
			"default": {"test" : "prints default"},
			"subcommands": {
				"test" : "prints test",
				"hello <op:args>" : "prints args",
			}
		}
		print(style.help(help))
		return None

def run() -> Command:
	return Command()
