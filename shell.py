# file: bmo/shell.py

from prompt import Prompt
from command import Command
from session import Session
from logging import Log
from config import Config
from alias import Alias

class Shell:

	def __init__(self) -> None:
		pass

	def loop(self) -> None:
		self.on_start()
		for count, _ in enumerate(iter(bool, True)):
			try:
				line = input(Prompt().prompt(count))
				self.pre_loop(count, line)
			except KeyboardInterrupt:
				self.on_exit()
				break
			except EOFError:
				self.on_exit()
				break

	def pre_loop(self, count:int, line:str) -> any:
		line = Command().call(line)
		if line is not None:
			self.main_loop(count, line)
		return count, line

	def main_loop(self, count:int, line:str) -> any:
		try:
			line = Command()._pyex(line)(line, Session().session)
		except NameError:
			Log().error('NameError', line)
		if line is not None:
			self.post_loop(count, line)
		return count, line

	def post_loop(self, count:int, line:str) -> any:
		if line is not None:
			print(line)
		else:
			Log().log("Loop", line)
		return count, line

	def on_start(self) -> None:
		Config().load()
		Alias().load()
		Session().load()
		print('\033[H\033[J')

	def on_exit(self) -> None:
		Config().save()