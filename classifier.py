def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20575.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if Layers <= 1.5:
					return True
				else:  # if Layers > 1.5
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
				if yValue <= 276.0:
					if OpenConnectors <= 4.5:
						return False
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 276.0
					if yValue <= 364.5:
						if OpenConnectors <= 4.5:
							return True
						else:  # if OpenConnectors > 4.5
							return True
					else:  # if yValue > 364.5
						return True
	else:  # if diff > 20575.0
		if diff <= 25469.5:
			if OpenConnectors <= 4.5:
				if yValue <= 314.5:
					return False
				else:  # if yValue > 314.5
					if diff <= 22906.5:
						if yValue <= 364.0:
							return False
						else:  # if yValue > 364.0
							return True
					else:  # if diff > 22906.5
						if yValue <= 368.0:
							return True
						else:  # if yValue > 368.0
							return False
			else:  # if OpenConnectors > 4.5
				if yValue <= 386.0:
					if diff <= 21971.0:
						if OpenConnectors <= 6.5:
							return False
						else:  # if OpenConnectors > 6.5
							return True
					else:  # if diff > 21971.0
						if OpenConnectors <= 8.5:
							return False
						else:  # if OpenConnectors > 8.5
							return True
				else:  # if yValue > 386.0
					if diff <= 23328.0:
						return True
					else:  # if diff > 23328.0
						if Conns <= 13.0:
							return True
						else:  # if Conns > 13.0
							return True
		else:  # if diff > 25469.5
			if OpenConnectors <= 6.5:
				if yValue <= 349.5:
					return False
				else:  # if yValue > 349.5
					if yValue <= 417.0:
						if diff <= 27265.0:
							return False
						else:  # if diff > 27265.0
							return False
					else:  # if yValue > 417.0
						return False
			else:  # if OpenConnectors > 6.5
				if diff <= 28691.5:
					if yValue <= 420.0:
						if Conns <= 13.0:
							return True
						else:  # if Conns > 13.0
							return False
					else:  # if yValue > 420.0
						return True
				else:  # if diff > 28691.5
					if OpenConnectors <= 7.5:
						if diff <= 35336.0:
							return True
						else:  # if diff > 35336.0
							return False
					else:  # if OpenConnectors > 7.5
						return False
