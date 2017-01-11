def tree(blueConns, greenConns, redConns, darkBlueConns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20575.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if diff <= 14006.5:
					return True
				else:  # if diff > 14006.5
					return True
			else:  # if diff > 16402.5
				if redConns <= 1.0:
					return False
				else:  # if redConns > 1.0
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
							if redConns <= 2.0:
								return True
							else:  # if redConns > 2.0
								return False
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 364.5
					return True
	else:  # if diff > 20575.0
		if diff <= 25469.5:
			if yValue <= 403.0:
				if Layers <= 3.5:
					if diff <= 22524.5:
						return False
					else:  # if diff > 22524.5
						if yValue <= 369.0:
							if yValue <= 309.0:
								return False
							else:  # if yValue > 309.0
								if yValue <= 342.5:
									return True
								else:  # if yValue > 342.5
									return False
						else:  # if yValue > 369.0
							return False
				else:  # if Layers > 3.5
					if diff <= 22078.5:
						return True
					else:  # if diff > 22078.5
						if OpenConnectors <= 8.5:
							return False
						else:  # if OpenConnectors > 8.5
							return True
			else:  # if yValue > 403.0
				if OpenConnectors <= 4.5:
					if yValue <= 418.5:
						return True
					else:  # if yValue > 418.5
						return False
				else:  # if OpenConnectors > 4.5
					if diff <= 23328.0:
						return True
					else:  # if diff > 23328.0
						if OpenConnectors <= 7.5:
							return True
						else:  # if OpenConnectors > 7.5
							return True
		else:  # if diff > 25469.5
			if yValue <= 350.0:
				if Layers <= 4.5:
					return False
				else:  # if Layers > 4.5
					return False
			else:  # if yValue > 350.0
				if diff <= 35310.5:
					if Layers <= 3.5:
						if yValue <= 410.5:
							if yValue <= 395.5:
								return False
							else:  # if yValue > 395.5
								return False
						else:  # if yValue > 410.5
							return False
					else:  # if Layers > 3.5
						if yValue <= 418.5:
							if greenConns <= 5.0:
								return False
							else:  # if greenConns > 5.0
								return False
						else:  # if yValue > 418.5
							return True
				else:  # if diff > 35310.5
					return False
