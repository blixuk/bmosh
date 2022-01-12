# file: bmo/style.py

import re

def style(text:str, **styles) -> str:
	escape_codes = {
		# styling
		'reset'		:	'\033[0m',
		'bold'		:	'\033[01m',
		'b'			:	'\033[01m',
		'faint'		:	'\033[02m',
		'f'			:	'\033[02m',
		'italic'	:	'\033[03m',
		'i'			:	'\033[03m',
		'underline'	:	'\033[04m',
		'u'			:	'\033[04m',
		'blink'		:	'\033[05m',
		'l'			:	'\033[05m',
		'invert'	:	'\033[07m',
		'r'			:	'\033[07m',
		'strike'	:	'\033[09m',
		's'			:	'\033[09m',
		'invisible'	:	'\033[08m',
		'v'			:	'\033[08m',
		# forground colours
		'fgBlack'	:	'\033[30m',
		'fgRed'		:	'\033[31m',
		'fgGreen'	:	'\033[32m',
		'fgYellow'	:	'\033[33m',
		'fgBlue'	:	'\033[34m',
		'fgMagenta'	:	'\033[35m',
		'fgCyan'	:	'\033[36m',
		'fgWhite'	:	'\033[37m',
		# bright forground colours
		'fgBBlack'	:	'\033[90m',
		'fgBRed'	:	'\033[91m',
		'fgBGreen'	:	'\033[92m',
		'fgBYellow'	:	'\033[93m',
		'fgBBlue'	:	'\033[94m',
		'fgBMagenta':	'\033[95m',
		'fgBCyan'	:	'\033[96m',
		# background colours
		'bgBlack'	:	'\033[40m',
		'bgRed'		:	'\033[41m',
		'bgGreen'	:	'\033[42m',
		'bgYellow'	:	'\033[43m',
		'bgBlue'	:	'\033[44m',
		'bgMagenta'	:	'\033[45m',
		'bgCyan'	:	'\033[46m',
		'bgWhite'	:	'\033[47m',
		# bright background colours
		'bgBBlack'	:	'\033[100m',
		'bgBRed'	:	'\033[101m',
		'bgBGreen'	:	'\033[102m',
		'bgBYellow'	:	'\033[103m',
		'bgBBlue'	:	'\033[104m',
		'bgBMagenta':	'\033[105m',
		'bgBCyan'	:	'\033[106m',
		'bgBWhite'	:	'\033[107m'
	}

	styled_text = ''
	for style in styles:
		if styles[style] == True:
			try:
				styled_text += escape_codes[style]
			except KeyError:
				raise KeyError(f"style '{style}' does not exist")

	styled_text += text
	return f"\033[0m{styled_text}\033[0m"

def clean(text:str) -> any:
	escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
	return escape.sub('', text)

# Information Styles
def information(text:str, blink:bool=False) -> style:
	return style(text, bold=True, fgBlue=True, blink=blink)

def Information(text:str, blink:bool=False) -> style:
	return style(text, bold=False, fgWhite=True, bgBlue=True, blink=blink)

def error(text:str, blink:bool=False) -> style:
	return style(text, bold=True, fgRed=True, blink=blink)

def Error(text:str, blink:bool=False) -> style:
	return style(text, bold=True, fgBlack=True, bgRed=True, blink=blink)

def warning(text:str, blink:bool=False) -> style:
	return style(text, bold=True, fgYellow=True, blink=blink)

def Warning(text:str, blink:bool=False) -> style:
	return style(text, bold=True, fgBlack=True, bgYellow=True, blink=blink)

def success(text:str, blink:bool=False) -> style:
	return style(text, bold=True, fgGreen=True, blink=blink)

def Success(text:str, blink:bool=False) -> style:
	return style(text, bold=True, fgBlack=True, bgGreen=True, blink=blink)

def blink(text:str) -> style:
	return style(text, blink=True)

# Colours
def black(text:str) -> style:
	return style(text, bold=False, fgBlack=True)

def red(text:str) -> style:
	return style(text, bold=False, fgRed=True)

def green(text:str) -> style:
	return style(text, bold=False, fgGreen=True)

def yellow(text:str) -> style:
	return style(text, bold=False, fgYellow=True)

def blue(text:str) -> style:
	return style(text, bold=False, fgBlue=True)
	
def magenta(text:str) -> style:
	return style(text, bold=False, fgMagenta=True)

def white(text:str) -> style:
	return style(text, bold=False, fgWhite=True)

def grey(text:str) -> style:
	return style(text, bold=False, fgBBlack=True)

# progress bar

def progressBar(iterable, prefix='', suffix='', decimals=1, length=100, fill='█', end="\r"):
	total = len(iterable)

	def printProgressBar(iteration):
		percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=end)

	printProgressBar(0)

	for i, item in enumerate(iterable):
		yield item
		printProgressBar(i + 1)

	print()

def progressBarStyled(iterable, prefix='', suffix='', decimals=1, length=100, fill='█', end="\r"):
	total = len(iterable)

	def printProgressBar(iteration):
		percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		print(f'\r{prefix} |{style(bar, fgYellow=True)}| {percent}% {suffix}', end=end)

	printProgressBar(0)

	for i, item in enumerate(iterable):
		yield item
		printProgressBar(i + 1)

	print()

def command(commands:str, description:str="") -> style:
	command = []
	commands = commands.split(" ")
	command.append(style(commands[0], bold=True, fgBlue=True))
	for word in commands[1:]:
		if word.startswith("<") and word.endswith(">"):
			word = word.lstrip("<").rstrip(">")
			word = f"<{style(word, fgYellow=True)}>"
		else:
			word = style(word, bold=True, fgGreen=True)
		command.append(word)
	
	return f"{' '.join(command)} : {description}"

def help(help:dict) -> str:
	command_help = []
	for key, value in help.items():
		if key == "name":
			command_help.append(style(f"{value}:", bold=True, fgWhite=True))
		elif key == "description":
			command_help.append(f"    {value}")
		elif key == "default":
			command_help.append(style("default:", bold=True))
			for name, description in value.items():
				command_help.append(f"    {command(name, description)}")
		elif key == "subcommands":
			command_help.append(style("subcommands:", bold=True))
			for name, description in value.items():
				name = f"{help['name']} {name}"
				command_help.append(f"    {command(name, description)}")
	return "\n".join(command_help)