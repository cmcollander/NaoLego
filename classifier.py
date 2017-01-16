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
								if Conns <= 9.0:
									return True
								else:  # if Conns > 9.0
									return True
			else:  # if diff > 19999.0
				if OpenConnectors <= 4.5:
					if yValue <= 323.5:
						if Conns <= 5.0:
							return True
						else:  # if Conns > 5.0
							return False
					else:  # if yValue > 323.5
						if yValue <= 364.0:
							return True
						else:  # if yValue > 364.0
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
		if OpenConnectors <= 8.5:
			if diff <= 27407.0:
				if yValue <= 422.5:
					if yValue <= 397.0:
						if diff <= 22349.5:
							return False
						else:  # if diff > 22349.5
							if diff <= 22622.0:
								return True
							else:  # if diff > 22622.0
								if yValue <= 286.5:
									return False
								else:  # if yValue > 286.5
									return False
					else:  # if yValue > 397.0
						if diff <= 25687.5:
							if Conns <= 9.0:
								if diff <= 23381.0:
									return True
								else:  # if diff > 23381.0
									return False
							else:  # if Conns > 9.0
								if yValue <= 417.5:
									return True
								else:  # if yValue > 417.5
									return True
						else:  # if diff > 25687.5
							if yValue <= 412.0:
								return True
							else:  # if yValue > 412.0
								return False
				else:  # if yValue > 422.5
					if OpenConnectors <= 5.0:
						return False
					else:  # if OpenConnectors > 5.0
						return False
			else:  # if diff > 27407.0
				if Layers <= 3.5:
					if diff <= 29001.0:
						return False
					else:  # if diff > 29001.0
						if diff <= 38539.0:
							if diff <= 32962.5:
								if diff <= 30249.0:
									return False
								else:  # if diff > 30249.0
									return False
							else:  # if diff > 32962.5
								return True
						else:  # if diff > 38539.0
							return False
				else:  # if Layers > 3.5
					if diff <= 32622.5:
						if OpenConnectors <= 7.5:
							if diff <= 28536.0:
								return True
							else:  # if diff > 28536.0
								return True
						else:  # if OpenConnectors > 7.5
							if yValue <= 334.5:
								return False
							else:  # if yValue > 334.5
								return True
					else:  # if diff > 32622.5
						if yValue <= 416.5:
							return False
						else:  # if yValue > 416.5
							return False
		else:  # if OpenConnectors > 8.5
			if diff <= 30849.5:
				if yValue <= 361.5:
					if yValue <= 317.0:
						return True
					else:  # if yValue > 317.0
						return True
				else:  # if yValue > 361.5
					if Conns <= 15.0:
						return True
					else:  # if Conns > 15.0
						return True
			else:  # if diff > 30849.5
				if diff <= 38823.5:
					if diff <= 33248.5:
						return False
					else:  # if diff > 33248.5
						if yValue <= 388.0:
							return True
						else:  # if yValue > 388.0
							return True
				else:  # if diff > 38823.5
					return False
