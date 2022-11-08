class Solution():

	def recursive(self, m, n, hori, vert, moves):
		if (vert >= m or hori >= n):
			return
		moves = moves + 1
		Solution.recursive(self, hori + 1, 2)
		Solution.recursive(self, vert + 1, 2)
		

	def uniquePaths(self, m, n):
		hori = 0
		vert = 0
		moves = 0
		Solution.recursive(self, m, n, hori, vert, moves)

obj = Solution()
obj.uniquePaths(int(2), int(2))
