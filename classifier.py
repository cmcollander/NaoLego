def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20577.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if yValue <= 166.5:
					return True
				else:  # if yValue > 166.5
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
				if yValue <= 364.5:
					if OpenConnectors <= 4.5:
						return True
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 364.5
					return True
	else:  # if diff > 20577.0
		if diff <= 25532.5:
			if OpenConnectors <= 4.5:
				if yValue <= 314.5:
					if yValue <= 213.0:
						return False
					else:  # if yValue > 213.0
						return False
				else:  # if yValue > 314.5
					if yValue <= 420.5:
						return True
					else:  # if yValue > 420.5
						return False
			else:  # if OpenConnectors > 4.5
				if yValue <= 386.0:
					if diff <= 23321.0:
						return True
					else:  # if diff > 23321.0
						return False
				else:  # if yValue > 386.0
					if diff <= 23328.0:
						return True
					else:  # if diff > 23328.0
						return True
		else:  # if diff > 25532.5
			if Layers <= 3.5:
				if yValue <= 337.0:
					return False
				else:  # if yValue > 337.0
					if diff <= 27376.5:
						return False
					else:  # if diff > 27376.5
						return False
			else:  # if Layers > 3.5
				if diff <= 38823.5:
					if yValue <= 418.5:
						return False
					else:  # if yValue > 418.5
						return True
				else:  # if diff > 38823.5
					return False
