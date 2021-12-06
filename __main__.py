# file: bmo/__main__.py

from command import Command
cmd = Command(description="BMO")
from shell import Shell
shell = Shell()

class BMO:

	def __init__(self):
		pass

	@cmd.subcommand()
	def run(self, args):
		shell.loop()

	@cmd.subcommand()
	def help(self, args):
		cmd.print_help()

if __name__ == '__main__':
	cmd.parse()