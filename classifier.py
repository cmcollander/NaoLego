def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 22233.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if yValue <= 173.5:
					return True
				else:  # if yValue > 173.5
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
					if yValue <= 279.5:
						if OpenConnectors <= 4.5:
							return False
						else:  # if OpenConnectors > 4.5
							return True
					else:  # if yValue > 279.5
						if diff <= 18190.5:
							if yValue <= 345.5:
								if diff <= 17784.0:
									return True
								else:  # if diff > 17784.0
									return True
							else:  # if yValue > 345.5
								return True
						else:  # if diff > 18190.5
							if Conns <= 7.0:
								return True
							else:  # if Conns > 7.0
								if Conns <= 9.0:
									return True
								else:  # if Conns > 9.0
									return True
			else:  # if diff > 19999.0
				if yValue <= 324.0:
					if Layers <= 3.5:
						if Conns <= 5.0:
							return True
						else:  # if Conns > 5.0
							return False
					else:  # if Layers > 3.5
						return True
				else:  # if yValue > 324.0
					if yValue <= 364.0:
						if Layers <= 2.5:
							return True
						else:  # if Layers > 2.5
							return True
					else:  # if yValue > 364.0
						if diff <= 20950.0:
							return True
						else:  # if diff > 20950.0
							return True
	else:  # if diff > 22233.0
		if OpenConnectors <= 8.5:
			if diff <= 25687.5:
				if yValue <= 362.5:
					if yValue <= 206.0:
						return True
					else:  # if yValue > 206.0
						if yValue <= 330.0:
							if diff <= 23139.5:
								if Conns <= 5.0:
									return False
								else:  # if Conns > 5.0
									return False
							else:  # if diff > 23139.5
								return False
						else:  # if yValue > 330.0
							if yValue <= 341.5:
								return True
							else:  # if yValue > 341.5
								if Conns <= 7.0:
									return False
								else:  # if Conns > 7.0
									return False
				else:  # if yValue > 362.5
					if OpenConnectors <= 5.5:
						if yValue <= 369.0:
							return True
						else:  # if yValue > 369.0
							if yValue <= 420.5:
								if yValue <= 398.5:
									return False
								else:  # if yValue > 398.5
									if Layers <= 1.5:
										return True
									else:  # if Layers > 1.5
										return True
							else:  # if yValue > 420.5
								return False
					else:  # if OpenConnectors > 5.5
						if OpenConnectors <= 6.5:
							return True
						else:  # if OpenConnectors > 6.5
							if yValue <= 419.0:
								return True
							else:  # if yValue > 419.0
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
							if diff <= 29046.0:
								if yValue <= 371.5:
									return False
								else:  # if yValue > 371.5
									if diff <= 27092.0:
										return False
									else:  # if diff > 27092.0
										return True
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
					if diff <= 35336.0:
						if OpenConnectors <= 7.5:
							if OpenConnectors <= 6.5:
								return False
							else:  # if OpenConnectors > 6.5
								if diff <= 28536.0:
									return True
								else:  # if diff > 28536.0
									return True
						else:  # if OpenConnectors > 7.5
							if yValue <= 356.0:
								return False
							else:  # if yValue > 356.0
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
					if diff <= 27800.5:
						return True
					else:  # if diff > 27800.5
						return True
			else:  # if diff > 31453.0
				if yValue <= 424.5:
					if yValue <= 353.5:
						return False
					else:  # if yValue > 353.5
						return False
				else:  # if yValue > 424.5
					return True
