def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	sum_=0
	if len(a[0]) == len(b):
		max = len(a)
		max_in = len(b)
		out =[]
		for i in range(max):
			for j in range(max_in):
				sum_ += a[i][j] * b[j]
			out.append(sum_)
			sum_=0
		return out
	else:
		return -1
	# If the number of columns in 'a' does not match the length of 'b', return -1.
