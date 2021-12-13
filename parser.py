# file: bmo/command.py

import os
import importlib

from logging import Log
from alias import Alias
from session import Session

class Parser:

	commands = {}
	aliases = {}

	def __init__(self) -> None:
		self.get_commands()
		self.get_aliases()

	def parse(self, line:str) -> any:
		if line == "":
			return None

		args = line.split(' ')

		if args[0] in Parser.aliases:
			alias = Parser.aliases[args[0]].split(' ')
			command = importlib.import_module(Parser.commands[alias[0]])
			if len(alias) == 1:
				return command.run().default()
			elif len(alias) >= 2:
				return command.run().subcommands[alias[1]](args[2:])
			else:
				return line
		else:
			if args[0] in Parser.commands:
				command = importlib.import_module(Parser.commands[args[0]])
				if len(args) == 1 or not hasattr(command.run(), 'subcommands'):
					return command.run().default(args[1:])
				elif len(args) >= 2:
					try:
						return command.run().subcommands[args[1]](args[2:])
					except KeyError:
						return command.run().help([])
				else:
					return line
			else:
				try:
					return self.py_exec(line)(line, Session().session)
				except NameError:
					return line
					Log().error('NameError', line)

	def get_commands(self) -> None:
		for name in os.listdir("commands"):
			path = f"commands/{name}"
			if os.path.isfile(path):
				basename = os.path.basename(path)
				base, extension = os.path.splitext(path)
				if extension == ".py" and not basename.startswith("_"):
					Parser.commands[name[:-3]] = base.replace("/", ".")

	def get_aliases(self) -> None:
		for alias, value in Alias().list_full():
			Parser.aliases[alias] = value

	def py_exec(self, args:list) -> any:
		try:
			compile(" ".join(args), '<stdin>', 'eval') # compile python with eval
		except SyntaxError: # if syntax error: either can't eval or not python syntax
			return exec # try exec python statement
		return eval # eval python expression
