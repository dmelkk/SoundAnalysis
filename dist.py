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
		return abs((a - b + 0.0) / CHUNK) + abs(abs(l[a]) - abs(r[b]))
	for i in range(CHUNK):
		mindist = euclid(i, i)
		for j in range(int(nmin(i, abs(l[i] - r[i])))):
			if (mindist > euclid(i, i - j)):
				mindist = euclid(i, i - j)
		for j in range(int(nmin(CHUNK - i - 1, abs(l[i] - r[i])))):
			if (mindist > euclid(i, i + j)):
				mindist = euclid(i, i + j)
		d += mindist
		maxd += abs(l[i])
	return d / maxd
