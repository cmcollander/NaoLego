def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20575.0:
		if yValue <= 189.0:
			return True
		else:  # if yValue > 189.0
			if diff <= 17396.0:
				return True
			else:  # if diff > 17396.0
				if yValue <= 364.5:
					return True
				else:  # if yValue > 364.5
					return True
	else:  # if diff > 20575.0
		if diff <= 25687.5:
			if OpenConnectors <= 4.5:
				if yValue <= 314.5:
					return False
				else:  # if yValue > 314.5
					return False
			else:  # if OpenConnectors > 4.5
				if yValue <= 386.0:
					return False
				else:  # if yValue > 386.0
					return True
		else:  # if diff > 25687.5
			if yValue <= 350.0:
				if Conns <= 11.0:
					return False
				else:  # if Conns > 11.0
					return False
			else:  # if yValue > 350.0
				if diff <= 35310.5:
					return False
				else:  # if diff > 35310.5
					return False
