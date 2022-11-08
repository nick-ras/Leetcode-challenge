class Solution():
	# def __init__(self):
	# 	moves_init = 0

	def recursive(self, m, n, hori, vert, moves):
		if (vert >= m and hori >= n):
			print(f"if {moves}")
			return moves
		if (hori < m):
			moves = moves + Solution.recursive(self, m, n, hori + 1, vert, moves + 1)
		elif (vert < m):
			moves = moves + Solution.recursive(self, m, n, hori, vert + 1, moves + 1)
		return moves
		

	def uniquePaths(self, m, n):
		hori = 0
		vert = 0
		res = Solution.recursive(self, m, n, hori, vert, int(0))
		print(f"end   {res}")

obj = Solution()
obj.uniquePaths(int(2), int(2))
