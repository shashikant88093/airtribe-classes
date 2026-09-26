# https://leetcode.com/problems/course-schedule/description/

from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build the adjacency list and an in-degree array
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        # Queue stores all courses with no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        courses_taken = 0
        
        # Process the queue
        while queue:
            node = queue.popleft()
            courses_taken += 1
            
            # Reduce the in-degree of neighbors
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, we can now take this course
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If we were able to take all courses, return True
        return courses_taken == numCourses
