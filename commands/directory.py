# file: bmo/commands/directory.py

import types

import style
from directory import Directory

class Command:
	'''
	directory
	'''

	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None

	def default(self):
		print(style.green(Directory().get_path()))
		return None

	def change(self, args:list) -> None:
		'''
		directory change
		'''
		if len(args) == 1:
			Directory().change(str(args[0]))
		else:
			Directory().change()
		return None

	def list(self, args:list) -> None:
		'''
		directory list
		'''
		for name, path in Directory().get_directories():
			print(f'[{style.yellow(str(name))}] {style.green(str(path))}')
		return None

	def stack(self, args:list) -> None:
		for count, path in enumerate(Directory().get_stack()):
			print(f"[{style.yellow(str(count))}] {style.green(str(path))}")
		return None

	def root(self, args:list) -> None:
		if len(args) == 1:
			Directory().set_root(str(args[0]))
		return None

	def push(self, args:list) -> None:
		if len(args) == 1:
			Directory().push(str(args[0]))
		else:
			Directory().push()
		return None

	def pop(self, args:list) -> None:
		Directory().pop()
		return None

	def drop(self, args:list) -> None:
		if len(args) == 1:
			Directory().drop(int(args[0]))
		return None

	def jump(self, args:list) -> None:
		if len(args) == 1:
			Directory().jump(int(args[0]))
		return None

	def add(self, args:list) -> None:
		if len(args) == 2:
			Directory().add(str(args[0]), str(args[1]))
		elif len(args) == 1:	
			Directory().add(str(args[0]))
		return None

	def remove(self, args:list) -> None:
		if len(args) == 1:
			Directory().remove(str(args[0]))
		return None

def run() -> Command:
	return Command()