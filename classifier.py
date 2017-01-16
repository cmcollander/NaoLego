def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 23620.5:
		if yValue <= 168.5:
			if diff <= 14831.0:
				return True
			else:  # if diff > 14831.0
				return False
		else:  # if yValue > 168.5
			return True
	else:  # if diff > 23620.5
		if yValue <= 368.0:
			return False
		else:  # if yValue > 368.0
			if diff <= 25624.0:
				return True
			else:  # if diff > 25624.0
				if OpenConnectors <= 7.5:
					return False
				else:  # if OpenConnectors > 7.5
					if diff <= 33686.5:
						return True
					else:  # if diff > 33686.5
						return False
