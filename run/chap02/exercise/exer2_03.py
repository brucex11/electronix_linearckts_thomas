from inspect import currentframe

def exer2_03(self):
	"""Page 27:
	Fig 2-14: Use KVL to solve for vS and vY.
	ANS:  vS = +8V, vY = +5V.
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


	ans_string:str = f"""
For KVL, when "PUSH THRU" from negative -> positive, the voltage is POSITIVE
as passing THRU each component around the loop.

Fig 2-14 has 2 loops: 1) left  2)  right

Loop 1)
  +vS  - 2  - 6  =  0
  +vS =  2  + 6  = 8V    <==========================

Loop 2)
  +6   - vY  -  1  =  0
  +6         -  1  =  vY
  +5 = vY                <==========================
"""
	print( ans_string, end='' )

	print( f"--- END {self.prob_str} ---" )
