# file: bmo/shell.py

from prompt import Prompt
from commands import Commands
from session import Session
from logging import Log

class Shell:

	def __init__(self) -> None:
		Session().load_session('main')
		self.command = Commands()
		print('\033[H\033[J')

	def loop(self) -> None:
		for count, _ in enumerate(iter(bool, True)):
			try:
				line = input(Prompt().prompt(count))
				self.pre_loop(count, line)
			except KeyboardInterrupt:
				break
			except EOFError:
				break

	def pre_loop(self, count:int, line:str) -> any:
		line = self.command._call(line)
		if line is not None:
			self.main_loop(count, line)
		return count, line

	def main_loop(self, count:int, line:str) -> any:
		try:
			line = self.command._pyex(line)(line, Session().session)
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