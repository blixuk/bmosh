# file: bmo/__main__.py

from args import Args
args = Args(description="BMO")
from shell import Shell
shell = Shell()

class BMO:

	def __init__(self):
		pass

	@args.subcommand()
	def run(self, args):
		shell.loop()

	@args.subcommand()
	def help(self, args):
		args.print_help()

if __name__ == '__main__':
	args.parse()