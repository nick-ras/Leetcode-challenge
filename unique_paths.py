# git add .\unique_paths.py ; git commit -m "h" ; git push
class Solution():

	def recursive(self, m, n, hori, vert, moves):
		moves + 1
		if (vert >= m or hori >= n):
			print(f"if {moves}")
			return int(moves)
		moves = 1 + Solution.recursive(self, m, n, hori + 1, vert, moves + 1) + Solution.recursive(self, m, n, hori, vert + 1, moves + 1)
		

	def uniquePaths(self, m, n):
		hori = 1
		vert = 1
		res = Solution.recursive(self, m, n, hori, vert, int(0))
		print(f"end   {res}")

obj = Solution()
obj.uniquePaths(int(3), int(7))
