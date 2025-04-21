from inspect import currentframe

def exer2_02(self):
	"""Page 25:
	(a) Write the KCL equations for each node A B C D.
	Given i1 = -1mA, i3 = 0.5mA, and i6 = 0.2mA, find i2, i4, and i5.
	ANS(b):  i2 = 1mA, i4 = 0.5mA, i5 = 0.3mA.
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
	i1:float = -1
	i3:float = 0.5
	i6:float = 0.2


	# ---- Assumptions ---------------
	VBE:float = 0.7   # V

	# ---- Calcs ---------------------
	calc_result:float = 0


	ans_string:str = f"""
Choose node D as the reference.
The main discipline is to be consistent with direction of currents always 
being POSITIVE IN to the node.

KCL: the algebraic sum of currents entering a node = 0 at every instant.

  Node A:
  Since given current directions are OUT of the node, then:
    -i1 + (-i2)  = 0
    -i1  -  i2   = 0         (1)

  Node B: (similarly per given directions)
    i2 + (-i3) + (-i4) = 0
    i2  -  i3  -  i4 = 0     (2)

  Node C: (similarly per given directions)
    i4 + (-i5) + (-i6) = 0
    i4  -  i5  -  i6 = 0     (3)

  Node D: (similarly per given directions)
    i1 + i3 + i5 + i6 = 0

Therefore, there are 3 equations and 3 unknowns.

Substitute i1 in (1) and solve for i2:

  -({i1}) - i2 = 0
  i2 = -({i1})
"""
	print( ans_string, end='' )

	i2:float = -(i1)
	print( f"  i2 = {i2}      <=================" )


	ans_string = f"""
Sum (1) (2) (3):

    -i1  -  i2                             = 0     (1)
            i2  -  i3  -  i4               = 0     (2)
 +                        i4  -  i5  -  i6 = 0     (3)
  -------------------------------------------
    -i1 +  0i2 -   i3  + 0i4  -  i5  -  i6 = 0

    -i1        -i3 +     - i5 - i6 = 0
    -({i1})    -{i3} +   - i5 - {i6} = 0
    -({i1})    -{i3}  - {i6} = i5

"""
	print( ans_string, end='' )

	i5:float = -(i1) -i3  - i6
	print( f"  i5 = {i5}      <=================" )


	ans_string = f"""
Sub i5 into (3), solve for i4:

  i4  -  i5  -  i6 = 0     (3)
  i4  =  i5  +  i6
  i4  =  {i5}  +  {i6}
"""
	print( ans_string, end='' )

	i4:float = i5 + i6
	print( f"  i4 = {i4}      <=================" )

	print( f"\n--- END {self.prob_str} ---" )
