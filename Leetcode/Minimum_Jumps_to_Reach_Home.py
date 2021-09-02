class Solution:

    def minimumJumps(self, forbidden, a, b, x):
        if(x == 0):
            return 0
        if (x in forbidden):
            return -1

        queue = []
        visited = set()
        prevcount, currcount = 0, 0
        currpos = 0
        steps = 0

        queue.insert(0, (0, False))
        # print(queue[0], steps)
        prevcount = 1
        steps += 1

        while(len(queue)):
            pos, isBackwards = queue.pop(-1)
            prevcount -= 1

            # move forward
            nextstep = pos+a
            if nextstep not in forbidden:
                if nextstep == x:
                    return steps

                if nextstep < 10000 and (nextstep, False) not in visited:
                    queue.insert(0, (nextstep, False))
                    visited.add((nextstep, False))
                    # print(queue[0], steps)
                    currcount += 1

            # move backward
            nextstep = pos-b
            if nextstep >= 0 and nextstep not in forbidden:
                if (isBackwards == False) and (nextstep, False) not in visited and (nextstep, False) not in visited:
                    if nextstep == x:
                        return steps

                    queue.insert(0, (nextstep, True))
                    visited.add((nextstep, True))
                    # print(queue[0], steps)
                    currcount += 1

            if prevcount == 0:
                steps += 1
                prevcount = currcount
                currcount = 0

        return -1


forbidden = [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54,
             154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98]
a = 29
b = 98
x = 80

solution = Solution()

print(solution.minimumJumps(forbidden, a, b, x))
