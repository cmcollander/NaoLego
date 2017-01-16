def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20577.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if diff <= 13274.5:
					return True
				else:  # if diff > 13274.5
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
						if yValue <= 277.5:
							return False
						else:  # if yValue > 277.5
							return True
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 364.5
					return True
	else:  # if diff > 20577.0
		if OpenConnectors <= 4.5:
			if diff <= 29046.0:
				if yValue <= 328.0:
					if diff <= 22463.5:
						return False
					else:  # if diff > 22463.5
						if diff <= 25436.0:
							return False
						else:  # if diff > 25436.0
							return False
				else:  # if yValue > 328.0
					if diff <= 23429.0:
						if yValue <= 364.0:
							return False
						else:  # if yValue > 364.0
							return True
					else:  # if diff > 23429.0
						if yValue <= 410.5:
							return False
						else:  # if yValue > 410.5
							return False
			else:  # if diff > 29046.0
				return False
		else:  # if OpenConnectors > 4.5
			if diff <= 25687.5:
				if yValue <= 386.0:
					if diff <= 23736.0:
						if OpenConnectors <= 7.5:
							return True
						else:  # if OpenConnectors > 7.5
							return True
					else:  # if diff > 23736.0
						if diff <= 24668.5:
							return False
						else:  # if diff > 24668.5
							return False
				else:  # if yValue > 386.0
					if diff <= 23328.0:
						return True
					else:  # if diff > 23328.0
						if Conns <= 13.0:
							return True
						else:  # if Conns > 13.0
							return True
			else:  # if diff > 25687.5
				if diff <= 38823.5:
					if OpenConnectors <= 9.5:
						if Layers <= 3.5:
							return False
						else:  # if Layers > 3.5
							return False
					else:  # if OpenConnectors > 9.5
						if diff <= 30849.5:
							return True
						else:  # if diff > 30849.5
							return False
				else:  # if diff > 38823.5
					return False
