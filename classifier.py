def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 22233.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if diff <= 13099.0:
					return True
				else:  # if diff > 13099.0
					return True
			else:  # if diff > 16402.5
				if yValue <= 169.5:
					return False
				else:  # if yValue > 169.5
					if yValue <= 176.5:
						return True
					else:  # if yValue > 176.5
						return False
		else:  # if yValue > 189.0
			if diff <= 19999.0:
				if diff <= 17396.0:
					return True
				else:  # if diff > 17396.0
					if yValue <= 279.5:
						if OpenConnectors <= 4.5:
							return False
						else:  # if OpenConnectors > 4.5
							return True
					else:  # if yValue > 279.5
						if diff <= 18190.5:
							if yValue <= 345.5:
								return True
							else:  # if yValue > 345.5
								return True
						else:  # if diff > 18190.5
							if Layers <= 2.5:
								return True
							else:  # if Layers > 2.5
								return True
			else:  # if diff > 19999.0
				if yValue <= 324.0:
					if Conns <= 11.0:
						if Conns <= 5.0:
							return True
						else:  # if Conns > 5.0
							return False
					else:  # if Conns > 11.0
						return True
				else:  # if yValue > 324.0
					if OpenConnectors <= 4.5:
						if yValue <= 364.0:
							return True
						else:  # if yValue > 364.0
							return True
					else:  # if OpenConnectors > 4.5
						if yValue <= 353.0:
							return True
						else:  # if yValue > 353.0
							return True
	else:  # if diff > 22233.0
		if OpenConnectors <= 8.5:
			if diff <= 26504.0:
				if yValue <= 393.5:
					if yValue <= 371.5:
						if yValue <= 363.0:
							if diff <= 22580.5:
								return False
							else:  # if diff > 22580.5
								return False
						else:  # if yValue > 363.0
							return True
					else:  # if yValue > 371.5
						return False
				else:  # if yValue > 393.5
					if yValue <= 422.5:
						if diff <= 25687.5:
							if OpenConnectors <= 5.5:
								return True
							else:  # if OpenConnectors > 5.5
								return True
						else:  # if diff > 25687.5
							return False
					else:  # if yValue > 422.5
						if yValue <= 430.5:
							return False
						else:  # if yValue > 430.5
							return False
			else:  # if diff > 26504.0
				if Layers <= 3.5:
					if Layers <= 1.5:
						if diff <= 29046.0:
							if yValue <= 371.5:
								return False
							else:  # if yValue > 371.5
								return False
						else:  # if diff > 29046.0
							if yValue <= 329.5:
								return False
							else:  # if yValue > 329.5
								return False
					else:  # if Layers > 1.5
						if OpenConnectors <= 6.5:
							return False
						else:  # if OpenConnectors > 6.5
							if yValue <= 392.5:
								return False
							else:  # if yValue > 392.5
								return False
				else:  # if Layers > 3.5
					if diff <= 32622.5:
						if yValue <= 347.0:
							if OpenConnectors <= 7.5:
								return True
							else:  # if OpenConnectors > 7.5
								return False
						else:  # if yValue > 347.0
							if yValue <= 404.0:
								return True
							else:  # if yValue > 404.0
								return False
					else:  # if diff > 32622.5
						if yValue <= 416.5:
							return False
						else:  # if yValue > 416.5
							return False
		else:  # if OpenConnectors > 8.5
			if diff <= 31453.0:
				if yValue <= 361.5:
					if yValue <= 317.0:
						return True
					else:  # if yValue > 317.0
						return False
				else:  # if yValue > 361.5
					if yValue <= 428.5:
						return True
					else:  # if yValue > 428.5
						return True
			else:  # if diff > 31453.0
				if yValue <= 424.5:
					if yValue <= 353.5:
						return False
					else:  # if yValue > 353.5
						return False
				else:  # if yValue > 424.5
					return True
