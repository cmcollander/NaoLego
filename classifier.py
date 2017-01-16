def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20575.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if yValue <= 177.0:
					return True
				else:  # if yValue > 177.0
					return True
			else:  # if diff > 16402.5
				if diff <= 19010.0:
					return False
				else:  # if diff > 19010.0
					return False
		else:  # if yValue > 189.0
			if diff <= 17396.0:
				return True
			else:  # if diff > 17396.0
				if yValue <= 276.0:
					return True
				else:  # if yValue > 276.0
					return True
	else:  # if diff > 20575.0
		if OpenConnectors <= 4.5:
			if yValue <= 364.0:
				if yValue <= 314.5:
					return False
				else:  # if yValue > 314.5
					return False
			else:  # if yValue > 364.0
				if diff <= 22933.0:
					return True
				else:  # if diff > 22933.0
					return False
		else:  # if OpenConnectors > 4.5
			if diff <= 25687.5:
				if yValue <= 386.0:
					return False
				else:  # if yValue > 386.0
					return True
			else:  # if diff > 25687.5
				if yValue <= 296.5:
					return True
				else:  # if yValue > 296.5
					return False
