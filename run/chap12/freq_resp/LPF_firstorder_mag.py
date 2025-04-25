from inspect import currentframe
import math
from typing import List, Any  # Tuple, Dict, Set

import matplotlib.pyplot as plt

# from assertions.assertions import assert_within_percentage
# from equations.equations import to_s_k, to_s_mA, to_s_uA
# from equations.equations import equivalent_parallel_resisitance
# from equations.equations import r1_parallel_r2
# from equations.equations import current_divider


def LPF_firstorder_mag(self):
	"""2nd Ed pg 708:
	Frequency response for most-basic RL and RC LFP circuits.

	./docx/chap12/freq_resp/first-order/LPF/first-order__LPF_RL_RC.docx
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	# assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π  τ

	# ---- Assumptions ---------------
	omega_range:List[float] = [round(0.01 + i * 0.01, 2) for i in range(100000)]  # 100000 values from 0.01 to 1000
	# print( omega_range )

	# tenthX_crossing_point:List[Any] = []  # ratio is 0.1X
	# ω01_dB_crossing_point:List[Any] = []   # ratio is 1X (unity)
	# sqrt2X_crossing_point:List[Any] = []  # ratio is sqrt(2)X
	# twoX_crossing_point:List[Any] = []    # ratio is 2X

	ax1_plot_label_Tjω:str = 'T(ω)=[1 / (1 + ω)]'
	list_Tjω:List[float] = []

	ax1_plot_label_Tdb:str = '|T(ω)|=20log[1/sqr(1 + ω^2)]'
	list_Tdb:List[float] = []
	ωpoint1_dB_crossing_point:List[Any] = []    # ω=.1
	ω01_dB_crossing_point:List[Any] = []   # ω=1
	ω10_dB_crossing_point:List[Any] = []    # ω=10
	ω100_dB_crossing_point:List[Any] = []    # ω=100

	# T_jω:float = 1 / (1 + ω)

	# ---- Calcs ---------------------
	for idx, ω in enumerate(omega_range):
		val:float = 1 / (1 + ω)
		list_Tjω.append( val )

	for idx, ω in enumerate(omega_range):
		eq:float = math.sqrt( 1 / (1 + ω**2) )
		val2:float = 20 * math.log10( eq )
		list_Tdb.append( val2 )
		if( ω == 0.1 ):
			ωpoint1_dB_crossing_point = [omega_range[idx],int(val2)]
			print( f"ωpoint1_dB_crossing_point: {ωpoint1_dB_crossing_point}" )
		if( ω == 1 ):
			ω01_dB_crossing_point = [omega_range[idx],int(val2)]
			print( f"ω01_dB_crossing_point: {ω01_dB_crossing_point}" )
		if( ω == 10 ):
			ω10_dB_crossing_point = [omega_range[idx],int(val2)]
			print( f"ω10_dB_crossing_point: {ω10_dB_crossing_point}" )
		if( ω == 100 ):
			ω100_dB_crossing_point = [omega_range[idx],int(val2)]
			print( f"ω100_dB_crossing_point: {ω100_dB_crossing_point}" )







# 	ans_string:str = """
# ---- ({}DC op point) ----
# REPLACE THIS TEXT.
# """
	# print( ans_string )

	# print( '\n---- (a) ----' )

	# Tight_layout() doesn't quite behave as expected with semilog or log-log plots,
	# so use newer implementation with 'constrained_layout=True' parameter.
	# Hm, the above in conjunction with plt.tight_layout() -OR- fig.tight_layout()
	# still does not work (there's still 'margin' between the log-line and the axes).
	fig, ax1 = plt.subplots(constrained_layout=True)  # Create a figure and axis for the first plot
	ax1.set_xlabel('ω')  # shared x-axis
	ax1.set_ylabel('|T(ω)|dB', color='k')  # Set y-axis label for the first axis
	# ax1.set_ylabel('20log(ω/ωo)', color='k')  # Set y-axis label for the first axis

	# linear v linear ( y v x )
	# ax1.plot( omega_range, list_Tdb, color='b', label='T(ω) = 1 / (1 + ω)' )
	# ax1.plot( omega_range, list_Tjω, color='r', label='T(ω) = 1 / (1 + ω)' )

	# linear v log
	# ax1.semilogx( omega_range, list_Tjω, color='b', label=ax1_plot_label_Tjω )
	ax1.semilogx( omega_range, list_Tdb, color='b', label=ax1_plot_label_Tdb )

	# log v linear
	# ax1.semilogy( omega_range, list_log_omega, color='k', label='log' )

	# log v log
	# ax1.loglog( omega_range, list_log_omega, color='k', label='log' )


	ax1.tick_params(axis='y', labelcolor='k')
	plt.legend()  # adds a legend to label the current curve

	# Diode current - create second y-axis (id1) on to-be-shared x-axis (VPS)
	# ax2 = ax1.twinx()
	# ax2.plot( VPS_x_coord, id1, color='b', label='I(D1)' )  # customize color, recall 'k' = black
	# ax2.set_ylabel('I(D1) A', color='b')  # Set y-axis label for the second axis
	# ax2.tick_params(axis='y', labelcolor='b')
	# plt.legend()  # adds a legend to label the voltage curve

	lw:float = 2.0
	# Add a horiz guide line at unity that stops at 20log
	plt.hlines( y=ωpoint1_dB_crossing_point[1],
		xmin=omega_range[0], xmax=ωpoint1_dB_crossing_point[0],
		label=f"{ωpoint1_dB_crossing_point[1]}dB @ω=.1",
		color='purple', linestyle='--', linewidth=lw )
	# Add a vertical guide line at unity that stops at 20log
	plt.vlines( x=ωpoint1_dB_crossing_point[0],
		ymin=list_Tdb[-1], ymax=ωpoint1_dB_crossing_point[1],
		color='purple', linestyle='--', linewidth=lw )

	# Add a horiz guide line at unity that stops at 20log
	plt.hlines( y=ω01_dB_crossing_point[1],
		xmin=omega_range[0], xmax=ω01_dB_crossing_point[0],
		label=f"{ω01_dB_crossing_point[1]}dB @ω=1",
		color='r', linestyle='--', linewidth=lw )
	# Add a vertical guide line at unity that stops at 20log
	plt.vlines( x=ω01_dB_crossing_point[0],
		ymin=list_Tdb[-1], ymax=ω01_dB_crossing_point[1],
		color='r', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 10
	plt.hlines( y=ω10_dB_crossing_point[1],
		xmin=omega_range[0], xmax=ω10_dB_crossing_point[0],
		label=f"{ω10_dB_crossing_point[1]}dB @ω=10",
		color='g', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 10 that stops at 20log
	plt.vlines( x=ω10_dB_crossing_point[0],
		ymin=list_Tdb[-1], ymax=ω10_dB_crossing_point[1],
		color='g', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 100
	plt.hlines( y=ω100_dB_crossing_point[1],
		xmin=omega_range[0], xmax=ω100_dB_crossing_point[0],
		label=f"{ω100_dB_crossing_point[1]}dB @ω=100",
		color='k', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log
	plt.vlines( x=ω100_dB_crossing_point[0],
		ymin=list_Tdb[-1], ymax=ω100_dB_crossing_point[1],
		color='k', linestyle='--', linewidth=lw )





	plt.title( f"{pnum} LFP freq resp, normalized" )
	# plt.text(x=0.1, y=-80, s='τ=1', fontsize=14, color='k')

	# plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=4) )
	# plt.tight_layout()
	plt.axis('tight')
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()


# 	ans_string:str = f"""
# """
# 	print( ans_string )

	print( f"--- END {self.prob_str} ---" )




	# lw:float = 2.0
	# # Add a horiz guide line at 0.1X that stops at 20log(ω/ωo)
	# plt.hlines( y=tenthX_crossing_point[1],
	# 	xmin=omega_range[0], xmax=tenthX_crossing_point[0],
	# 	label=f"{tenthX_crossing_point[1]}dB @ω/ωo=0.1X",
	# 	color='purple', linestyle='--', linewidth=lw )
	# # Add a vertical guide line at 10X that stops at 20log(ω/ωo)
	# plt.vlines( x=tenthX_crossing_point[0],
	# 	ymin=list_log_omega[0], ymax=tenthX_crossing_point[1],
	# 	color='purple', linestyle='--', linewidth=lw )

	# # Add an entire-height horizontal guide line at unity
	# # plt.axhline( y=ω01_dB_crossing_point[1], color='k', label='unity' , linestyle='--', linewidth=lw )
	# # Add an entire-height vertical guide line at unity
	# # plt.axvline( x=ω01_dB_crossing_point[0], color='k', linestyle='--', linewidth=lw )

	# # Add a horiz guide line at unity that stops at 20log(ω/ωo)
	# plt.hlines( y=ω01_dB_crossing_point[1],
	# 	xmin=omega_range[0], xmax=ω01_dB_crossing_point[0],
	# 	label=f"{ω01_dB_crossing_point[1]}dB @ω/ωo=unity",
	# 	color='k', linestyle='--', linewidth=lw )
	# # Add a vertical guide line at unity that stops at 20log(ω/ωo)
	# plt.vlines( x=ω01_dB_crossing_point[0],
	# 	ymin=list_log_omega[0], ymax=ω01_dB_crossing_point[1],
	# 	color='k', linestyle='--', linewidth=lw )

	# # Add a horiz guide line at sqrt(2) that stops at 20log(ω/ωo)
	# plt.hlines( y=sqrt2X_crossing_point[1],
	# 	xmin=omega_range[0], xmax=sqrt2X_crossing_point[0],
	# 	label=f"{sqrt2X_crossing_point[1]}dB @ω/ωo=sqrt(2)X",
	# 	color='r', linestyle='--', linewidth=lw )
	# # Add a vertical guide line at sqrt(2) that stops at 20log(ω/ωo)
	# plt.vlines( x=sqrt2X_crossing_point[0],
	# 	ymin=list_log_omega[0], ymax=sqrt2X_crossing_point[1],
	# 	color='r', linestyle='--', linewidth=lw )


	# # Add an entire-height horizontal guide line at 2X
	# # plt.axhline( y=twoX_crossing_point[1], color='b', label='2X' , linestyle='--', linewidth=lw )
	# # Add an entire-height vertical guide line at 2X
	# # plt.axvline( x=twoX_crossing_point[0], color='b', linestyle='--', linewidth=lw )

	# # Add a horiz guide line at 2X that stops at 20log(ω/ωo)
	# plt.hlines( y=twoX_crossing_point[1],
	# 	xmin=omega_range[0], xmax=twoX_crossing_point[0],
	# 	label=f"{twoX_crossing_point[1]}dB @ω/ωo=2X",
	# 	color='b', linestyle='--', linewidth=lw )
	# # Add a vertical guide line at 2X that stops at 20log(ω/ωo)
	# plt.vlines( x=twoX_crossing_point[0],
	# 	ymin=list_log_omega[0], ymax=twoX_crossing_point[1],
	# 	color='b', linestyle='--', linewidth=lw )


	# # Add an entire-height horizontal guide line at 10X
	# # plt.axhline( y=ω10_dB_crossing_point[1], color='g', label='10X' , linestyle='--', linewidth=lw )
	# # Add an entire-height vertical guide line at 10X
	# # plt.axvline( x=ω10_dB_crossing_point[0], color='g', linestyle='--', linewidth=lw )

	# # Add a horiz guide line at 10X that stops at 20log(ω/ωo)
	# plt.hlines( y=ω10_dB_crossing_point[1],
	# 	xmin=omega_range[0], xmax=ω10_dB_crossing_point[0],
	# 	label=f"{ω10_dB_crossing_point[1]}dB @ω/ωo=10X",
	# 	color='g', linestyle='--', linewidth=lw )
	# # Add a vertical guide line at 10X that stops at 20log(ω/ωo)
	# plt.vlines( x=ω10_dB_crossing_point[0],
	# 	ymin=list_log_omega[0], ymax=ω10_dB_crossing_point[1],
	# 	color='g', linestyle='--', linewidth=lw )

