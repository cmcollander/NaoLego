def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20575.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if yValue <= 168.0:
					return True
				else:  # if yValue > 168.0
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
				if yValue <= 345.5:
					return True
				else:  # if yValue > 345.5
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
			if OpenConnectors <= 9.5:
				if diff <= 27434.5:
					return False
				else:  # if diff > 27434.5
					return False
			else:  # if OpenConnectors > 9.5
				if diff <= 28696.0:
					return True
				else:  # if diff > 28696.0
					return False
