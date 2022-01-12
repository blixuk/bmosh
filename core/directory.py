# file: bmo/directory.py 

import os
from pathlib import Path

class Directory:

	directories = {
		'..' : Path('..'),
		'...' : Path('../..'),
		'.3' : Path('../../..'),
		'.4' : Path('../../../..'),
		'.5' : Path('../../../../..'),
		'.6' : Path('../../../../../..'),
		'~' : Path('~').expanduser(),
		'home' : Path('~').expanduser(),
		'downloads' : Path('~/Downloads').expanduser(),
		'documents' : Path('~/Documents').expanduser(),
		'pictures' : Path('~/Pictures').expanduser(),
		'desktop' : Path('~/Desktop').expanduser(),
		'videos' : Path('~/Videos').expanduser(),
		'music' : Path('~/Music').expanduser(),
		'bmo' : Path('~/.config/bmo').expanduser(),
		'sessions' : Path('~/.config/bmo/sessions').expanduser(),
		'alias' : Path('~/.config/bmo/alias.bmo').expanduser(),
		'history' : Path('~/.config/bmo/history.bmo').expanduser(),
		'config' : Path('~/.config/bmo/config.bmo').expanduser(),
	}
	stack = [Path("/")]
	path = Path("/")

	def __init__(self) -> None:
		pass

	def set_path(self, path:str) -> None:
		Directory.path = Path(path)
		#logging.Log().error('directory', f"unable to set path '{path}'")

	def get_path(self) -> str:
		return str(Directory.path)

	def get_directory(self, name:str) -> str:
		if name in Directory.directories:
			return str(Directory.directories[name])
		return None

	def change(self, path:str='home') -> None:
		if path in Directory.directories:
			os.chdir(Directory.directories[path])
		os.chdir(Path(path).expanduser())
		#logging.Log().error('directory', f"unable to change path '{path}'")
		self.set_path(os.getcwd())

	def set_root(self, path: str) -> None:
		Directory.stack[0] = Path(path)
		#change(path) # should we change to root path when set?
		#logging.Log().error('directory', f"unable to set root path '{path}'")

	def get_stack(self) -> list:
		return Directory.stack

	def push(self, path:str=None):
		if path == None:
			Directory.stack.append(Directory.path)
		elif path in Directory.directories:
			Directory.stack.append(Directory.directories[path])
			self.change_directory(path)
		else:
			Directory.stack.append(Path(path).expanduser())
			self.change_directory(path)
		#logging.Log().error('directory', f"unable to push stack: '{path}'")

	def pop(self) -> None:
		if len(Directory.stack) > 1:
			del Directory.stack[-1]
			self.change_directory(Directory.stack[-1])
		#logging.Log().error('directory', f"unable to pop stack")

	def drop(self, index:int) -> None:
		if int(index) != 0 and len(Directory.stack) > 1:
			del Directory.stack[int(index)]
		#logging.Log().error('directory', f"Unable to drop stack: '{index}'")

	def jump(self, index:int) -> None:
		if int(index) <= (len(Directory.stack) - 1):
			self.change_directory(Directory.stack[int(index)])
		#logging.Log().error('directory', f"unable to jump stack: '{index}'")

	def get_directories(self) -> dict:
		return Directory.directories.items()

	def add(self, name:str, path:str=None) -> None:
		if name not in self.directories and path == None:
			self.directories[name] = self.path
		elif name not in self.directories:
			self.directories[name] = Path(path).expanduser()
		#logging.Log().error('directory', f"Unable to add path '{name}'")

	def remove(self, name:str) -> None:
		if name in Directory.directories:
			del Directory.directories[name]
		#logging.Log().error('directory', f"Unable to remove path '{name}'")
