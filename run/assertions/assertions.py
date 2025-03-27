
def assert_within_percentage( actual:float, expected:float, percentage:float=5.0 ) -> None:
	"""
	Usage single value:
	ans_a:float = 0.518e-03   # A
	try:
		assertions.assert_within_percentage( iDS, ans_a, assert_percentage )
		print( f"ASSERT NMOS iDS = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_a:.3e}." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	try:
		assertions.assert_within_percentage( iSD, ans_a, assert_percentage )
		print( f"ASSERT PMOS enhancement mode in saturation: iSD = {round(iSD,7)}V", end=' ' )
		print( f"is within {assert_percentage}% of accepted answer {ans_a}V." )
	except AssertionError as e:
		print( f"ASSERT AssertionError {pnum}: {e}" )

	Usage with List:
	list_calc_iD:List[float] = []   #  don't forget to use list_calc_iD.append(val) to load the list!!
	ans_a_iDS:Tuple = (0.518e-03, 0.691e-03, 0.691e-03)   #
	for idx, ans_iDS in enumerate(ans_a_iDS):
		try:
			assertions.assert_within_percentage( list_calc_iDS[idx], ans_iDS, assert_percentage )
			print( f"ASSERT NMOS iDS = {list_calc_iDS[idx]:.3e}A is within {assert_percentage}% of accepted answer: {ans_iDS:.3e}." )
		except AssertionError as e:
			print( f"ASSERT AssertionError {pnum}: {e}" )


		Args:
			actual:float the calculated value to check
			expected:float the target value
			percentage:float default=5%
	"""
	tolerance = expected * ( percentage / 100.0 )
	# print( f"abs(actual - expected) ?= tolerance -- {abs(actual - expected)} ?= {abs(tolerance)}" )
	# config the output number format
	if( (actual > 1000) or (actual < 0.001) ):
		o_msg = f"Actual {actual:.3e} is not within {percentage}% of expected {expected:.3e}"
	else:
		o_msg = f"Actual {actual:.3e} is not within {percentage}% of expected {expected}"

	assert abs(actual - expected) <= abs(tolerance), o_msg
