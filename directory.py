# file: bmo/directory.py 

import os
from pathlib import Path

import style
from logging import Log

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
		'aliases' : Path('~/.config/bmo/aliases.bmo').expanduser(),
		'history' : Path('~/.config/bmo/history.bmo').expanduser(),
		'config' : Path('~/.config/bmo/config.bmo').expanduser(),
	}
	stack = [Path("/")]
	path = Path("/")

	def __init__(self) -> None:
		pass

	def set_path(self, path:str) -> None:
		if Path(path).is_dir():
			Directory.path = Path(path)
		else:
			Log().error('directory', f"unable to set path '{path}'")

	def get_path(self) -> str:
		return str(Directory.path)

	def get_directory(self, name:str) -> str:
		if name in Directory.directories:
			return Directory.directories[name]
		else:
			return None

	def change_directory(self, path:str) -> None:
		if path in Directory.directories:
			os.chdir(Directory.directories[path])
		elif Path(path).expanduser().is_dir():
			os.chdir(Path(path).expanduser())
		else:
			Log().error('directory', f"unable to change path '{path}'")

		self.set_path(os.getcwd())

	def set_stack_root(self, path: str) -> None:
		if Path(path).is_dir():
			Directory.stack[0] = Path(path)
			#change(path) # should we change to root path when set?
		else:
			Log().error('directory', f"unable to set root path '{path}'")

	def get_stack_list(self) -> list:
		stack_list = []
		for count, path in enumerate(Directory.stack):
			stack_list.append(f"[{style.yellow(str(count))}] {style.green(str(path))}")
		return stack_list

	def push_directory(self, path:str=None):
		if path == None:
			Directory.stack.append(Directory.path)
		elif path in Directory.directories:
			Directory.stack.append(Directory.directories[path])
			self.change_directory(path)
		elif Path(path).expanduser().is_dir():
			Directory.stack.append(Path(path).expanduser())
			self.change_directory(path)
		else:
			Log().error('directory', f"unable to push stack: '{path}'")

	def pop_directory(self) -> None:
		if len(Directory.stack) > 1:
			del Directory.stack[-1]
			self.change_directory(Directory.stack[-1])
		else:
			Log().error('directory', f"unable to pop stack")

	def drop_directory(self, index:int) -> None:
		if int(index) != 0 and len(Directory.stack) > 1:
			del Directory.stack[int(index)]
		else:
			Log().error('directory', f"Unable to drop stack: '{index}'")

	def jump_directory(self, index:int) -> None:
		if int(index) <= (len(Directory.stack) - 1):
			self.change_directory(Directory.stack[int(index)])
		else:
			Log().error('directory', f"unable to jump stack: '{index}'")

	def get_direcotries_list(self) -> list:
		directories_list = []
		for key, path in Directory.directories.items():
			directories_list.append(f'[{style.yellow(str(key))}] {style.green(str(path))}')
		return directories_list

	def add_directory(self, name:str, path:str=None) -> None:
		if name not in self.directories and path == None:
			self.directories[name] = self.path
		elif name not in self.directories:
			self.directories[name] = Path(path).expanduser()
		else:
			Log().error('directory', f"Unable to add path '{name}'")

	def remove_directory(self, name:str) -> None:
		if name in Directory.directories:
			del Directory.directories[name]
		else:
			Log().error('directory', f"Unable to remove path '{name}'")
	