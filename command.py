# file: bmo/command.py

import os
import importlib

import style
from logging import Log
from alias import Alias

class Command:

	commands = {}

	def __init__(self) -> None:
		for name in os.listdir("commands"):
			path = f"commands/{name}"
			if os.path.isfile(path):
				basename = os.path.basename(path)
				base, extension = os.path.splitext(path)
				if extension == ".py" and not basename.startswith("_"):
					Command.commands[name[:-3]] = base.replace("/", ".")

	def _call(self, line) -> None:
			args = line.split(' ')
			if args[0] in self.commands:
				return self.commands[args[0]](args[1:])
			if args[0] in self.aliases:
				alias = self.aliases[args[0]][0]
				alias_args = self.aliases[args[0]][1:] + args[1:]
				return self.commands[alias](alias_args)
			return line

	def call(self, line:str) -> any:
		if line == "":
			return None
		args = line.split(' ')
		if Alias().exists(args[0]):
			alias = Alias().get_alias(args[0]).split(' ')
			command = importlib.import_module(Command.commands[alias[0]])
			if len(alias) == 1:
				return command.run().default()
			elif len(alias) >= 2:
				return command.run().subcommands[alias[1]](args[2:])
			else:
				return line
		elif args[0] in Command.commands:
			command = importlib.import_module(Command.commands[args[0]])
			if args[0] == "help":
				return command.run().default(args[1:])
			elif len(args) == 1:
				return command.run().default([])
			elif len(args) >= 2:
				return command.run().subcommands[args[1]](args[2:])
			else:
				return line
		else:
			#Log().error("command", f"no command named '{args[0]}'")
			return line

# 	def alias(self, args:list) -> None:
# 		"""
# command aliases\n
# defualt:
# 	alias:\t\t\t list all aliases
# subcommands:
# 	add <name> <command>:\t add command alias
# 	remove <name>:\t\t remove command alias
# 		"""
# 		if len(args) == 0:
# 			for alias, command in self.__get_alias():
# 				print(f"{style.yellow(alias)}\t{style.green(' '.join(command))}")
# 			return None
# 		if len(args) >= 2 and args[0] == "add":
# 			if args[1] not in Commands.aliases:
# 				Commands.aliases[args[1]] = list(args[2:])
# 				return None
# 			else:
# 				Log().error("alias", f"unable to add alias '{args[1]}'")
# 		if len(args) == 2 and args[0] == "remove":
# 			if args[1] in Commands.aliases:
# 				del Commands.aliases[args[1]]
# 			else:
# 				Log().error("alias", f"unable to remove alias '{args[1]}'")

	def alias(self, args:list) -> None:
		if len(args) == 0:
			for alias in Alias().list():
				print(alias)
		if len(args) == 1 and args[0] == "list":
			for alias in Alias().list_full():
				print(alias)
		if len(args) >= 2 and args[0] == "add":
			Alias().add(args[1], args[2:])
		if len(args) >= 2 and args[0] == "remove":
			Alias().remove(args[1])

	def _pyex(self, args:list) -> any:
		try:
			compile(" ".join(args), '<stdin>', 'eval') # compile python with eval
		except SyntaxError: # if syntax error: either can't eval or not python syntax
			return exec # try exec python statement
		return eval # eval python expression
