# file: bmo/config.py

from configparser import ConfigParser

from directory import Directory

class Config:

	config = ConfigParser()
	config_path = Directory().get_directory("config")

	def __init__(self):
		pass

	def load(self):
		Config.config.read(Config.config_path)

	def save(self):
		with open(Config.config_path, 'w') as config:
			Config.config.write(config)