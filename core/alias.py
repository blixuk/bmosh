# file: bmo/alias.py

import os
from configparser import RawConfigParser

import lib.style as style
from core.directory import Directory
from core.logging import Log

class Alias:

	parser = RawConfigParser()
	alias_path = Directory().get_directory("alias")

	def __init__(self):
		pass

	def load(self):
		if not os.path.isfile(Alias.alias_path):
			self.make_aliases()

		Alias.parser.read(Alias.alias_path)

	def save(self):
		with open(Alias.alias_path, 'w') as alias:
			Alias.parser.write(alias)

	def list(self) -> list:
		return Alias.parser.options("aliases")
	
	def list_full(self) -> list:
		return Alias.parser.items("aliases")

	def make_aliases(self):

		Alias.parser["aliases"] = {
			"c" : "clear",
			"al" : "alias list",
			"aa" : "alias add",
			"ar" : "alias remove",
			"dc" : "directory change",
			"dl" : "directory list",
			"ds" : "directory stack",
			"dt" : "directory root",
			"dp" : "directory push",
			"dd" : "directory pop",
			"dx" : "directory drop",
			"da" : "directory add",
			"dr" : "directory remove",
			"pe" : "py exec",
			"ph" : "py help",
		}

		self.save()

	def add(self, alias:str, value:list):
		if value == []:
			Log().error("alias", f"no value added '{alias}'")
		if alias not in Alias.parser.options("aliases"):
			value = " ".join(value)
			Alias.parser.set("aliases", alias, value)
			self.save()
		else:
			Log().error("alias", f"'{alias}' already exists")

	def remove(self, alias:str):
		if alias in Alias.parser.options("aliases"):
			Alias.parser.remove_option("aliases", alias)
			self.save()
		else:
			Log().error("alias", f"'{alias}' does not exist")

	def exists(self, alias:str) -> bool:
		return alias in Alias.parser.options("aliases")

	def get_alias(self, alias:str) -> list:
		if alias in Alias.parser.options("aliases"):
			return Alias.parser.get("aliases", alias)
		else:
			return None