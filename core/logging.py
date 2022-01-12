# file: bmo/logging.py

from datetime import date, datetime

import lib.style as style
from core.config import Config
from core.history import History

class Log:

	debugging_option:bool = Config().config.getboolean("logging", "debug")
	logging_option:bool = Config().config.getboolean("logging", "log")
	history_option:bool = Config().config.getboolean("logging", "history")
	date_time_format:str = Config().config.get("logging", "time_date_format")
	date_time:datetime = datetime.now().strftime(date_time_format)

	def __init__(self) -> None:
		pass

	def set_debug(self, option:bool) -> None:
		Log.debugging_option = option
		Config().config.set("logging", "debug", str(option))

	def get_debug(self) -> bool:
		return Log.debugging_option

	def set_logging(self, option:bool) -> None:
		Log.logging_option = option
		Config().config.set("logging", "log", str(option))

	def get_logging(self) -> bool:
		return Log.logging_option

	def set_history(self, option:bool) -> None:
		Log.history_option = option
		Config().config.set("logging", "history", str(option))

	def get_history(self) -> bool:
		return Log.history_option

	def warning(self, name:str, message:str) -> None:
		print(style.warning(f"{name}: {message}"))

	def error(self, name:str, message:str) -> None:
		print(style.error(f"{name} : {message}"))

	def debug(self, name:str, message:str="", date_time:bool=False) -> None:
		if Log.debugging_option == True:
			date_time = f"{style.yellow(Log.date_time)} " if date_time == True else ""
			message = f" : {style.green(message)}" if message != "" else ""
			print(f"{date_time}{name}{message}")

	def log(self, name:str, message:str="", date_time:bool=True) -> None:
		if Log.logging_option == True:
			date_time = f"{Log.date_time} " if date_time == True else ""
			message = f" : {message}" if message != "" else ""
			print(style.information(f"{date_time}{name}{message}"))

	def history(self, name:str, message:str="", date_time:bool=True) -> None:
		if Log.history_option == True:
			date_time = f"{Log.date_time} " if date_time == True else ""
			message = f" : {message}" if message != "" else ""
			History.add(f"{date_time}{name}{message}")