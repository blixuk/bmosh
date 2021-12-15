# file: bmo/parser.py

import os
import importlib
import readline

from logging import Log
from alias import Alias
from session import Session

class Parser:

	commands = {}
	aliases = {}
	completion = {}

	def __init__(self) -> None:
		self.get_commands()
		self.get_aliases()
		self.get_completion()

	def parse(self, line:str) -> any:
		if line == "":
			return None

		args = line.strip().split(' ')

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

	def py_exec(self, args:list) -> any:
		try:
			compile(" ".join(args), '<stdin>', 'eval') # compile python with eval
		except SyntaxError: # if syntax error: either can't eval or not python syntax
			return exec # try exec python statement
		return eval # eval python expression

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

	def get_completion(self) -> None:
		for name in Parser.commands:
			if name in Parser.commands:
				Parser.completion[name] = []
				command = importlib.import_module(Parser.commands[name])
				if hasattr(command.run(), 'subcommands'):
					for subcommand in command.run().subcommands:
						subcommands = Parser.completion[name]
						if subcommand != "default":
							subcommands.append(subcommand)
						Parser.completion[name] = subcommands

	def basic_completer(self, text:str, state:int) -> str:
		result = [x for x in Parser.completion if x.startswith(text)] + [None]
		return result[state]

	def advanced_completer(self, text:str, state:int) -> str:
		try:
			tokens = readline.get_line_buffer().split(" ")
			if tokens == []:
				results = []
			elif len(tokens) == 1:
				results = [x+" " for x in Parser.completion if x.startswith(tokens[0])] + [None]
			else:
				results = [x+" " for x in Parser.completion[tokens[0]] if x.startswith(tokens[1])] + [None]
			return results[state]
		except Exception as e:
			print('ERROR:', e)
