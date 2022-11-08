class Solution():
	# def __init__(self):
	# 	moves_init = 0

	def recursive(self, m, n, hori, vert, moves):
		if (vert >= m and hori >= n):
			print(f"hey{moves}")
			return moves
		print(moves)
		if (hori < m):
			Solution.recursive(self, m, n, hori + 1, vert, moves + 1)
		if (vert < m):
			Solution.recursive(self, m, n, hori, vert + 1, moves + 1)
		

	def uniquePaths(self, m, n):
		hori = 0
		vert = 0
		moves = Solution.recursive(self, m, n, hori, vert, int(0))
		print(moves)

obj = Solution()
obj.uniquePaths(int(2), int(2))
