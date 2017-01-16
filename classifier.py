def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20577.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if diff <= 13043.5:
					return True
				else:  # if diff > 13043.5
					return True
			else:  # if diff > 16402.5
				if diff <= 19010.0:
					return False
				else:  # if diff > 19010.0
					if yValue <= 170.5:
						return False
					else:  # if yValue > 170.5
						return False
		else:  # if yValue > 189.0
			if diff <= 17396.0:
				return True
			else:  # if diff > 17396.0
				if yValue <= 276.0:
					if OpenConnectors <= 4.5:
						return False
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 276.0
					if yValue <= 364.5:
						return True
					else:  # if yValue > 364.5
						return True
	else:  # if diff > 20577.0
		if OpenConnectors <= 4.5:
			if yValue <= 330.5:
				if yValue <= 145.5:
					return False
				else:  # if yValue > 145.5
					if yValue <= 314.5:
						return False
					else:  # if yValue > 314.5
						return False
			else:  # if yValue > 330.5
				if diff <= 23429.0:
					if yValue <= 364.0:
						return False
					else:  # if yValue > 364.0
						return True
				else:  # if diff > 23429.0
					if diff <= 29046.0:
						return False
					else:  # if diff > 29046.0
						return False
		else:  # if OpenConnectors > 4.5
			if diff <= 25687.5:
				if yValue <= 386.0:
					if diff <= 23247.0:
						return True
					else:  # if diff > 23247.0
						return False
				else:  # if yValue > 386.0
					if diff <= 23328.0:
						return True
					else:  # if diff > 23328.0
						return True
			else:  # if diff > 25687.5
				if OpenConnectors <= 9.5:
					if Layers <= 3.5:
						return False
					else:  # if Layers > 3.5
						return False
				else:  # if OpenConnectors > 9.5
					if diff <= 31453.0:
						return True
					else:  # if diff > 31453.0
						return False
