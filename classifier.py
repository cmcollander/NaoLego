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
		if Layers <= 3.5:
			if yValue <= 364.5:
				if yValue <= 314.5:
					return False
				else:  # if yValue > 314.5
					return False
			else:  # if yValue > 364.5
				if diff <= 22933.0:
					return True
				else:  # if diff > 22933.0
					return False
		else:  # if Layers > 3.5
			if diff <= 25684.0:
				if yValue <= 373.5:
					return True
				else:  # if yValue > 373.5
					return True
			else:  # if diff > 25684.0
				if diff <= 28691.5:
					return False
				else:  # if diff > 28691.5
					return False
