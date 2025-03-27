# pylint: disable=E1101
# E1101 is the error code for "not a known attribute of 'None'" in Pylint.
"""
.. py:currentmodule:: py_main.py

Runs a shell command.
"""
from inspect import currentframe

import argparse
# import errno
import sys

from chap01 import class_chap01
from chap02 import class_chap02


def main() -> int:
	"""
	Entry point for script.

	:rtype: int
	:returns: The resulting value from executing the desired command.
	"""

	try:
		# fcn_name:str = currentframe().f_code.co_name
		# print( f"ENTRYPOINT: Module: '{__name__}'; function: '{fcn_name}'" )

		parse_the_args()

		# # Example to retrieve all modules-by-name
		# global_variables = globals()
		# # Filter out modules that start with '__' and are instances of types like 'sys' (modules)
		# modules = {name: obj for name, obj in global_variables.items() if isinstance(obj, type(sys)) and not name.startswith('__')}
		# # List of module names
		# module_names = list(modules.keys())
		# print( f"module_names: {module_names}" )

		# Retrieve the command-line subcommand as this is the "operation" to perform.
		# This is the implementation of the source-code's design.
		class_name:str = chapter_subcmd
		# print( f"class_name: {class_name}" )
		# Convert the camel-case classname to all lowercase.
		cllow:str = class_name.lower()

		# Generate the module name as below; again, this is per project architecture
		# module-by-subdir and source-code fnames.
		module_name:str = f"class_{cllow}"
		# print( f"module_name: {module_name}" )

		try:
			# Retrieve the module's reference per its name:str
			module_ref = globals()[module_name]
			# print( f"module_ref: '{module_ref}' -> TYPE: '{type(module_ref)}'" )
			# Retrieve the class reference from the module
			class_ref = getattr( module_ref, class_name )
			# print( f"class_ref: '{class_ref}' -> TYPE: '{type(class_ref)}'" )
			# Setup the __init__ parameters
			params = [path_config_file]
			# Instantiate the class and run it
			class_ref( *params ).run_in_subdir()
			# Note per line above: the code in the run() class-method could be moved
			# to the end of the class __init__() method there eliminating the need
			# for the run() method.  Then, the call would simply be as below:
			# class_ref( *params )
		except AttributeError as e:
			print( f"Exception caught in main: {e} for getattr( {class_ref} )" )

	except FileExistsError as e:
		print( f"Exception caught in main: {e}" )

	return 0


def parse_the_args():
	"""
	Handle all switches on the command line.  All info required by this script
	loaded into global 'config_params' object.

	Input and output dirs are checked for existence.  The output PATH is
	built to ensure that the filename's extension is .csv.
	"""
	desc="""microelx.py [ Chap01 | Chap02 | Chap02 | Chap05 ]  PATH-to-config.ini
	Example runtime commands:
	(.venvPy3-12-0) .\\run> python run.py Chap01  ..\\config\\chap01\\example\\config_example__01-10.ini
	(.venvPy3-12-0) .\\run> python run.py Chap02  ..\\config\\chap02\\problem\\config_problem__21-30.ini
	"""

	parser = argparse.ArgumentParser( prog=desc )
	# Below, dest='command' captures the sub-command supplied on cmd-line to
	# then determine which sub-command class to instantiate.
	# For example, if sub-command == SEARCH, then cl=task_seach.class_search.Search(...).
	subparsers = parser.add_subparsers( dest='command', required=False, help='Specify chapter' )
	parser_chap01 = subparsers.add_parser( 'Chap01', help='run Chapter 01 problems' )
	parser_chap01.add_argument( 'config_file', help='PATH to config.ini' )
	parser_chap02 = subparsers.add_parser( 'Chap02', help='run Chapter 02 problems' )
	parser_chap02.add_argument( 'config_file', help='PATH to config.ini' )
	# parser_chap77 = subparsers.add_parser( 'Chap77', help='run Chapter XX problems' )
	# parser_chap77.add_argument( 'config_file', help='PATH to config.ini' )
	# The REST
	parser.add_argument( "-p", "--pr", help="OPTION: print config.ini contents" )
	# let each "task" have its own version number
	parser.add_argument( "-v", "--version", help="print TASKS version and exit", action='store_true' )
	# No switches, not even -h
	if len( sys.argv ) == 1:
		parser.print_help( sys.stderr )
		sys.exit(1)
	global args
	args = parser.parse_args()
	# print( f"args cmd line: {args}" )
	# print( f"args sub-cmd: {args.command}" )
	# print( f"SEARCH cmd line: " )
	# Tend the optional switches
	if( args.pr ):
		# pcf = ParseConfigFile( args.pr )
		# pcf.print_all_config_parameters()
		sys.exit(1)
	if (args.version):
		print( f"Chap01 v0.1.0" )
		print( f"Chap02 v0.1.0" )
		sys.exit(1)
	global chapter_subcmd
	chapter_subcmd = args.command
	global path_config_file
	path_config_file = args.config_file


# This is useful when the "file" is to be run directly by python (and not imported)
if __name__ == "__main__":
	# print( 'Call ', __name__ )
	main()
else:
	print( "Do not run from import" )
