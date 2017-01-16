def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 22233.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if yValue <= 166.5:
					return True
				else:  # if yValue > 166.5
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
						if yValue <= 292.0:
							return False
						else:  # if yValue > 292.0
							return False
					else:  # if yValue > 323.5
						if yValue <= 364.0:
							return True
						else:  # if yValue > 364.0
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
		if diff <= 38539.0:
			if OpenConnectors <= 8.5:
				if diff <= 24937.0:
					if yValue <= 397.0:
						if yValue <= 369.5:
							return False
						else:  # if yValue > 369.5
							return False
					else:  # if yValue > 397.0
						if yValue <= 422.5:
							return True
						else:  # if yValue > 422.5
							return False
				else:  # if diff > 24937.0
					if Layers <= 3.5:
						if diff <= 26702.0:
							return False
						else:  # if diff > 26702.0
							return False
					else:  # if Layers > 3.5
						if OpenConnectors <= 7.5:
							return True
						else:  # if OpenConnectors > 7.5
							return False
			else:  # if OpenConnectors > 8.5
				if diff <= 30849.5:
					if yValue <= 361.5:
						return True
					else:  # if yValue > 361.5
						if yValue <= 426.5:
							return True
						else:  # if yValue > 426.5
							return True
				else:  # if diff > 30849.5
					if yValue <= 368.0:
						return False
					else:  # if yValue > 368.0
						return True
		else:  # if diff > 38539.0
			return False
