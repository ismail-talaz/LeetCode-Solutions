class Solution:

    def bfs(self,grid,src,visited):
        queue=[src]

        while queue:
            src=queue.pop(0)
            y,x=src
            if src not in visited:   
                visited.add(src)
            else:
                continue

            if y!=0 and grid[y-1][x]!="0":queue.append((y-1,x))
            if y!=len(grid)-1 and grid[y+1][x]!="0":queue.append((y+1,x))
            if x!=0 and grid[y][x-1]!="0":queue.append((y,x-1))
            if x!=len(grid[0])-1 and grid[y][x+1]!="0":queue.append((y,x+1))

        return visited

    def numIslands(self,grid) -> int:

        count=0
        visited=set()

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                src=(y,x)
                if src not in visited and grid[y][x]!="0":
                    count+=1
                    visited=self.bfs(grid,src,visited)
            
        return count
