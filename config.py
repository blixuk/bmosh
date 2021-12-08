# file: bmo/config.py

import os
from configparser import RawConfigParser

from directory import Directory

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

	def make_config(self):

		Config.config["prompt"] = {
			"time_date_format" : "[%d/%m/%Y %H:%M:%S]",
			"carrot" : ">",
			"count" : False,
			"count_format" : "[@]",
		}

		self.save()