# file: lemonpy/commands.py

import types

import style
from logging import Log
from directory import Directory
from session import Session
from config import Config

class Commands:

	commands = {}
	aliases = {
		"c" : ["clear"],
		"al" : ["alias"],
		"aa" : ["alias", "add"],
		"ar" : ["alias", "remove"],
		"dc" : ["directory", "change"],
		"dl" : ["directory", "list"],
		"ds" : ["directory", "stack"],
		"dt" : ["directory", "root"],
		"dp" : ["directory", "push"],
		"dd" : ["directory", "pop"],
		"dx" : ["directory", "drop"],
		"da" : ["directory", "add"],
		"dr" : ["directory", "remove"],
		"pe" : ["pyex"],
		"pi" : ["pyin"],
		"ph" : ["pyhelp"],
	}

	def __init__(self) -> None:
		self.__set_commands()

	def _call(self, line) -> None:
			args = line.split(' ')
			if args[0] in self.commands:
				return self.commands[args[0]](args[1:])
			if args[0] in self.aliases:
				alias = self.aliases[args[0]][0]
				alias_args = self.aliases[args[0]][1:] + args[1:]
				return self.commands[alias](alias_args)
			return line

	def __get_functions(self) -> any:
		for name, function in Commands.__dict__.items():
			if type(function) == types.FunctionType and not name.startswith('_'):
				yield name

	def __set_commands(self) -> None:
		for function in self.__get_functions():
			Commands.commands[function] = getattr(self, function)

	def __get_alias(self) -> any:
		for alias, command in Commands.aliases.items():
			yield alias, command

	def test(self, args:list) -> None:
		'''this is a test function'''
		for command in Commands.commands:
			print(command)

	# commands

	def alias(self, args:list) -> None:
		"""
command aliases\n
defualt:
	alias:\t\t\t list all aliases
subcommands:
	add <name> <command>:\t add command alias
	remove <name>:\t\t remove command alias
		"""
		if len(args) == 0:
			for alias, command in self.__get_alias():
				print(f"{style.yellow(alias)}\t{style.green(' '.join(command))}")
			return None
		if len(args) >= 2 and args[0] == "add":
			if args[1] not in Commands.aliases:
				Commands.aliases[args[1]] = list(args[2:])
				return None
			else:
				Log().error("alias", f"unable to add alias '{args[1]}'")
		if len(args) == 2 and args[0] == "remove":
			if args[1] in Commands.aliases:
				del Commands.aliases[args[1]]
			else:
				Log().error("alias", f"unable to remove alias '{args[1]}'")

	def command(self, args:list) -> None:
		"""
list all commands\n
defualt:
	command:\t\t list all commands
		"""
		if len(args) == 0:
			for command in self.__get_functions():
				print(f"{style.yellow(command)}")
			return None

	def help(self, args) -> None:
		'''
show help messages for commands\n
defualt:
	help:\t\t show a list of commands
	help <name>:\t show help for a command
		'''
		if len(args) == 0:
			print("\t".join(Commands.commands))
		if args[0] in Commands.commands:
			print(f"{args[0]}:\n\t{Commands.commands[args[0]].__doc__}")
		else:
			Log().error("help", f"unable to find help for '{args[0]}'")
		return None

	def clear(self, args) -> None:
		'''
clear the terminal window\n
defualt:
	clear:\t\t clear the terminal window
		'''
		print('\033[H\033[J')
		return None
	
	def pyin(self, args:list) -> None:
		try:
			args = " ".join(args)
			print(dir(args))
			return None
		except Exception as ex:
			Log().error("pyin", ex)

	def pyhelp(self, args:list) -> None:
		try:
			if len(args) == 0:
				help()
			else:
				args = " ".join(args)
				print(help(args))
			return None
		except Exception as ex:
			Log().error("pyin", ex)

	def pyex(self, args:list) -> None:
		try:
			args = " ".join(args)
			compile(args, '<stdin>', 'eval') # compile python with eval
		except SyntaxError: # if syntax error: either can't eval or not python syntax
			print(exec(args, Session().session)) # try exec python statement
			return None
		print(eval(args, Session().session)) # eval python expression
		return None

	def _pyex(self, args:list) -> any:
		try:
			compile(" ".join(args), '<stdin>', 'eval') # compile python with eval
		except SyntaxError: # if syntax error: either can't eval or not python syntax
			return exec # try exec python statement
		return eval # eval python expression

	# directory

	def directory(self, args:list) -> None:
		"""
handles directories and paths\n
defualt:
	directory:\t\t show the current directory
subcommands:
	change <path>:\t\t change directory
	list:\t\t\t list all aliased directories
	stack:\t\t\t list all directories in the stack
	root:\t\t\t set the stack root directory
	push <path>:\t\t push a directory to the stack or current directory
	pop:\t\t\t pop last directory from the stack
	drop <index>:\t\t drop a directory from the stack
	jump <index>:\t\t jump to a directory in the stack
	add <name> <path>:\t add a directory to the stack
	remove <name>:\t\t remove a directory from the stack
		"""
		if len(args) == 0:
			print(style.green(Directory().get_path()))
		elif len(args) == 2 and args[0] == "change":
			Directory().change_directory(str(args[1]))
		elif len(args) == 1 and args[0] == "list":
			print("\n".join(Directory().get_direcotries_list()))
		elif len(args) == 1 and args[0] == "stack":
			print("\n".join(Directory().get_stack_list()))
		elif len(args) == 2 and args[0] == "root":
			Directory().set_stack_root(str(args[1]))
		elif len(args) == 1 and args[0] == "push":
			Directory().push_directory()
		elif len(args) == 2 and args[0] == "push":
			Directory().push_directory(str(args[1]))
		elif len(args) == 1 and args[0] == "pop":
			Directory().pop_directory()
		elif len(args) == 2 and args[0] == "drop":
			Directory().drop_directory(int(args[1]))
		elif len(args) == 2 and args[0] == "jump":
			Directory().jump_directory(int(args[1]))
		elif len(args) == 2 and args[0] == "add":
			Directory().add_directory(str(args[1]))
		elif len(args) == 3 and args[0] == "add":
			Directory().add_directory(str(args[1]), str(args[2]))
		elif len(args) == 2 and args[0] == "remove":
			Directory().remove_directory(str(args[1]))
		return None

	# session

	def session(self, args:list) -> None:
		if len(args) == 0:
			print([item for item in Session().get_session()])
		elif len(args) == 1 and args[0] == "list":
			for item in Session().list_session():
				print(str(item))
		elif len(args) == 2 and args[0] == "list" and args[1] == "full":
			for item in Session().list_full_session():
				print(str(item))
		elif len(args) == 1 and args[0] == "save":
			Session().save_session()
		elif len(args) == 2 and args[0] == "save":
			Session().save_session(str(args[1]))
		elif len(args) == 2 and args[0] == "load":
			Session().load_session(str(args[1]))
		return None
	
	def config(self, args:list) -> None:
		if len(args) == 0:
			print(Config().config.sections())
		if len(args) == 1 and args[0] == "list":
			for item in Config().list():
				print(item)
		if len(args) == 2 and args[0] == "list" and args[1] == "full":
			for item in Config().list_full():
				print(item)	
		return None