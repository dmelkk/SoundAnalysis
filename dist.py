import numpy as np

def dist(l, r):
	d = 0
	maxd = 0
	CHUNK = len(l)
	def euclid(a, b):
		return abs((a - b + 0.0) / CHUNK) + abs(l[a] - r[b])
	for i in range(CHUNK):
		mindist = euclid(i, i)
		for j in range(int(np.min(i, abs(l[i] - r[i])))):
			if (mindist > euclid(i, i - j)):
				mindist = euclid(i, i - j)
		for j in range(int(np.min(CHUNK - i - 1, abs(l[i] - r[i])))):
			if (mindist > euclid(i, i + j)):
				mindist = euclid(i, i + j)
		d += mindist
		maxd += euclid(i, i)
	return d / maxd


