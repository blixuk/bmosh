# file: bmo/history.py

import os
from datetime import datetime

from directory import Directory

class History:

	history = []
	history_path = Directory().get_directory('history')
	date_time:datetime = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")

	def __init__(self) -> None:
		pass

	def add(self, line:str) -> None:
		if line not in ["", " ", "\t", "\n"] and line not in History.history:
			History.history.append(line.strip())
		return None

	# def remove(self, index:int) -> None:
	# 	History.history.pop(index)
	# 	return None

	def clear(self) -> None:
		History.history = []
		return None

	def get_line(self, index:int) -> str:
		return History.history[index]

	def get_last(self) -> str:
		return History.history[-1]

	def make_history(self) -> None:
		if not os.path.isfile(History.history_path):
			with open(History.history_path, 'w') as f:
					f.write(f"[created]{History.date_time}")
		return None

	def save(self) -> None:
		History.history.append(f"[closed]{History.date_time}")
		with open(History.history_path, 'w') as f:
			for line in History.history:
				f.write(f"{line}\n")
		return None

	def load(self) -> None:
		if not os.path.isfile(History.history_path):
			self.make_history()
		with open(History.history_path, 'r') as f:
			for line in f:
				if line not in ["", " ", "\t", "\n"]:
					History.history.append(line.strip())
		History.history.append(f"[opened]{History.date_time}")
		return None