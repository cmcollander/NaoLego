def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20575.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if diff <= 13054.5:
					return True
				else:  # if diff > 13054.5
					return True
			else:  # if diff > 16402.5
				if diff <= 19010.0:
					return False
				else:  # if diff > 19010.0
					if diff <= 19267.5:
						return True
					else:  # if diff > 19267.5
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
							if Layers <= 1.5:
								return True
							else:  # if Layers > 1.5
								return False
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 364.5
					return True
	else:  # if diff > 20575.0
		if diff <= 25687.5:
			if OpenConnectors <= 4.5:
				if yValue <= 314.5:
					return False
				else:  # if yValue > 314.5
					if yValue <= 417.0:
						if Layers <= 1.5:
							if diff <= 22596.5:
								return False
							else:  # if diff > 22596.5
								return False
						else:  # if Layers > 1.5
							if yValue <= 337.0:
								return False
							else:  # if yValue > 337.0
								return True
					else:  # if yValue > 417.0
						return False
			else:  # if OpenConnectors > 4.5
				if yValue <= 386.0:
					if yValue <= 355.5:
						if Conns <= 15.0:
							if diff <= 23736.0:
								return True
							else:  # if diff > 23736.0
								return False
						else:  # if Conns > 15.0
							return True
					else:  # if yValue > 355.5
						return False
				else:  # if yValue > 386.0
					if diff <= 23328.0:
						return True
					else:  # if diff > 23328.0
						if Conns <= 13.0:
							if yValue <= 416.5:
								return True
							else:  # if yValue > 416.5
								return False
						else:  # if Conns > 13.0
							return True
		else:  # if diff > 25687.5
			if OpenConnectors <= 6.5:
				if yValue <= 349.5:
					return False
				else:  # if yValue > 349.5
					if yValue <= 410.5:
						if diff <= 27265.0:
							if yValue <= 400.0:
								return False
							else:  # if yValue > 400.0
								return True
						else:  # if diff > 27265.0
							if Layers <= 3.5:
								return False
							else:  # if Layers > 3.5
								return True
					else:  # if yValue > 410.5
						return False
			else:  # if OpenConnectors > 6.5
				if diff <= 30936.5:
					if diff <= 30136.5:
						if diff <= 28691.5:
							if Layers <= 3.5:
								return False
							else:  # if Layers > 3.5
								return True
						else:  # if diff > 28691.5
							return False
					else:  # if diff > 30136.5
						return True
				else:  # if diff > 30936.5
					if yValue <= 435.0:
						return False
					else:  # if yValue > 435.0
						return False
