class Solution(object):
	def numIslands(self, grid):
		self.grid = grid
		#grid = [[int(letter) for letter in x] for x in grid]
		grid = [list(map(int, x)) for x in grid]
		islands = 0
		for count1, value in enumerate(grid):
			for count2, y in enumerate(value):
				if (int(y) == 1):
					if (count2 != 0):
						if (value[count2 - 1] == 1):
							print("stop found 1 before")
							continue
					if (count2 != 4):
						if (value[count2 + 1] == 1):
							print("stop found 1 after")
							continue
					if(count1 != 0):
						if (grid[count1 - 1][count2] == 1):
							print("found above horizontal")
							continue
					if(count1 != 3):
						if (grid[count1 + 1][count2] == 1):
							print("found belowhorizontal")
							continue
					islands = islands + 1
		print(islands)

grid = [
  ["1","0","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
obj = Solution()
obj.numIslands(grid)
