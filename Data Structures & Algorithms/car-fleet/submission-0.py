class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        road = []
        stack = []

        for i in range(len(position)):
            car = (position[i], speed[i])
            road.append(car)

        road.sort(reverse=True)

        for car in road:
            p, s = car
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)