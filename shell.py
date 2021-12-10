# file: bmo/shell.py

from os import dup
import sys
from typing import final

import style
from config import Config
from prompt import Prompt
from parser import Parser
from session import Session
from alias import Alias
from history import History
from logging import Log

debug = Log().debug
log = Log().log

class Shell:

	def __init__(self) -> None:
		pass

	def loop(self) -> None:
		self.on_start()
		for count, _ in enumerate(iter(bool, True)):
			try:
				line = input(Prompt().prompt(count))
				debug("loop", str(line))
				self.pre_loop(count, line)
			except KeyboardInterrupt:
				debug("KeyboardInterrupt", "exit clean!")
				self.exit_handler("KeyboardInterrupt")
			except EOFError:
				debug("EOFError")
			except SystemExit:
				debug("SystemExit", "exit clean!")
				self.on_exit("SystemExit")

	def pre_loop(self, count:int, line:str) -> any:
		debug("pre_Loop_in", str(line))
		History().add(line)
		line = Parser().parse(line)
		if line is not None:
			self.main_loop(count, line)
		debug("pre_Loop_out", str(line))

	def main_loop(self, count:int, line:str) -> any:
		debug("main_Loop_in", str(line))
		if line is not None:
			self.post_loop(count, line)
		else:
			log("main_Loop", str(line))
		debug("main_Loop_out", str(line))

	def post_loop(self, count:int, line:str) -> any:
		debug("post_Loop_in", str(line))
		if line is not None:
			print(line)
		else:
			log("post_Loop", str(line))
		debug("post_Loop_out", str(line))

	def on_start(self) -> None:
		Config().load()
		Alias().load()
		History().load()
		Session().load()
		print('\033[H\033[J')

	def on_exit(self, message:str="") -> None:
		Config().save()
		Alias().save()
		History().save()
		Session().save()
		log("exit", message)
		sys.exit(0)

	def exit_handler(self, message:str) -> None:
		responce = input(style.red("Do you want to exit? [y/n] "))
		if responce in ["y", "Y", "yes", "Yes", "YES"]:
			self.on_exit(message)