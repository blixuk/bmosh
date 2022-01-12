# file: bmo/__main__.py

from args import Args
args = Args(description="BMO")
from core.config import Config
Config().load()
from shell import Shell

class BMO:

	@args.subcommand()
	def run(self, args):
		shell = Shell()
		shell.loop()

	@args.subcommand()
	def help(self, args):
		args.print_help()

if __name__ == '__main__':
	args.parse()