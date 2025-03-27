# from datetime import datetime
import importlib
from inspect import currentframe

from setup import class_setup


class Chap01( class_setup.Setup ):
	"""
	HW problems:  1.1-1 ; -4 ; -11
                1.2-1
                1.4-4 ; -6c,d,e,f ; -13
	"""

	def __init__( self, path_config_file:str ) -> None:
		"""
		Call the base-class to parse the config.ini file.
		Prep the log file's PATH.
		Prep the generated output file's PATH.

		Args:
			path_to_config_file : string
				this is passed to the base class for parsing
		"""
		fcn_name:str = currentframe().f_code.co_name
		print( f"Chap02:ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		super().__init__(path_config_file)


	# ----------------------------------------------------------------------------
	# --- Functions: helpers to support all of Chapter 01 ------------------------
	# ----------------------------------------------------------------------------


	# ----------------------------------------------------------------------------
	# --- Dynamic method caller --------------------------------------------------
	# ----------------------------------------------------------------------------
	def run_in_dir(self):
		"""Call the method per the config.ini file [problem_num] WHEN THE MODULE
			 (OR .PY FILENAME) IS IN THE SAME SUBDIR AS THIS MODULE/.PY FILE.
		"""
		fcn_name:str = currentframe().f_code.co_name
		print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# build the module name starting with this class's name
		class_name:str = self.__class__.__name__
		# convert the camel-case classname to all lowercase
		cllow:str = class_name.lower()
		module_name:str = f"{cllow}.{self.prob}"
		method_name:str = f"{self.prob}"
		module = importlib.import_module( module_name )
		method = getattr( module, method_name )
		if callable(method):
			method(self)
		else:
			raise AttributeError( f"Method '{self.prob}' not found" )


	def run_in_subdir(self):
		"""Call the method per the config.ini file [problem_num]
		"""
		fcn_name:str = currentframe().f_code.co_name
		print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# # Example to retrieve all modules
		# global_variables = globals()
		# # Filter out modules that start with '__' and are instances of types like 'sys' (modules)
		# modules = {name: obj for name, obj in global_variables.items() if isinstance(obj, type(sys)) and not name.startswith('__')}
		# # List of module names
		# module_names = list(modules.keys())
		# print( f">>>>>>>>>>>>>>>>>>>module_names: {module_names}" )

		# Build the FULL module name in req'd format: class-name.subdir-name.python-fname
		#   where:
		#      class-name:   contains all lower-case chars,
		#      subdir-name:  is picked up from the config.ini file,
		#      python-fname: is aka a python "module" without the .py extension,
		#                    and is also picked up from the config.ini file.
		# this class's name
		class_tmp:str = self.__class__.__name__
		# print( f"class_name: {class_tmp}" )
		# convert the camel-case classname to all lowercase
		class_name:str = class_tmp.lower()
		subdir_name:str = self.subdir_name
		py_fname_sans_extension:str = self.prob
		# build the FULL module name
		module_name:str = f"{class_name}.{subdir_name}.{py_fname_sans_extension}"
		# use the module-name string to import the desired module
		module = importlib.import_module( module_name )
		# finally, grab the function-name in the module
		# print( f"*** module: '{module_name}'  *** py_fname_sans_extension: '{py_fname_sans_extension}" )
		method = getattr( module, py_fname_sans_extension )
		if callable(method):
			method(self)
		else:
			raise AttributeError( f"Method '{self.prob}' not found" )
