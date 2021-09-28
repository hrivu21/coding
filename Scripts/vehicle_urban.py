import random

# random.seed(2)

horizontal = {"right": (0, 1, 4, 5, 8, 9), "left": (2, 3, 6, 7, 10, 11)}

lane_y_coor = [
    1.75,
    5.25,
    427.75,
    431.25,
    434.75,
    438.25,
    860.75,
    864.25,
    867.75,
    871.25,
    1293.75,
    1297.25,
]

vertical = {"down": (0, 1, 4, 5, 8, 9), "up": (2, 3, 6, 7, 10, 11)}

lane_x_coor = [
    1.75,
    5.25,
    244.75,
    248.25,
    251.75,
    255.25,
    494.75,
    498.25,
    501.75,
    505.25,
    744.75,
    748.25,
]


def find_greater(l, value):  # l assumed to be sorted
    for i, x in enumerate(l):
        if x > value:
            return i
    return -1


def find_lesser(l, value):  # l assumed to be sorted
    for i in range(len(l)-1, -1, -1):
        if l[i] < value:
            return i
    return -1


def find_next_crosslane(x, y, direction):
    next_idx = None

    if direction == "right":
        next_idx = find_greater(lane_x_coor, x)

    elif direction == "left":
        next_idx = find_lesser(lane_x_coor, x)

    elif direction == "up":
        next_idx = find_greater(lane_y_coor, y)

    elif direction == "down":
        next_idx = find_lesser(lane_y_coor, y)

    assert next_idx > -1
    return next_idx


