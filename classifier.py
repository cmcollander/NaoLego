def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 22233.0:
		if diff <= 17396.0:
			if yValue <= 187.5:
				return True
			else:  # if yValue > 187.5
				return True
		else:  # if diff > 17396.0
			if yValue <= 189.0:
				if yValue <= 169.5:
					return False
				else:  # if yValue > 169.5
					return False
			else:  # if yValue > 189.0
				if yValue <= 364.0:
					if OpenConnectors <= 4.5:
						return True
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 364.0
					if yValue <= 431.5:
						return True
					else:  # if yValue > 431.5
						return True
	else:  # if diff > 22233.0
		if diff <= 38539.0:
			if Layers <= 3.5:
				if diff <= 26504.0:
					if yValue <= 422.5:
						return False
					else:  # if yValue > 422.5
						return False
				else:  # if diff > 26504.0
					if yValue <= 381.5:
						return False
					else:  # if yValue > 381.5
						return False
			else:  # if Layers > 3.5
				if yValue <= 419.5:
					if diff <= 31484.5:
						return True
					else:  # if diff > 31484.5
						return False
				else:  # if yValue > 419.5
					if Conns <= 15.0:
						return True
					else:  # if Conns > 15.0
						return True
		else:  # if diff > 38539.0
			return False
