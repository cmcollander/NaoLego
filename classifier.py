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
					if diff <= 19010.0:
						return False
					else:  # if diff > 19010.0
						return True
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
							if Layers <= 2.5:
								return True
							else:  # if Layers > 2.5
								if yValue <= 357.5:
									return True
								else:  # if yValue > 357.5
									return True
			else:  # if diff > 19999.0
				if OpenConnectors <= 4.5:
					if yValue <= 323.5:
						if Layers <= 1.5:
							return True
						else:  # if Layers > 1.5
							return False
					else:  # if yValue > 323.5
						if diff <= 21105.0:
							return True
						else:  # if diff > 21105.0
							return True
				else:  # if OpenConnectors > 4.5
					if yValue <= 351.0:
						if Conns <= 13.0:
							if diff <= 21342.5:
								return True
							else:  # if diff > 21342.5
								return True
						else:  # if Conns > 13.0
							return True
					else:  # if yValue > 351.0
						return True
	else:  # if diff > 22233.0
		if diff <= 38539.0:
			if Conns <= 15.0:
				if diff <= 24992.0:
					if yValue <= 397.0:
						if yValue <= 369.5:
							if yValue <= 362.5:
								if diff <= 22963.0:
									return False
								else:  # if diff > 22963.0
									return False
							else:  # if yValue > 362.5
								return True
						else:  # if yValue > 369.5
							return False
					else:  # if yValue > 397.0
						if OpenConnectors <= 5.5:
							if yValue <= 420.5:
								if diff <= 23381.0:
									return True
								else:  # if diff > 23381.0
									return True
							else:  # if yValue > 420.5
								return False
						else:  # if OpenConnectors > 5.5
							if Layers <= 3.5:
								return True
							else:  # if Layers > 3.5
								return True
				else:  # if diff > 24992.0
					if OpenConnectors <= 6.5:
						if diff <= 26702.0:
							if diff <= 26405.5:
								if yValue <= 365.5:
									return False
								else:  # if yValue > 365.5
									return False
							else:  # if diff > 26405.5
								return True
						else:  # if diff > 26702.0
							if diff <= 32491.5:
								if yValue <= 329.5:
									return False
								else:  # if yValue > 329.5
									return False
							else:  # if diff > 32491.5
								return True
					else:  # if OpenConnectors > 6.5
						if diff <= 30769.0:
							if yValue <= 358.5:
								if OpenConnectors <= 7.5:
									return True
								else:  # if OpenConnectors > 7.5
									return False
							else:  # if yValue > 358.5
								if yValue <= 414.0:
									return True
								else:  # if yValue > 414.0
									return False
						else:  # if diff > 30769.0
							if yValue <= 416.5:
								return False
							else:  # if yValue > 416.5
								return True
			else:  # if Conns > 15.0
				if diff <= 25770.0:
					return True
				else:  # if diff > 25770.0
					if yValue <= 417.0:
						if Conns <= 17.0:
							if yValue <= 354.0:
								return True
							else:  # if yValue > 354.0
								return False
						else:  # if Conns > 17.0
							return False
					else:  # if yValue > 417.0
						return True
		else:  # if diff > 38539.0
			return False
