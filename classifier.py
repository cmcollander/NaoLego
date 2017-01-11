def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20575.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if Layers <= 1.5:
					return True
				else:  # if Layers > 1.5
					return True
			else:  # if diff > 16402.5
				if diff <= 18932.0:
					return False
				else:  # if diff > 18932.0
					return False
		else:  # if yValue > 189.0
			if diff <= 17396.0:
				return True
			else:  # if diff > 17396.0
				if yValue <= 345.5:
					if OpenConnectors <= 4.5:
						if yValue <= 277.5:
							return False
						else:  # if yValue > 277.5
							if yValue <= 326.5:
								return False
							else:  # if yValue > 326.5
								return False
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 345.5
					if yValue <= 364.5:
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
								if yValue <= 358.5:
									if yValue <= 334.0:
										return False
									else:  # if yValue > 334.0
										return False
								else:  # if yValue > 358.5
									return True
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
				if Conns <= 7.0:
					if yValue <= 418.5:
						return True
					else:  # if yValue > 418.5
						return False
				else:  # if Conns > 7.0
					if diff <= 23328.0:
						return True
					else:  # if diff > 23328.0
						if Conns <= 13.0:
							if yValue <= 415.5:
								return True
							else:  # if yValue > 415.5
								return False
						else:  # if Conns > 13.0
							return True
		else:  # if diff > 25469.5
			if Layers <= 4.5:
				if yValue <= 349.5:
					return False
				else:  # if yValue > 349.5
					if yValue <= 410.5:
						if diff <= 27391.5:
							return True
						else:  # if diff > 27391.5
							if yValue <= 391.0:
								if diff <= 30465.5:
									return False
								else:  # if diff > 30465.5
									return False
							else:  # if yValue > 391.0
								return False
					else:  # if yValue > 410.5
						if OpenConnectors <= 7.5:
							return False
						else:  # if OpenConnectors > 7.5
							return False
			else:  # if Layers > 4.5
				if yValue <= 418.5:
					if yValue <= 317.0:
						return False
					else:  # if yValue > 317.0
						return False
				else:  # if yValue > 418.5
					return True
