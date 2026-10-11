from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # since positions cant change just need to know if car reaches one before it
        stack = deque()
        sorted_indices = sorted(range(len(position)), key=lambda i: position[i])

        for i in reversed(sorted_indices):
            time = (target - position[i]) / speed[i]
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
