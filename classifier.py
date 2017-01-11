def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20575.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				return True
			else:  # if diff > 16402.5
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
							return True
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 345.5
					if yValue <= 364.5:
						return True
					else:  # if yValue > 364.5
						return True
	else:  # if diff > 20575.0
		if OpenConnectors <= 4.5:
			if yValue <= 314.5:
				return False
			else:  # if yValue > 314.5
				if diff <= 22906.5:
					if yValue <= 351.5:
						return False
					else:  # if yValue > 351.5
						return True
				else:  # if diff > 22906.5
					if yValue <= 410.5:
						if diff <= 27333.5:
							return False
						else:  # if diff > 27333.5
							return False
					else:  # if yValue > 410.5
						return False
		else:  # if OpenConnectors > 4.5
			if diff <= 25687.5:
				if yValue <= 386.0:
					if diff <= 23321.0:
						if OpenConnectors <= 7.5:
							return False
						else:  # if OpenConnectors > 7.5
							return True
					else:  # if diff > 23321.0
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
				if OpenConnectors <= 9.5:
					if OpenConnectors <= 7.5:
						if OpenConnectors <= 6.5:
							return False
						else:  # if OpenConnectors > 6.5
							return False
					else:  # if OpenConnectors > 7.5
						return False
				else:  # if OpenConnectors > 9.5
					return False
