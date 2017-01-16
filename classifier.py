def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 22233.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if diff <= 13099.0:
					return True
				else:  # if diff > 13099.0
					return True
			else:  # if diff > 16402.5
				if yValue <= 172.0:
					return False
				else:  # if yValue > 172.0
					return False
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
					if yValue <= 364.0:
						if diff <= 21197.0:
							return False
						else:  # if diff > 21197.0
							return False
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
		if OpenConnectors <= 8.5:
			if diff <= 25687.5:
				if yValue <= 362.5:
					if yValue <= 206.0:
						return True
					else:  # if yValue > 206.0
						if yValue <= 330.0:
							return False
						else:  # if yValue > 330.0
							return False
				else:  # if yValue > 362.5
					if Conns <= 9.0:
						if yValue <= 369.0:
							return True
						else:  # if yValue > 369.0
							return False
					else:  # if Conns > 9.0
						if OpenConnectors <= 6.5:
							return True
						else:  # if OpenConnectors > 6.5
							return True
			else:  # if diff > 25687.5
				if Layers <= 3.5:
					if diff <= 26504.0:
						if diff <= 26241.5:
							return False
						else:  # if diff > 26241.5
							return True
					else:  # if diff > 26504.0
						if Layers <= 1.5:
							return False
						else:  # if Layers > 1.5
							return False
				else:  # if Layers > 3.5
					if diff <= 35336.0:
						if OpenConnectors <= 7.5:
							return True
						else:  # if OpenConnectors > 7.5
							return False
					else:  # if diff > 35336.0
						return False
		else:  # if OpenConnectors > 8.5
			if diff <= 31453.0:
				if yValue <= 361.5:
					if yValue <= 317.0:
						return True
					else:  # if yValue > 317.0
						return False
				else:  # if yValue > 361.5
					if Conns <= 15.0:
						return True
					else:  # if Conns > 15.0
						return True
			else:  # if diff > 31453.0
				if yValue <= 424.5:
					if yValue <= 353.5:
						return False
					else:  # if yValue > 353.5
						return False
				else:  # if yValue > 424.5
					return True
