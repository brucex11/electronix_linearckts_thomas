from inspect import currentframe
import numpy as np

import matplotlib.pyplot as plt


def exam3_03(self):
	"""Page 84:
	Use the unit step function to describe the signal in Fig. 1.16a."
	ANS: x(t) = tu(t) - 3(t-2)u(t-2) + 2(t-3)u(t-3).
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: '{pnum}'" )
	print( f"{self.problem_txt}" )
	# print( f"{self.problem_ans}" )
	print( '-----------------------------------------------\nSolution' )
	return

	#  α   β   Ω   μ   λ   γ   ξ   ω

	# ---- Answers -------------------
	ans:float = 0

	# ---- Givens --------------------

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Calcs ---------------------
	calc_result:float = 0


	# Define time vector:
	x_time_start:float = 0  # 'actual' second in time to start the time-span
	x_time_sec:float = 4    # total num 'actual' seconds to time-span
	x_time_tics:int = 1000  # num array elements in time-span
	x_time_delta_tau:float = 1/x_time_tics
	print( f"delta-tau = time-span step-size = {x_time_delta_tau}" )
	t_sig = np.linspace( x_time_start, x_time_sec, x_time_tics )
	print( f"len(t_sig) = {len(t_sig)}" )

	# Define x1(t): 
	# 'actual' time in seconds:
	#   * positive is delay (earlier in time)
	#   * negative is advance (later in time)
	#   * MUST fall within time-span
	# slope = rise / run = (upper_bound-lower_bound) / x_time_sec
	# positive slope:  upper_bound > lower_bound
	# negative slope:  upper_bound < lower_bound
	upper_bound:float = 4   # high amplitude of ramp
	lower_bound:float = 0   #  low amplitude of ramp
	rise:float = upper_bound - lower_bound   # total "height" of ramp
	delta_rise:float = rise * x_time_delta_tau

	# Slope ramp:  rise / run
	slope:float = ( upper_bound - lower_bound ) / x_time_sec
	print( f"slope ramp x1(t) = ( upper_bound - lower_bound ) / x_time_sec" )
	print( f"                 = ( {upper_bound} - {lower_bound} ) / {x_time_sec}" )
	print( f"                 = {slope}" )

	ramp_full = np.arange( start=lower_bound, stop=upper_bound, step=delta_rise )
	# print( f"len(ramp_full) = {len(ramp_full)}" )

	# Apply the unit step.
	u_t_0_2 = np.heaviside(t_sig, 0) - np.heaviside(t_sig - 2, 0)
	x1_t = ramp_full * u_t_0_2


	# Define x2(t):
	upper_bound:float = -2  # high amplitude of ramp
	lower_bound:float = 6   #  low amplitude of ramp
	rise:float = upper_bound - lower_bound   # total "height" of ramp
	delta_rise:float = rise * x_time_delta_tau

	# Slope ramp:  rise / run
	slope:float = ( upper_bound - lower_bound ) / x_time_sec
	print( f"slope ramp x2(t) = ( upper_bound - lower_bound ) / x_time_sec" )
	print( f"                 = ( {upper_bound} - {lower_bound} ) / {x_time_sec}" )
	print( f"                 = {slope}" )

	ramp_full = np.arange( start=lower_bound, stop=upper_bound, step=delta_rise )
	# print( f"len(ramp_full) = {len(ramp_full)}" )

	# Apply the unit step.
	u_t_0_2 = np.heaviside(t_sig-2, 0) - np.heaviside(t_sig-3, 0)
	x2_t = ramp_full * u_t_0_2

	# Compute the signal
	signal:np.ndarray = x1_t + x2_t

	# Plot the ramps and their sum
	plt.figure(figsize=(10, 6))

	# Plot x1(t)
	plt.subplot(3, 1, 1)
	plt.plot(t_sig, x1_t, label='x1(t)', color='blue')
	plt.title( f"x1(t) = ramp" )
	plt.xlabel('time(s)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot x2(t)
	plt.subplot(3, 1, 2)
	plt.plot(t_sig, x2_t, label='x2(t)', color='r')
	plt.title( f"x2(t) = ramp" )
	plt.xlabel('time(s)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot the signal
	plt.subplot(3, 1, 3)
	plt.plot(t_sig, signal, label='', color='purple')
	plt.title( f"Signal x1(t) + x2(t)" )
	plt.xlabel('time(s)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	plt.tight_layout()
	plt.show()
	plt.close()
