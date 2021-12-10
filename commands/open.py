# file: bmo/commands/open.py

from re import sub
import subprocess

class Comamnd:
	'''
	open
	'''

	def default(self, args:list) -> None:
		subprocess.Popen('xdg-open', args[0])
		return None

def run() -> str:
	return Comamnd()