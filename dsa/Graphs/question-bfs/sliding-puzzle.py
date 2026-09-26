
# https://leetcode.com/problems/sliding-puzzle/
class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start = ""
        for row in board:
            for num in row:
                start+=str(num)
            
        target = "123450"

        queue = deque()

        queue.append((start,0))

        visited = set()

        directions=[
            [1,3],##0 Idx
            [0,2,4],## 1Idx
            [1,5],## 2Idx
            [0,4],## 3Idx
            [1,3,5],## 4Idx
            [2,4],## 5Idx
        ]

        # REMOVE-->MARK*--->WORK--->ADD*

        while queue:
            config,moves = queue.popleft()

            if config in visited:
                continue
            visited.add(config)

            if config == target:
                return moves

            zeroIdx = config.index('0')


            for newIdx in directions[zeroIdx]:
                newConfig = list(config)
                
                temp = newConfig[zeroIdx]
                newConfig[zeroIdx] = newConfig[newIdx]
                newConfig[newIdx]=temp

                new_config = "".join(newConfig)
                if new_config not in visited:
                    queue.append((new_config,moves+1))

        return -1

    
