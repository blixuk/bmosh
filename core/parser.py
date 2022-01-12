# file: bmo/parser.py

import os
import importlib
import readline
from shlex import split

from core.logging import Log
from core.alias import Alias
from core.session import Session

debug = Log().debug
error = Log().error

class Parser:

	commands = {}
	aliases = {}
	completion = {}

	def __init__(self) -> None:
		self.get_commands()
		self.get_aliases()
		self.get_completion()

	def parse(self, args:list) -> any:
		if type(args) == str:
			line = args
			args = split(args)

		debug("parse : args", str(args))
		if args == []:
			return None # or [] ?

		if "|" in args:
			pipeline = self.make_pipeline(args)
			debug("parse : pipe : pipepline", str(pipeline))
			output = []
			debug("parse : pipe : output", str(output))
			for pipe in pipeline:
				debug("parse : pipe : pipe", str(pipe))
				output = self.parse(pipe + output)
				debug("parse : pipe : output", str(output))
			return None

		if args[0] in Parser.aliases:
			args = self.get_alias(args)
			debug("parse : alias", str(args))

		if args[0] in Parser.commands:
			debug("parse : command", str(args))
			return self.run_command(args)
		else:
			try:
				debug("parse : python", str(line))
				return self.run_python(line)(line, Session().session)
			except NameError:
				error('NameError', line)
				return line

	def run_command(self, args:list) -> any:
		command = importlib.import_module(Parser.commands[args[0]])
		debug("parse : command : command", str(command))
		debug("parse : command : subcommands", str(hasattr(command.run(), 'subcommands')))
		if len(args) == 1 or not hasattr(command.run(), 'subcommands'):
			debug("parse : command : 1", str(args))
			return command.run().default(args[1:])
		elif len(args) >= 2 and hasattr(command.run(), 'subcommands'):
			try:
				debug("parse : command : 2", str(args))
				return command.run().subcommands[args[1]](args[2:])
			except KeyError as e:
				debug("parse : command : KeyError", str(e))
				return command.run().help([])
		else:
			return args

	def get_alias(self, args:list) -> list:
		return Parser.aliases[args[0]].split(' ') + args[1:]

	def run_python(self, line:str) -> any:
		try:
			debug("parse : python : compile", str(line))
			compile(line, '<stdin>', 'eval') # compile python with eval
		except SyntaxError: # if syntax error: either can't eval or not python syntax
			debug("parse : python : exec", str(line))
			return exec # try exec python statement
		debug("parse : python : eval", str(line))
		return eval # eval python expression

	def make_pipeline(self, args:list) -> list:
		pipeline = []
		pipe = []
		for arg in args:
			if arg != "|":
				pipe.append(arg)
			else:
				pipeline.append(pipe)
				pipe = []
		pipeline.append(pipe)
		debug("parse : pipeline : string", str(pipeline))
		return pipeline

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
