# file: bmo/prompt.py

from datetime import datetime
import os

from directory import Directory
import style

class Prompt:

	def __init__(self) -> None:
		self.time_date_format = "[%d/%m/%Y %H:%M:%S]"
		self.carrot = '>'

	def prompt(self, count) -> str:
		return f"{style.green(Directory().get_path())}{self.space()}{self.date_time()}\n[{count}]{self.carrot} "

	def date_time(self) -> str:
		return datetime.now().strftime(self.time_date_format)

	def space(self) -> str:
		columns, rows = os.get_terminal_size()
		space_size = (columns - (len(self.date_time()) + len(Directory().get_path())))
		return str(' ' * space_size)