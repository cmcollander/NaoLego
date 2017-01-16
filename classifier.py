def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 20575.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if yValue <= 177.0:
					return True
				else:  # if yValue > 177.0
					return True
			else:  # if diff > 16402.5
				if diff <= 19010.0:
					return False
				else:  # if diff > 19010.0
					if diff <= 19407.0:
						return False
					else:  # if diff > 19407.0
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
	else:  # if diff > 20575.0
		if diff <= 25469.5:
			if Conns <= 7.0:
				if yValue <= 314.5:
					if yValue <= 145.5:
						return False
					else:  # if yValue > 145.5
						return False
				else:  # if yValue > 314.5
					if yValue <= 417.0:
						if Layers <= 1.5:
							return False
						else:  # if Layers > 1.5
							return True
					else:  # if yValue > 417.0
						return False
			else:  # if Conns > 7.0
				if yValue <= 386.0:
					if yValue <= 355.5:
						if diff <= 23736.0:
							return True
						else:  # if diff > 23736.0
							return False
					else:  # if yValue > 355.5
						return False
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
					if diff <= 31615.5:
						if yValue <= 410.5:
							return False
						else:  # if yValue > 410.5
							return False
					else:  # if diff > 31615.5
						return False
			else:  # if OpenConnectors > 6.5
				if diff <= 30936.5:
					if diff <= 30037.0:
						if diff <= 28691.5:
							return True
						else:  # if diff > 28691.5
							return False
					else:  # if diff > 30037.0
						return True
				else:  # if diff > 30936.5
					if yValue <= 419.0:
						return False
					else:  # if yValue > 419.0
						if diff <= 41221.5:
							return True
						else:  # if diff > 41221.5
							return False
