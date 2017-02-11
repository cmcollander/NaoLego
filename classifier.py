def tree(Conns, OpenConnectors, Layers, yValue, diff):
	if diff <= 22233.0:
		if yValue <= 189.0:
			if diff <= 16402.5:
				if diff <= 13310.5:
					return True
				else:  # if diff > 13310.5
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
			if diff <= 20791.0:
				if diff <= 17396.0:
					return True
				else:  # if diff > 17396.0
					if yValue <= 276.0:
						if OpenConnectors <= 4.5:
							return False
						else:  # if OpenConnectors > 4.5
							return True
					else:  # if yValue > 276.0
						if diff <= 18190.5:
							return True
						else:  # if diff > 18190.5
							return True
			else:  # if diff > 20791.0
				if yValue <= 336.0:
					if OpenConnectors <= 4.5:
						if diff <= 21315.5:
							return False
						else:  # if diff > 21315.5
							return False
					else:  # if OpenConnectors > 4.5
						return True
				else:  # if yValue > 336.0
					if diff <= 22001.0:
						if diff <= 21245.5:
							return True
						else:  # if diff > 21245.5
							return True
					else:  # if diff > 22001.0
						return True
	else:  # if diff > 22233.0
		if diff <= 38539.0:
			if Layers <= 4.5:
				if diff <= 28493.0:
					if OpenConnectors <= 5.5:
						if yValue <= 420.5:
							return False
						else:  # if yValue > 420.5
							return False
					else:  # if OpenConnectors > 5.5
						if yValue <= 422.5:
							return True
						else:  # if yValue > 422.5
							return False
				else:  # if diff > 28493.0
					if diff <= 29812.0:
						if yValue <= 411.0:
							return False
						else:  # if yValue > 411.0
							return False
					else:  # if diff > 29812.0
						if diff <= 30249.0:
							return True
						else:  # if diff > 30249.0
							return False
			else:  # if Layers > 4.5
				if yValue <= 419.5:
					if OpenConnectors <= 9.5:
						if diff <= 27104.0:
							return False
						else:  # if diff > 27104.0
							return True
					else:  # if OpenConnectors > 9.5
						if diff <= 31453.0:
							return True
						else:  # if diff > 31453.0
							return True
				else:  # if yValue > 419.5
					if OpenConnectors <= 9.5:
						return True
					else:  # if OpenConnectors > 9.5
						return True
		else:  # if diff > 38539.0
			return False
