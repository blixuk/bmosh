# file: bmo/prompt.py

from datetime import datetime
import os

import style
from directory import Directory
from config import Config

class Prompt:

	date_time_format:str = Config().config.get("prompt", "date_time_format")
	date_time:bool = Config().config.getboolean("prompt", "date_time")
	carrot:str = Config().config.get("prompt", "carrot")
	count_format:str = Config().config.get("prompt", "count_format")
	count:bool = Config().config.getboolean("prompt", "count")

	def __init__(self) -> None:
		pass

	def prompt(self, count) -> str:
		count = Prompt.count_format.replace("@", count) if Prompt.count else ""
		date_time = self.get_date_time() if Prompt.date_time else ""
		return f"{style.blue(Directory().get_path())}{self.space()}{date_time}\n{count}{Prompt.carrot} "

	def get_date_time(self) -> str:
		return datetime.now().strftime(Prompt.date_time_format)

	def space(self) -> str:
		columns, rows = os.get_terminal_size()
		space_size = (columns - (len(self.get_date_time()) + len(Directory().get_path())))
		return str(' ' * space_size)