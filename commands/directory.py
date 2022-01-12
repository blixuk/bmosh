# file: bmo/commands/directory.py

import types

import lib.style as style
from core.directory import Directory

class Command:
	
	subcommands = {}

	def __init__(self) -> None:
		for name, function in Command.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				Command.subcommands[name] = getattr(self, name)
		return None

	def default(self, args:list) -> None:
		print(style.green(Directory().get_path()))
		return None

	def change(self, args:list) -> None:
		if len(args) == 1:
			Directory().change(str(args[0]))
		else:
			Directory().change()
		return None

	def list(self, args:list) -> None:
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

	def help(self, args:list) -> None:
		help = {
			"name": "directory",
			"description": "a command for managing and navigating directories",
			"default": {"directory" : "prints the current directory"},
			"subcommands": {
				"change <op:path>" : "changes directory to the specified path or home directory",
				"list" : "list all saved directories",
				"stack" : "list all directories in the stack",
				"root <path>" : "set the root directory of the stack",
				"push <op:path" : "push specified directory onto the stack or current directory",
				"pop" : "pop the top directory from the stack",
				"drop <index>" : "drop the directory at the specified index from the stack",
				"jump <index>" : "change directory to the specified index in the stack",
				"add <name> <op:path>" : "add directory to saved directories or current directory",
				"remove <name>" : "remove specified directory from saved directories",
			}
		}
		print(style.help(help))
		return None

def run() -> Command:
	return Command()
