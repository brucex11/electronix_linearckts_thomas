import ast
from inspect import currentframe
import math
import numpy as np
from typing import List, Tuple  # Any, Dict, Set

import matplotlib.pyplot as plt


def exer2_04(self):
	"""Page 228
	Linear Systems and Signals, Lathi
	Prob 2.4-27 (a) Find and sketch c(t) = x1(t) * x2(t) for the pairs of functions
	illustrated in Fig. P2.4-27.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )


	#  α   β   Ω   μ   λ   γ   ξ   ω

	# ---- Answers -------------------
	ans:float = 0

	# ---- Givens --------------------

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Calcs ---------------------
	calc_result:float = 0


	# ---- chatgpt -------------------
	# Define time vector (from -10 to 10 seconds for a wide enough range)
	t_sig = np.linspace(-8, 8, 1000)

	# Define x1(t): value 1 between 4 and 6 seconds, zero elsewhere
	pulse1 = np.zeros_like(t_sig)
	pulse1[(t_sig >= 4) & (t_sig <= 6)] = 1

	# Define x2(t): value 2 between -5 and -4 seconds, zero elsewhere
	pulse2 = np.zeros_like(t_sig)
	pulse2[(t_sig >= -5) & (t_sig <= -4)] = 2

	# Compute the convolution of the two pulses
	conv_mode:str = 'full'
	conv_result = np.convolve(pulse1, pulse2, mode=conv_mode) * (t_sig[1] - t_sig[0])  # Multiply by delta t for correct scaling
	if( conv_mode == 'same' ):
		t_con:np.ndarray = t_sig
	elif( conv_mode == 'full' ):
		t_con = np.linspace(-8, 8, len(conv_result))

	# Plot the pulses and their convolution
	plt.figure(figsize=(10, 6))

	# Plot x1(t)
	plt.subplot(3, 1, 1)
	plt.plot(t_sig, pulse1, label='x1(t)', color='blue')
	plt.title('x1(t)')
	plt.xlabel('Time (seconds)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot x2(t)
	plt.subplot(3, 1, 2)
	plt.plot(t_sig, pulse2, label='x2(t)', color='r')
	plt.title('x2(t)')
	plt.xlabel('Time (seconds)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot the Convolution of x1(t) and x2(t)
	plt.subplot(3, 1, 3)
	# t = np.linspace(-8, 8, 1999)
	plt.plot(t_con, conv_result, label='Convolution', color='purple')
	plt.title( f"{conv_mode}: Convolution of x1(t) and x2(t)" )
	plt.xlabel('Time (seconds)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	plt.tight_layout()
	plt.show()
	plt.close()

	return






	# ---- Givens --------------------
	# max_for_time_range:int = 1601
	# x_time:List[float] = [round(0 + i * 0.01, 3) for i in range(max_for_time_range)]  # from 0.0 to 7.0
	# print( f"len(x_time): {len(x_time)}" )

	x_time = np.linspace(-8, 8, 1601)  # x-values from -8 to 8

	x1_t_a:List[float] = [0.0] * 1200
	x1_t_b:List[float] = [1.0] * 200
	x1_t_c:List[float] = [0.0] * 201
	x1_t:List[float] = x1_t_a + x1_t_b  + x1_t_c
	print( f"len(x1_t): {len(x1_t)}" )

	x2_t_a:List[float] = [0.0] * 300
	x2_t_b:List[float] = [2.0] * 100
	x2_t_c:List[float] = [0.0] * 1201
	x2_t:List[float] = x2_t_a + x2_t_b  + x2_t_c

	# plot_x1_x2( self, x_time, x1_t, x2_t )

	# conv = np.convolve( x1_t, x2_t )
	conv_mode:str = 'full'
	conv = np.convolve( x1_t, x2_t, mode=conv_mode ) * (x_time[1] - x_time[0])  # Multiply by delta t for correct scaling
	print( f"type(conv): {type(conv)}" )
	print( f"len(conv): {len(conv)}" )

	xc_time = np.linspace( -16, 16, len(conv) )
	plot_conv( self, xc_time, conv, mode=conv_mode )


	ans_string:str = """
CONVOLUTION
"""
	print( ans_string )

	print( '\n---- (a) -------------------------------------------' )


def plot_conv( self, xc_time, conv, mode:str ):
	"""
	"""
	plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )
	plt.plot( xc_time, conv, color='purple', label=f"mode={mode}" )  # customize color, recall 'k' = black

	plt.xlim( -6,6 )
	plt.ylim( 0, 2.2 )

	plt.title( "title" )
	plt.grid(True)
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()


def plot_x1_x2( self, x_time, x1_t, x2_t ):
	"""
	"""
	plt.figure( figsize=ast.literal_eval(self.cf.get_config_params['common']['param_figure_figsize']) )
	plt.plot( x_time, x1_t, color='k', label=f"A=1" )  # customize color, recall 'k' = black
	plt.plot( x_time, x2_t, color='r', label=f"B=2" )  # customize color, recall 'k' = black

	plt.xlim( -8,8 )
	plt.ylim( 0, 2.2 )

	plt.legend()  # adds a legend to label the highlighted point
	plt.show()

