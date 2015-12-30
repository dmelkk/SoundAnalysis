import numpy as np

def dist(l, r):
	d = 0
	maxd = 0
	CHUNK = len(l)
	def nmin(a, b):
		if (a > b):
			return b
		return a
	def euclid(a, b):
		return abs((a - b + 0.0) / CHUNK) + abs(l[a] - r[b])

	l = abs(l)
	r = abs(r)

	for i in range(CHUNK):
		mindist = euclid(i, i)
		for j in range(nmin(i, int( CHUNK * (abs(l[i] - r[i]))))):
			if (mindist > euclid(i, i - j)):
				mindist = euclid(i, i - j)
		for j in range(nmin(CHUNK - i - 1, int(CHUNK * (abs(l[i] - r[i]))))):
			if (mindist > euclid(i, i + j)):
				mindist = euclid(i, i + j)
		d += mindist
		maxd += abs(l[i])
	if maxd == 0:
		return 0
	return d / maxd
