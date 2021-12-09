# file: bmo/commands/session.py

import types

from session import Session

class Command:
	'''
	session
	'''

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None

	def default(self, args:list) -> None:
		'''
		print the current session
		'''
		print([item for item in Session().get()])
		return None

	def list(self, args:list) -> None:
		'''
		print a list of the current session
			session list
		print a full list of the current session
			session list full
		'''
		if len(args) == 1 and args[0] == 'full':
			for item in Session().list_full():
				print(item)
		else:
			for item in Session().list():
				print(item)
		return None

	def save(self, args:list) -> None:
		'''
		save the current session
			session save
		save a custom session
			session save <name>
		'''
		if len(args) == 1:
			Session().save(str(args[0]))
		else:
			Session().save()
		return None
	
	def load(self, args:list) -> None:
		'''
		load the defualt session
			session load
		load a custom session
			session load <name>
		'''
		if len(args) == 1:
			Session().save(str(args[0]))
		else:
			Session().save()
		return None


def run() -> Command:
	return Command()
