# file: bmo/commands/py.py

import types

from session import Session

class Command:
	'''
	python
	'''

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None

	def default(self):
		help()
		return None

	def help(self, args:list) -> None:
		if len(args) == 1:
			args = " ".join(args)
			help(args)
			return None
		else:
			help()
			return None

	def exec(self, args:list) -> None:
		try:
			args = " ".join(args)
			compile(args, '<stdin>', 'eval') # compile python with eval
		except SyntaxError: # if syntax error: either can't eval or not python syntax
			print(exec(args, Session().session)) # try exec python statement
			return None
		print(eval(args, Session().session)) # eval python expression
		return None

	# def dir(self, args:list) -> None:
	# 	if len(args) == 1:
	# 		args = " ".join(args)
	# 		print(dir(args))
	# 		return None
	# 	else:
	# 		print(dir(self))
	# 		return None

def run() -> Command:
	return Command()
