def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 22233.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if yValue <= 177.0:
					return True
				else:  # if yValue > 177.0
					return True
			else:  # if diff > 16402.5
				if yValue <= 169.5:
					return False
				else:  # if yValue > 169.5
					if diff <= 19010.0:
						return False
					else:  # if diff > 19010.0
						return True
		else:  # if yValue > 189.0
			if diff <= 19999.0:
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
			else:  # if diff > 19999.0
				if OpenConnectors <= 4.5:
					if yValue <= 323.5:
						if Conns <= 5.0:
							return True
						else:  # if Conns > 5.0
							return False
					else:  # if yValue > 323.5
						if diff <= 21105.0:
							return True
						else:  # if diff > 21105.0
							return True
				else:  # if OpenConnectors > 4.5
					if yValue <= 351.0:
						if Conns <= 13.0:
							return True
						else:  # if Conns > 13.0
							return True
					else:  # if yValue > 351.0
						return True
	else:  # if diff > 22233.0
		if OpenConnectors <= 8.5:
			if diff <= 27407.0:
				if yValue <= 422.5:
					if yValue <= 397.0:
						if yValue <= 363.0:
							return False
						else:  # if yValue > 363.0
							return False
					else:  # if yValue > 397.0
						if diff <= 25687.5:
							return True
						else:  # if diff > 25687.5
							return False
				else:  # if yValue > 422.5
					if yValue <= 438.5:
						return False
					else:  # if yValue > 438.5
						return False
			else:  # if diff > 27407.0
				if Layers <= 3.5:
					if diff <= 29001.0:
						return False
					else:  # if diff > 29001.0
						if diff <= 38539.0:
							return False
						else:  # if diff > 38539.0
							return False
				else:  # if Layers > 3.5
					if diff <= 32622.5:
						if yValue <= 347.0:
							return False
						else:  # if yValue > 347.0
							return True
					else:  # if diff > 32622.5
						if yValue <= 418.5:
							return False
						else:  # if yValue > 418.5
							return False
		else:  # if OpenConnectors > 8.5
			if diff <= 30849.5:
				if yValue <= 361.5:
					if yValue <= 303.5:
						return True
					else:  # if yValue > 303.5
						return True
				else:  # if yValue > 361.5
					if yValue <= 430.0:
						return True
					else:  # if yValue > 430.0
						return True
			else:  # if diff > 30849.5
				if diff <= 38823.5:
					if diff <= 33248.5:
						return False
					else:  # if diff > 33248.5
						if yValue <= 388.0:
							return True
						else:  # if yValue > 388.0
							return True
				else:  # if diff > 38823.5
					return False
