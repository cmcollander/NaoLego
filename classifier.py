def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 23535.5:
		if yValue <= 168.5:
			return False
		else:  # if yValue > 168.5
			if diff <= 21993.0:
				return True
			else:  # if diff > 21993.0
				if diff <= 22874.0:
					return False
				else:  # if diff > 22874.0
					return True
	else:  # if diff > 23535.5
		if yValue <= 335.0:
			return False
		else:  # if yValue > 335.0
			if OpenConnectors <= 5.5:
				return False
			else:  # if OpenConnectors > 5.5
				if diff <= 31453.0:
					return True
				else:  # if diff > 31453.0
					return False
