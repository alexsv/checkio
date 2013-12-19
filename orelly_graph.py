from collections import defaultdict


def checkio(data):
	get_key = lambda x,y: "%s-%s" % ((x, y) if y > x else (y, x))
	edges = set()
	vertexes = defaultdict(lambda: [False, set()])

	def deep_search(index, result):
		if len(vertexes) == len(set(result)) and index == 1:
			return result
		for v in vertexes[index][1]:
			key = get_key(index, v)
			if key in edges:
				edges.remove(key)
				res = deep_search(v, result + [v])
				if res:
					return res
				edges.add(key)
		
	for start, finish in map(lambda x: (int(x[0]), int(x[1])), data.split(',')):
		edges.add(get_key(start, finish)) 
		vertexes[start][1].add(finish)
		vertexes[finish][1].add(start)

	return deep_search(1, [1])

if __name__ == "__main__":
	print checkio("12,28,87,71,13,14,34,35,45,46,63,65")
		