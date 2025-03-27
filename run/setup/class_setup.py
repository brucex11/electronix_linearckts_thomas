import ast
# from collections import OrderedDict
# from datetime import datetime
import configparser
import errno
from inspect import currentframe
import logging
import os
import pathlib
from typing import Any, Dict   # also available: List, Set, Tuple


class Setup():
	"""
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
		print( f"Setup:ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# base-class attributes
		self._dict_config_params:Dict[str,Any] = {}

		if not os.path.isfile( path_config_file ):
			raise FileExistsError( errno.ENOENT, os.strerror(errno.ENOENT), path_config_file )
		# print( f"PATH to config file: '{path_config_file}'" )
		# self._lg = logger_obj

		configParser = configparser.ConfigParser( allow_no_value=True )
		configParser.read( path_config_file )
		for section in configParser.sections():
			self._dict_config_params[section] = {}
			for option in configParser.options( section ):
				self._dict_config_params[section][option] = configParser.get( section, option )

		if( ast.literal_eval( self.get_config_param['common']['print_config_params'] ) ):
			self.print_all_config_parameters()

		# Pick-up the common config params
		# subdir_name is used to build the "path" to dynamically call the problem function
		self._chapter_title = self.get_config_param['common']['chapter_title']
		chlow:str = self.chapter_title.lower()
		self._subdir_name = self.get_config_param['common']['subdir_name']
		self.prob:str = self.get_config_param['common']['problem_num']
		# Strip the leading 'p' and replace '_' with '.' for printing purpose only.
		# tmps:str = self.prob.lstrip(self.prob[0])
		self._prob_str:str = self.prob.replace( '_', '.' )
		self._problem_txt = self.get_config_param['common']['problem_txt']
		self._problem_ans = self.get_config_param['common']['problem_ans']

		# Create the logger object
		if( ast.literal_eval( self.get_config_param['common']['enable_logging'] ) ):
			ftmp1:str = self.get_config_param['common']['logger_folder_template']
			ftmp2:str = ftmp1.replace( 'CHPTR', chlow )
			logger_folder:str = ftmp2.replace( 'PRBLM', self.subdir_name )
			print( f"logger-folder: '{logger_folder}'")
			# logger_folder:str = ftmp3.replace( 'QNUM', self.prob )
			pathlib.Path( logger_folder ).mkdir( parents=True, exist_ok=True )

			lfname:str = f"{self.prob}.log2"
			path_to_log_file:str = os.path.join( logger_folder, lfname )
			print( f"path_to_log_file: '{str(path_to_log_file).replace("\\", "/")}'" )

			logging.basicConfig(
				filename=path_to_log_file,  # Log file name
				filemode='a',  # Write mode ('w' for overwrite, 'a' for append)
				level=logging.DEBUG,  # Set the minimum level of messages to capture
				format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
			)
			lg = logging.getLogger( self.prob )
			# print( f"type(lg): {type(lg)}" )
			lg.info( f"---- START {self.get_config_param['common']['problem_num']} ----" )
			lg.info( f"PATH to this log file: '{str(path_to_log_file).replace("\\", "/")}'" )


		# # save figure params
		# self._save_figure = ast.literal_eval(
		# 	self.cf.get_config_param['common']['save_figure'] )
		# self._save_figure_folder:str = os.path.join(
		# 	self.cf.get_config_param['common']['save_figure_rootdir'],
		# 	self.cf.get_config_param['common']['save_figure_subdir'],
		# 	self.cf.get_config_param['common']['project_title']
		# )


		# Class-level attributes

		# Initialize constants for all problems

		# rsp = input( 'yes if ok, else press <Enter>' )
		# if rsp != 'yes':
		# 	print( 'QUIT' )
		# 	exit()


	# ----------------------------------------------------------------------------
	# --- Getters ----------------------------------------------------------------
	# ----------------------------------------------------------------------------
	@property
	def get_config_param(self):
		return self._dict_config_params

	@property
	def chapter_title(self):
		return self._chapter_title
	@property
	def problem_ans(self):
		return self._problem_ans
	@property
	def problem_txt(self):
		return self._problem_txt
	@property
	def prob_str(self):
		return self._prob_str
	@property
	def save_figure(self):
		return self._save_figure
	@property
	def save_figure_folder(self):
		return self._save_figure_folder
	@property
	def subdir_name(self):
		return self._subdir_name


	# ---------------------------------------------------------------------------
	# --- Functions -------------------------------------------------------------
	# ---------------------------------------------------------------------------
	def print_all_config_parameters( self ):
		"""
		Print the config params if the ['common']['print_config_params']
		is set to True.
		"""
		# print( f"params: '{self.get_config_param}'" )
		for section, its in self._dict_config_params.items():
			print( f"<><> section: '{section}' (key-pairs below)" )
			for key, val in its.items():
				print( f"     {key} : {val}")


	# ----------------------------------------------------------------------------
	# --- Functions: helpers to support all of Chapter 02 ------------------------
	# ----------------------------------------------------------------------------
