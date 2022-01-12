# file: bmo/session.py

import shelve
import os

import lib.style as style
from core.logging import Log
from core.directory import Directory

class Session:

	session = {}
	session_path = Directory().get_directory("sessions")

	def __init__(self) -> None:
		pass

	def load(self, name:str=None) -> None:
		if not os.path.exists(Session.session_path):
			os.makedirs(Session.session_path)

		Session.session = {}
		if name is None:
			name = "main"

		with shelve.open(f"{Session.session_path}/{name}.session") as db:
			if "session" not in db:
				Session.session["session"] = name
			for key in db:
				try:
					if not key.startswith("__") or not key.endswith("__"):
						Session.session[key] = db[key]
				except TypeError:
					Log().error(f"session', 'TypeError loading '{key}'")   

	def save(self, name:str=None) -> None:
		if not os.path.exists(Session.session_path):
			os.makedirs(Session.session_path)

		if name is None and Session.session["session"]:
			name = Session.session["session"]
		elif name is None and not Session.session["session"]:
			name = "main"

		with shelve.open(f"{Session.session_path}/{name}.session", 'n') as db:
			for key in Session.session:
				try:
					if not key.startswith("__") or not key.endswith("__"):
						db[key] = Session.session[key]
				except TypeError:
					Log().error(f"session', 'TypeError saving '{key}'")
			db["session"] = name

	def get(self) -> list:
		session:list = []
		for count, (key, value) in enumerate(Session.session.items()):
			if not key.startswith("__") or not key.endswith("__"):
				session.append(f"{key}:{value}")
		return session

	def list(self) -> list:
		session:list = []
		for key, value in Session.session.items():
			if not key.startswith("__") or not key.endswith("__"):
				session.append(f"{style.green(str(key))} -> {style.yellow(str(value))}")
		return session

	def list_full(self) -> list:
		session:list = []
		for key, value in Session.session.items():
			if not key.startswith("__") or not key.endswith("__"):
				session.append(f"{style.green(str(key))} -> {style.yellow(str(value))}:{style.red(str(value.__class__.__name__))}")
		return session