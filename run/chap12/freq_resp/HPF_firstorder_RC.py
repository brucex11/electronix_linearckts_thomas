from inspect import currentframe
import math
from typing import List, Any  # Tuple, Dict, Set

import matplotlib.pyplot as plt

# from assertions.assertions import assert_within_percentage
# from equations.equations import to_s_k, to_s_mA, to_s_uA
# from equations.equations import equivalent_parallel_resisitance
# from equations.equations import r1_parallel_r2
# from equations.equations import current_divider


def HPF_firstorder_RC(self):
	"""2nd Ed pg 712:
	Frequency response for first-order RC HPF circuit.
	Proof the transfer-function mag & phase equations using the values
	R = 43,629Ω and C = 0.01μF.

	freq-cutoff = 364.8Hz
	ω-cutoff = 2292.1rad

	./docx/chap12/freq_resp/first-order/HPF/first-order__HPF_RConly.docx
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

	# ---- Givens --------------------
	R:float = 43629
	C:float = 0.01e-06

	
	# ---- Assumptions ---------------
	# ω_range:List[float] = [round(1 + i * 0.1, 1) for i in range(99991)]  # 99991 values from 1.0 to exactly 10,000.0
	ω_range:List[float] = [round(10 + i * 0.1, 1) for i in range(999991)]  # 99991 values from 10.0 to exactly 100,000.0
	print( f"FIRST value-ω_range: {ω_range[0]}" )
	print( f"LAST value-ω_range:  {ω_range[-1]}" )
	# print( ω_range )
	print( f"len(ω_range): {len(ω_range)}" )
	# return

	# ax1_plot_label_Tjω:str = 'T(ω)=[ω/(1+ω)]'
	# list_Tjω:List[float] = []

	# ----------------------------------------------------------------------------
	# --- mag --------------------------------------------------------------------
	# ----------------------------------------------------------------------------

	ax1_plot_label_Tdb:str = '|T(ω)|=20log[ω/sqr(1+ω^2)]'
	list_Tdb:List[float] = []
	ω100_dB_crossing_point:List[Any] = []    # ω=100
	ω1000_dB_crossing_point:List[Any] = []   # ω=1000
	ω10k_dB_crossing_point:List[Any] = []    # ω=10000
	ω100k_dB_crossing_point:List[Any] = []   # ω=100k

	ω_cutoff_crossing_point:List[Any] = []   # (ω/ωc)=1

	# T_jω:float = 1 / (1 + ω)

	# ---- Calcs ---------------------
	tau:float = (R * C)
	ωc:float = 1 / tau   # cut-off freq radians
	ωc_cutoff:float = round(ωc,1)   # round according to ω_range increment
	fc:float = ωc / (2 * math.pi)   # cut-off freq Hz
	fc_plot:float = round(fc,1)
	print( f"tau = {tau}s." )
	print( f"ωc = {ωc}rads" )
	print( f"fc = {fc} = {fc_plot}Hz" )


	# ---- Calcs ---------------------
	# for idx, ω in enumerate(ω_range):
	# 	eq:float = ω * math.sqrt( 1 / (1 + ω**2) )
	# 	val:float = eq
	# 	list_Tjω.append( val )

	for idx, ω in enumerate(ω_range):
		eq:float = ω * tau * math.sqrt( 1 / (1 + (ω/ωc)**2) )
		val2:float = 20 * math.log10( eq )
		val2 = round(val2,2)
		list_Tdb.append( val2 )
		# if( ω == 10 ):
		# 	ω10_dB_crossing_point = [ω_range[idx],val2]
		# 	print( f"ω10_dB_crossing_point: {ω10_dB_crossing_point}" )
		if( ω == 100 ):
			ω100_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω100_dB_crossing_point: {ω100_dB_crossing_point}" )
		if( ω == 1000 ):
			ω1000_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω1000_dB_crossing_point: {ω1000_dB_crossing_point}" )
		if( ω == ωc_cutoff ):
			ω_cutoff_crossing_point = [ω_range[idx],val2]
			print( f"ω_cutoff_crossing_point: {ω_cutoff_crossing_point}" )
		if( ω == 10000 ):
			ω10k_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω10k_dB_crossing_point: {ω10k_dB_crossing_point}" )
		if( ω == 100e+03 ):
			ω100k_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω100k_dB_crossing_point: {ω100k_dB_crossing_point}" )


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
	ax1.set_ylabel('|T(ω)|', color='k')  # Set y-axis label for the first axis
	# ax1.set_ylabel('20log(ω/ωo)', color='k')  # Set y-axis label for the first axis

	# linear v linear ( y v x )
	# ax1.plot( ω_range, list_Tdb, color='b', label='T(ω) = 1 / (1 + ω)' )
	# ax1.plot( ω_range, list_Tjω, color='r', label='T(ω) = 1 / (1 + ω)' )

	# linear v log
	# ax1.semilogx( ω_range, list_Tjω, color='b', label=ax1_plot_label_Tjω )
	ax1.semilogx( ω_range, list_Tdb, color='b', label=ax1_plot_label_Tdb )

	# log v linear
	# ax1.semilogy( ω_range, list_log_omega, color='k', label='log' )

	# log v log
	# ax1.loglog( ω_range, list_log_omega, color='k', label='log' )


	ax1.tick_params(axis='y', labelcolor='k')
	plt.legend()  # adds a legend to label the current curve

	# Diode current - create second y-axis (id1) on to-be-shared x-axis (VPS)
	# ax2 = ax1.twinx()
	# ax2.plot( VPS_x_coord, id1, color='b', label='I(D1)' )  # customize color, recall 'k' = black
	# ax2.set_ylabel('I(D1) A', color='b')  # Set y-axis label for the second axis
	# ax2.tick_params(axis='y', labelcolor='b')
	# plt.legend()  # adds a legend to label the voltage curve

	lw:float = 1.0
	# Add a horiz guide line at 10
	# plt.hlines( y=ω10_dB_crossing_point[1],
	# 	xmin=ω_range[0], xmax=ω10_dB_crossing_point[0],
	# 	label=f"{ω10_dB_crossing_point[1]}dB@ω/ωc=10",
	# 	color='k', linestyle='--', linewidth=lw )
	# # Add a vertical guide line at 100 that stops at 20log(10)
	# plt.vlines( x=ω10_dB_crossing_point[0],
	# 	ymin=list_Tdb[0], ymax=ω10_dB_crossing_point[1],
	# 	color='k', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 100
	plt.hlines( y=ω100_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω100_dB_crossing_point[0],
		label=f"{ω100_dB_crossing_point[1]}dB@ω/ωc=100",
		color='k', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(100)
	plt.vlines( x=ω100_dB_crossing_point[0],
		ymin=list_Tdb[0], ymax=ω100_dB_crossing_point[1],
		color='k', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 1000
	plt.hlines( y=ω1000_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω1000_dB_crossing_point[0],
		label=f"{ω1000_dB_crossing_point[1]}dB@ω/ωc=1k",
		color='purple', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 1000 that stops at 20log(1000)
	plt.vlines( x=ω1000_dB_crossing_point[0],
		ymin=list_Tdb[0], ymax=ω1000_dB_crossing_point[1],
		color='purple', linestyle='--', linewidth=lw )

	# Add a horiz guide line at cutoff
	plt.hlines( y=ω_cutoff_crossing_point[1],
		xmin=ω_range[0], xmax=ω_cutoff_crossing_point[0],
		label=f"{ω_cutoff_crossing_point[1]}dB@ω/ωc={ω_cutoff_crossing_point[0]}",
		color='r', linestyle='--', linewidth=lw )
	# Add a vertical guide line at cutoff that stops at 20log(ωc)
	plt.vlines( x=ω_cutoff_crossing_point[0],
		ymin=list_Tdb[0], ymax=ω_cutoff_crossing_point[1],
		color='r', linestyle='--', linewidth=lw )

	plt.hlines( y=ω10k_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω10k_dB_crossing_point[0],
		label=f"{ω10k_dB_crossing_point[1]}dB@ω/ωc=10k",
		color='g', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(10)
	plt.vlines( x=ω10k_dB_crossing_point[0],
		ymin=list_Tdb[0], ymax=ω10k_dB_crossing_point[1],
		color='g', linestyle='--', linewidth=lw )

	plt.hlines( y=ω100k_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω100k_dB_crossing_point[0],
		label=f"{ω100k_dB_crossing_point[1]}dB@ω/ωc=100k",
		color='cyan', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(10)
	plt.vlines( x=ω100k_dB_crossing_point[0],
		ymin=list_Tdb[0], ymax=ω100k_dB_crossing_point[1],
		color='cyan', linestyle='--', linewidth=lw )



	plt.title( f"{pnum} HFP freq resp" )
	plt.text(x=1e+04, y=-40, s=f"fc={fc_plot}Hz", fontsize=14, color='k')

	plt.xlim(left=10)

	# plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=4) )
	# plt.tight_layout()
	# plt.axis('tight')
	plt.legend()  # adds a legend to label the highlighted point
	# plt.show()


	# ----------------------------------------------------------------------------
	# --- phase ------------------------------------------------------------------
	# ----------------------------------------------------------------------------

	list_phase:List[float] = []
	ω100_dB_crossing_point:List[Any] = []    # ω=100
	ω1000_dB_crossing_point:List[Any] = []   # ω=1000
	ω10k_dB_crossing_point:List[Any] = []    # ω=10000
	ω100k_dB_crossing_point:List[Any] = []   # ω=100k

	ω_cutoff_crossing_point:List[Any] = []   # (ω/ωc)=1


	# Set K to [1 | -1]
	K:float = 1
	K_angle:float = 0
	if( K==1 ):
		K_angle = 0
	elif( K==-1 ):
		K_angle = -180
	else:
		print( 'Invalid K val, hard-exit' )
		exit()
	ax1_plot_label_phase:str = f"<K={K_angle}+90-arctan(ω/ωc)"


	# ---- Calcs ---------------------
	for idx, ω in enumerate(ω_range):
		eq:float = 180 / math.pi * math.atan(ω/ωc)
		val2:float = K_angle + 90 - eq     # 2nd Ed, pg 712
		val2 = round(val2,1)
		list_phase.append( val2 )
		if( ω == 100 ):
			ω100_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω100_dB_crossing_point: {ω100_dB_crossing_point}" )
		if( ω == 1000 ):
			ω1000_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω1000_dB_crossing_point: {ω1000_dB_crossing_point}" )
		if( ω == ωc_cutoff ):
			ω_cutoff_crossing_point = [ω_range[idx],val2]
			print( f"ω_cutoff_crossing_point: {ω_cutoff_crossing_point}" )
		if( ω == 10000 ):
			ω10k_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω10k_dB_crossing_point: {ω10k_dB_crossing_point}" )
		if( ω == 100e+03 ):
			ω100k_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω100k_dB_crossing_point: {ω100k_dB_crossing_point}" )



	fig, ax1 = plt.subplots(constrained_layout=True)  # Create a figure and axis for the first plot
	ax1.set_xlabel('ω')  # shared x-axis
	ax1.set_ylabel('<K deg', color='k')  # Set y-axis label for the first axis

	# linear v log
	# ax1.semilogx( ω_range, list_Tjω, color='b', label=ax1_plot_label_Tjω )
	ax1.semilogx( ω_range, list_phase, color='b', label=ax1_plot_label_phase )

	# log v linear
	# ax1.semilogy( ω_range, list_log_omega, color='k', label='log' )

	# log v log
	# ax1.loglog( ω_range, list_log_omega, color='k', label='log' )


	ax1.tick_params(axis='y', labelcolor='k')
	plt.legend()  # adds a legend to label the current curve

	lw:float = 1.0
	# Add a horiz guide line at 100
	plt.hlines( y=ω100_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω100_dB_crossing_point[0],
		label=f"{ω100_dB_crossing_point[1]}deg@ω/ωc=100",
		color='k', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(100)
	plt.vlines( x=ω100_dB_crossing_point[0],
		ymin=list_phase[-1], ymax=ω100_dB_crossing_point[1],
		color='k', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 1000
	plt.hlines( y=ω1000_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω1000_dB_crossing_point[0],
		label=f"{ω1000_dB_crossing_point[1]}deg@ω/ωc=1k",
		color='purple', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 1000 that stops at 20log(1000)
	plt.vlines( x=ω1000_dB_crossing_point[0],
		ymin=list_phase[-1], ymax=ω1000_dB_crossing_point[1],
		color='purple', linestyle='--', linewidth=lw )

	# Add a horiz guide line at cutoff
	plt.hlines( y=ω_cutoff_crossing_point[1],
		xmin=ω_range[0], xmax=ω_cutoff_crossing_point[0],
		label=f"{ω_cutoff_crossing_point[1]}deg@ω/ωc={ω_cutoff_crossing_point[0]}",
		color='r', linestyle='--', linewidth=lw )
	# Add a vertical guide line at cutoff that stops at 20log(ωc)
	plt.vlines( x=ω_cutoff_crossing_point[0],
		ymin=list_phase[-1], ymax=ω_cutoff_crossing_point[1],
		color='r', linestyle='--', linewidth=lw )

	plt.hlines( y=ω10k_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω10k_dB_crossing_point[0],
		label=f"{ω10k_dB_crossing_point[1]}deg@ω/ωc=10k",
		color='g', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(10)
	plt.vlines( x=ω10k_dB_crossing_point[0],
		ymin=list_phase[-1], ymax=ω10k_dB_crossing_point[1],
		color='g', linestyle='--', linewidth=lw )

	plt.hlines( y=ω100k_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω100k_dB_crossing_point[0],
		label=f"{ω100k_dB_crossing_point[1]}deg@ω/ωc=100k",
		color='cyan', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(10)
	plt.vlines( x=ω100k_dB_crossing_point[0],
		ymin=list_phase[-1], ymax=ω100k_dB_crossing_point[1],
		color='cyan', linestyle='--', linewidth=lw )



	plt.title( f"{pnum} HFP freq resp" )

	if( K == 1 ):
		plt.text(x=1e+04, y=85, s=f"K={K}", fontsize=14, color='k')
		plt.text(x=1e+04, y=75, s=f"fc={fc_plot}Hz", fontsize=14, color='k')
	else:  # K=-1
		plt.text(x=15, y=-150, s=f"K={K}", fontsize=14, color='k')
		plt.text(x=15, y=-160, s=f"fc={fc_plot}Hz", fontsize=14, color='k')

	plt.xlim(left=10)
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()



# 	ans_string:str = f"""
# """
# 	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
