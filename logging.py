# file: bmo/logging.py

from datetime import datetime

import style

class Log:

	debugging:bool = True
	logging:bool = True
	date_time:datetime = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")

	def __init__(self) -> None:
		pass

	def set_debug(self, option:bool) -> None:
		Log.debugging = option

	def get_debug(self) -> bool:
		return Log.debugging

	def set_logging(self, option:bool) -> None:
		Log.logging = option

	def get_logging(self) -> bool:
		return Log.logging

	def warning(self, name:str, message:str) -> None:
		print(style.warning(f"{name}: {message}"))

	def error(self, name:str, message:str) -> None:
		print(style.error(f"{name} : {message}"))

	def debug(self, name:str, message:str, date_time:bool=False) -> None:
		if Log.debugging == True:
			if date_time == True:
				print(f"{style.yellow(Log.date_time)} {style.red(name)} : {style.green(message)}")
			else:
				print(f"{style.red(name)} : {style.green(message)}")
	
	def log(self, name:str, message:str, date_time:bool=True) -> None:
		if Log.logging == True:
			if date_time == True:
				print(style.information(f"{Log.date_time} {name} : {message}"))
			else:
				print(style.information(f"{name} : {message}"))