class Vehicle:
    def __init__(self, x, y, direction, lane_no):
        self.x = x
        self.y = y
        self.direction = direction
        self.lane_no = lane_no

    def _decide_next_lane_dir(self, paths):
        while True:
            r1, r2 = random.random(), random.random()
            if r1 < 0.25:  # right
                if "right" in paths:
                    next_dir = "right"
                    next_lane_no = paths["right"][0] if r2 < 0.5 else paths["right"][1]
                    break
            elif r1 < 0.5:
                if "left" in paths:
                    next_dir = "left"
                    next_lane_no = paths["left"][0] if r2 < 0.5 else paths["left"][1]
                    break
            elif r1 < 0.75:
                if "up" in paths:
                    next_dir = "up"
                    next_lane_no = paths["up"][0] if r2 < 0.5 else paths["up"][1]
                    break
            else:
                if "down" in paths:
                    next_dir = "down"
                    next_lane_no = paths["down"][0] if r2 < 0.5 else paths["down"][1]
                    break

        return next_dir, next_lane_no

    def decide_next_lane(self, i):  # i -> next crosslane index perpendicular to the current direction
        print('\n\nEntered a crossroad...')
        print((self.direction, self.lane_no))
        paths = dict()  # allowed lane changes at crossroads

        if self.direction == "right":
            assert self.lane_no in horizontal["right"]
            paths["up"] = [i, i + 1]

            # if i + 2 in vertical["down"] and i + 3 in vertical["down"]:
            if i < len(lane_x_coor) - 2:
                if self.lane_no + 1 in horizontal["right"]:
                    paths["right"] = [self.lane_no, self.lane_no + 1]
                else:
                    # assert(self.lane_no - 1 in horizontal['right'])
                    paths["right"] = [self.lane_no - 1, self.lane_no]

            if self.lane_no >= 2:
                if i + 2 in vertical["down"] and i + 3 in vertical["down"]:
                    paths["down"] = [i + 2, i + 3]

                if self.lane_no - 1 in horizontal["left"]:
                    # assert(self.lane_no + 2 in horizontal['left'] and self.lane_no + 3 in horizontal['left'])
                    paths["left"] = [self.lane_no - 1, self.lane_no - 2]
                else:
                    # assert(self.lane_no + 1 in horizontal['left'] and self.lane_no + 2 in horizontal['left'])
                    paths["left"] = [self.lane_no - 2, self.lane_no - 3]

        ##########################################################################################################
        elif self.direction == "left":
            assert self.lane_no in horizontal["left"]
            paths["down"] = [i, i - 1]

            # if i - 2 in vertical["up"] and i - 3 in vertical["up"]:
            if i >= 2:
                if self.lane_no + 1 in horizontal["left"]:
                    paths["left"] = [self.lane_no, self.lane_no + 1]
                else:
                    # assert(self.lane_no - 1 in horizontal['left'])
                    paths["left"] = [self.lane_no - 1, self.lane_no]

            if self.lane_no < len(lane_y_coor) - 2:
                if i - 2 in vertical["up"] and i - 3 in vertical["up"]:
                    paths["up"] = [i - 2, i - 3]

                if self.lane_no + 1 in horizontal["right"]:
                    # assert(self.lane_no + 2 in horizontal['left'] and self.lane_no + 3 in horizontal['left'])
                    paths["right"] = [self.lane_no + 1, self.lane_no + 1]
                else:
                    # assert(self.lane_no + 1 in horizontal['left'] and self.lane_no + 2 in horizontal['left'])
                    paths["right"] = [self.lane_no + 2, self.lane_no + 3]

        ############################################################################################################
        elif self.direction == "up":
            paths["left"] = [i, i + 1]

            if i + 2 in horizontal["right"] and i + 3 in horizontal["right"]:
                if self.lane_no + 1 in vertical["up"]:
                    paths["up"] = [self.lane_no, self.lane_no + 1]
                else:
                    # assert(self.lane_no - 1 in vertical['up'])
                    paths["up"] = [self.lane_no - 1, self.lane_no]

            if self.lane_no < len(lane_x_coor) - 2:
                if i + 2 in horizontal["right"] and i + 3 in horizontal["right"]:
                    paths["right"] = [i + 2, i + 3]

                if self.lane_no + 1 in vertical["down"]:
                    # assert(self.lane_no + 2 in vertical['left'] and self.lane_no + 3 in horizontal['left'])
                    paths["down"] = [self.lane_no + 1, self.lane_no + 2]
                else:
                    # assert(self.lane_no + 1 in vertical['left'] and self.lane_no + 2 in horizontal['left'])
                    paths["down"] = [self.lane_no + 2, self.lane_no + 3]

        ##########################################################################################################
        elif self.direction == "down":
            paths["right"] = [i, i - 1]

            if i - 2 in horizontal["left"] and i - 3 in horizontal["left"]:
                if self.lane_no + 1 in vertical["down"]:
                    paths["down"] = [self.lane_no, self.lane_no + 1]
                else:
                    # assert(self.lane_no - 1 in vertical['down'])
                    paths["down"] = [self.lane_no - 1, self.lane_no]

            if self.lane_no > 1:
                if i - 2 in horizontal["left"] and i - 3 in horizontal["left"]:
                    paths["left"] = [i - 2, i - 3]

                if self.lane_no - 1 in vertical["up"]:
                    # assert(self.lane_no + 2 in vertical['left'] and self.lane_no + 3 in horizontal['left'])
                    paths["up"] = [self.lane_no - 1, self.lane_no - 2]
                else:
                    # assert(self.lane_no + 1 in vertical['left'] and self.lane_no + 2 in horizontal['left'])
                    paths["up"] = [self.lane_no - 2, self.lane_no - 3]

        print('Paths: ', paths)
        print("Next Lane deciding....")
        to_return = self._decide_next_lane_dir(paths)
        print(to_return)
        return to_return

    def set_new_direction_lane(self, next_point):
        #  given current point and next point, modify self.direction and self.lane_no
        print("Current point: ", self.x, self.y)
        print("Next point: ", next_point)

        assert bool(self.x == next_point[0]) ^ bool(self.y == next_point[1])       # performing xor
        if self.x == next_point[0]:  # move up/down
            self.lane_no = lane_x_coor.index(self.x)
            if next_point[1] > self.y:
                self.direction = "up"
            else:
                self.direction = "down"
        elif self.y == next_point[1]:  # move left/right
            self.lane_no = lane_y_coor.index(self.y)
            if next_point[0] > self.x:
                self.direction = "right"
            else:
                self.direction = "left"

        print("New direction and lane: ", self.direction, self.lane_no)
        return None

    def move(self, speed, time, interval):
        step = speed * interval
        print("step = ", step)
        coor = list()
        t = 0
        queue = []  # list of the points to be visited

        next_idx = find_next_crosslane(self.x, self.y, self.direction)
        next_dir, next_lane_no = None, None

        # enter the 1st element of queue
        if self.direction == "left" or self.direction == "right":
            queue.append((lane_x_coor[next_idx], self.y))
        elif self.direction == "up" or self.direction == "down":
            queue.append((self.x, lane_y_coor[next_idx]))
        else:
            return "Error message"

        print("Queue: ", queue)
        t = 0
        while t <= time:
            if self.direction in "right":
                self.x += step

                if self.x >= queue[0][0]:       # crossing an intersection
                    self.x = queue[0][0]
                    curr_pos = queue.pop(0)     # current intersection coordinates

                    if len(queue) == 0:  # signifies entering a crossroad
                        # add to queue the points to visit in the current crossroad and first intersection in the next crossroad

                        next_dir, next_lane_no = self.decide_next_lane(lane_x_coor.index(self.x))

                        if next_dir == "left":
                            n_y = lane_y_coor[next_lane_no]
                            queue.append((self.x, n_y))
                            # next crossroad
                            n_x = lane_x_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))

                        elif next_dir == "right":
                            n_y = lane_y_coor[next_lane_no]
                            if self.lane_no != next_lane_no:
                                queue.append((self.x, n_y))
                            n_x = lane_x_coor[lane_x_coor.index(self.x) + 3]
                            queue.append((n_x, n_y))
                            # next crossroad
                            # nn_x = lane_x_coor[lane_x_coor.index(self.x) + 4]
                            # queue.append((nn_x, n_y))
                            n_x = lane_x_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))

                        elif next_dir == "up":
                            n_x = lane_x_coor[next_lane_no]
                            n_y = self.y
                            if (n_x, n_y) != curr_pos:
                                queue.append((n_x, n_y))
                            if (self.lane_no + 1) in horizontal["right"]:
                                n_y = lane_y_coor[self.lane_no + 1]
                                queue.append((n_x, n_y))
                            # next crossroad
                            if len(queue):
                                n_y = lane_y_coor[
                                    find_next_crosslane(
                                        queue[-1][0], queue[-1][1], next_dir
                                    )
                                ]
                            else:
                                n_y = lane_y_coor[
                                    find_next_crosslane(
                                        self.x, self.y, next_dir
                                    )
                                ]
                            queue.append((n_x, n_y))

                        elif next_dir == "down":
                            n_x = lane_x_coor[next_lane_no]
                            n_y = self.y
                            queue.append((n_x, n_y))
                            if (self.lane_no - 1) in horizontal["right"]:
                                n_y = lane_y_coor[self.lane_no - 3]
                                queue.append((n_x, n_y))
                            else:
                                n_y = lane_y_coor[self.lane_no - 2]
                                queue.append((n_x, n_y))
                            # next crossroad
                            n_y = lane_y_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))
                        else:
                            pass

                    print('Queue : ', queue)
                    next_point = queue[0]
                    self.set_new_direction_lane(next_point)

            elif self.direction in "left":
                self.x -= step

                if self.x <= queue[0][0]:  # crossing an intersection
                    self.x = queue[0][0]
                    curr_pos = queue.pop(
                        0
                    )  # current position i.e. intersection coordinates

                    if len(queue) == 0:  # signifies entering a crossroad
                        # add to queue the points to visit in the current crossroad and first intersection in the next crossroad

                        next_dir, next_lane_no = self.decide_next_lane(lane_x_coor.index(self.x))

                        if next_dir == "right":
                            n_y = lane_y_coor[next_lane_no]
                            queue.append((self.x, n_y))
                            # next crossroad
                            n_x = lane_x_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))

                        elif next_dir == "left":
                            n_y = lane_y_coor[next_lane_no]
                            if self.lane_no != next_lane_no:
                                queue.append((self.x, n_y))
                            n_x = lane_x_coor[lane_x_coor.index(self.x) - 3]
                            queue.append((n_x, n_y))
                            # next crossroad
                            # nn_x = lane_x_coor[lane_x_coor.index(self.x) - 4]
                            # queue.append((nn_x, n_y))
                            n_x = lane_x_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))

                        elif next_dir == "down":
                            n_x = lane_x_coor[next_lane_no]
                            n_y = self.y
                            if (n_x, n_y) != curr_pos:
                                queue.append((n_x, n_y))
                            if (self.lane_no - 1) in horizontal["left"]:
                                n_y = lane_y_coor[self.lane_no - 1]
                                queue.append((n_x, n_y))
                            # next crossroad
                            if len(queue):
                                n_y = lane_y_coor[
                                    find_next_crosslane(
                                        queue[-1][0], queue[-1][1], next_dir
                                    )
                                ]
                            else:
                                n_y = lane_y_coor[
                                    find_next_crosslane(
                                        self.x, self.y, next_dir
                                    )
                                ]
                            queue.append((n_x, n_y))

                        elif next_dir == "up":
                            n_x = lane_x_coor[next_lane_no]
                            n_y = self.y
                            queue.append((n_x, n_y))
                            if (self.lane_no + 1) in horizontal["left"]:
                                n_y = lane_y_coor[self.lane_no + 3]
                                queue.append((n_x, n_y))
                            else:
                                n_y = lane_y_coor[self.lane_no + 2]
                                queue.append((n_x, n_y))
                            # next crossroad
                            n_y = lane_y_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))
                        else:
                            pass

                    print('Queue : ', queue)
                    next_point = queue[0]
                    self.set_new_direction_lane(next_point)

            elif self.direction in "up":
                self.y += step

                if self.y >= queue[0][1]:  # crossing an intersection
                    self.y = queue[0][1]
                    curr_pos = queue.pop(
                        0
                    )  # current position i.e. intersection coordinates

                    if len(queue) == 0:  # signifies entering a crossroad
                        # add to queue the points to visit in the current crossroad and first intersection in the next crossroad

                        next_dir, next_lane_no = self.decide_next_lane(lane_y_coor.index(self.y))

                        if next_dir == "down":
                            n_x = lane_x_coor[next_lane_no]
                            n_y = self.y
                            queue.append((n_x, n_y))
                            # next crossroad
                            n_y = lane_y_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))

                        elif next_dir == "up":
                            n_x = lane_x_coor[next_lane_no]
                            n_y = self.y
                            if self.lane_no != next_lane_no:
                                queue.append((n_x, n_y))
                            n_y = lane_y_coor[lane_y_coor.index(self.y) + 3]
                            queue.append((n_x, n_y))
                            # next crossroad
                            # nn_x = lane_x_coor[lane_x_coor.index(self.x) + 4]
                            # queue.append((nn_x, n_y))
                            n_y = lane_y_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))

                        elif next_dir == "left":
                            n_y = lane_y_coor[next_lane_no]
                            n_x = self.x
                            if (n_x, n_y) != curr_pos:
                                queue.append((n_x, n_y))
                            if (self.lane_no - 1) in vertical["up"]:
                                n_x = lane_x_coor[self.lane_no - 1]
                                queue.append((n_x, n_y))
                            # next crossroad
                            if len(queue):
                                n_x = lane_x_coor[
                                    find_next_crosslane(
                                        queue[-1][0], queue[-1][1], next_dir
                                    )
                                ]
                            else:
                                n_x = lane_x_coor[
                                    find_next_crosslane(
                                        self.x, self.y, next_dir
                                    )
                                ]
                            queue.append((n_x, n_y))

                        elif next_dir == "right":
                            n_y = lane_y_coor[next_lane_no]
                            n_x = self.x
                            queue.append((n_x, n_y))
                            if (self.lane_no - 1) in vertical["up"]:
                                n_x = lane_x_coor[self.lane_no + 2]
                                queue.append((n_x, n_y))
                            else:
                                n_x = lane_x_coor[self.lane_no + 3]
                                queue.append((n_x, n_y))
                            # next crossroad
                            n_x = lane_x_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))
                        else:
                            pass

                    print('Queue : ', queue)
                    next_point = queue[0]
                    self.set_new_direction_lane(next_point)

            elif self.direction in "down":
                self.y -= step

                if self.y <= queue[0][1]:  # crossing an intersection
                    self.y = queue[0][1]
                    curr_pos = queue.pop(
                        0
                    )  # current position i.e. intersection coordinates

                    if len(queue) == 0:  # signifies entering a crossroad
                        # add to queue the points to visit in the current crossroad and first intersection in the next crossroad

                        next_dir, next_lane_no = self.decide_next_lane(lane_y_coor.index(self.y))

                        if next_dir == "up":
                            n_x = lane_x_coor[next_lane_no]
                            n_y = self.y
                            queue.append((n_x, n_y))
                            # next crossroad
                            n_y = lane_y_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))

                        elif next_dir == "down":
                            n_x = lane_x_coor[next_lane_no]
                            n_y = self.y
                            if self.lane_no != next_lane_no:
                                queue.append((n_x, n_y))
                            n_y = lane_y_coor[lane_y_coor.index(self.y) - 3]
                            queue.append((n_x, n_y))
                            # next crossroad
                            # nn_x = lane_x_coor[lane_x_coor.index(self.x) + 4]
                            # queue.append((nn_x, n_y))
                            n_y = lane_y_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))

                        elif next_dir == "right":
                            n_y = lane_y_coor[next_lane_no]
                            n_x = self.x
                            if (n_x, n_y) != curr_pos:
                                queue.append((n_x, n_y))
                            if (self.lane_no + 1) in vertical["down"]:
                                n_x = lane_x_coor[self.lane_no + 1]
                                queue.append((n_x, n_y))
                            # next crossroad
                            if len(queue):
                                n_x = lane_x_coor[
                                    find_next_crosslane(
                                        queue[-1][0], queue[-1][1], next_dir
                                    )
                                ]
                            else:
                                n_x = lane_x_coor[
                                    find_next_crosslane(
                                        self.x, self.y, next_dir
                                    )
                                ]
                            queue.append((n_x, n_y))

                        elif next_dir == "left":
                            n_y = lane_y_coor[next_lane_no]
                            n_x = self.x
                            queue.append((n_x, n_y))
                            if (self.lane_no + 1) in vertical["down"]:
                                n_x = lane_x_coor[self.lane_no - 2]
                                queue.append((n_x, n_y))
                            else:
                                n_x = lane_x_coor[self.lane_no - 3]
                                queue.append((n_x, n_y))
                            # next crossroad
                            n_x = lane_x_coor[
                                find_next_crosslane(
                                    queue[-1][0], queue[-1][1], next_dir
                                )
                            ]
                            queue.append((n_x, n_y))
                        else:
                            pass

                    print('Queue : ', queue)
                    next_point = queue[0]
                    self.set_new_direction_lane(next_point)

            else:
                print("XXXXXXXXXXXXXX")
                return

            coor.append((self.x, self.y))
            t += interval

        return coor


if __name__ == "__main__":
    for _ in range(5):
        x, y = 100, lane_y_coor[4]
        d = "right"
        l = 4
        v = Vehicle(x, y, d, l)

        speed, time, interval = 50, 40, 0.05
        assert speed*interval < 3.5
        print(v.move(speed, time, interval))
        print('\n\n\n\n')
