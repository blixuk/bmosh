# file: bmo/config.py

import os
from configparser import RawConfigParser

import lib.style as style
from core.directory import Directory

class Config:

	config = RawConfigParser()
	config_path = Directory().get_directory("config")

	def __init__(self):
		pass

	def load(self):
		if not os.path.isfile(Config.config_path):
			self.make_config()

		Config.config.read(Config.config_path)

	def save(self):
		with open(Config.config_path, 'w') as config:
			Config.config.write(config)

	def list(self) -> list:
		sections:list = []
		for section in Config.config.sections():
			sections.append(f"{style.blue(section)}:")
			for option in Config.config.options(section):
				sections.append(f"{style.green(option)}")
		return sections

	def list_full(self) -> list:
		sections:list = []
		for section in Config.config.sections():
			sections.append(f"{style.blue(section)}:")
			for option, value in Config.config.items(section):
				sections.append(f"{style.green(option)} -> {style.yellow(value)}")
		return sections

	def make_config(self):

		Config.config["prompt"] = {
			"date_time_format" : "[%d/%m/%Y %H:%M:%S]",
			"date_time" : True,
			"carrot" : ">",
			"count_format" : "[@]",
			"count" : False,
		}

		Config.config["logging"] = {
			"time_date_format" : "[%d/%m/%Y %H:%M:%S]",
			"log" : True,
			"debug" : False,
			"history" : True,
		}

		self.save()