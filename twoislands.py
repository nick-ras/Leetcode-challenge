class Solution(object):
	def numIslands(self, grid):
		self.grid = grid
		#grid = [[int(letter) for letter in x] for x in grid]
		grid = [list(map(int, x)) for x in grid]
		for count1, value in enumerate(grid):
			for count2, y in enumerate(value):
				if (int(y) == 1):
					if (value[count2 + 1] == 0):
						print("horizontal free")
					else:
						print("horizontal not free")

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
obj = Solution()
obj.numIslands(grid)
print(2)
