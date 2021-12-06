import random, math
import numpy as np
import matplotlib.pyplot as plt 
from math import log10


random.seed(5)

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
    for i in range(len(l) - 1, -1, -1):
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
    def __init__(self, x, y, direction, lane_no, init_speed, id):
        self.x = x
        self.y = y
        self.direction = direction
        self.lane_no = lane_no
        self.speed = init_speed
        self.id = id

        self.queue = []
        self.coor = []

        next_idx = find_next_crosslane(self.x, self.y, self.direction)
        # next_dir, next_lane_no = None, None

        # enter the 1st element of queue
        if self.direction == "left" or self.direction == "right":
            self.queue.append((lane_x_coor[next_idx], self.y))
        elif self.direction == "up" or self.direction == "down":
            self.queue.append((self.x, lane_y_coor[next_idx]))
        else:
            return "Error message"

    def _decide_next_lane_dir(self, paths):
        # while True:
        #     r1, r2 = random.random(), random.random() 
        #     if r1 < 0.25:  # right
        #         if "right" in paths:
        #             next_dir = "right"
        #             next_lane_no = paths["right"][0] if r2 < 0.5 else paths["right"][1]
        #             break
        #     elif r1 < 0.5:
        #         if "left" in paths:
        #             next_dir = "left"
        #             next_lane_no = paths["left"][0] if r2 < 0.5 else paths["left"][1]
        #             break
        #     elif r1 < 0.75:
        #         if "up" in paths:
        #             next_dir = "up"
        #             next_lane_no = paths["up"][0] if r2 < 0.5 else paths["up"][1]
        #             break
        #     else:
        #         if "down" in paths:
        #             next_dir = "down"
        #             next_lane_no = paths["down"][0] if r2 < 0.5 else paths["down"][1]
        #             break

        next_dir = random.choice(list(paths.keys()))
        next_lane_no = random.choice(paths[next_dir])

        return next_dir, next_lane_no

    def decide_next_lane(self, i):
        # i -> next crosslane index perpendicular to the current direction
        print("\n\nEntered a crossroad...")
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

        print("Paths: ", paths)
        print("Next Lane deciding....")
        to_return = self._decide_next_lane_dir(paths)
        print(to_return)
        return to_return

    def set_new_direction_lane(self, next_point):
        #  given current point and next point, modify self.direction and self.lane_no
        print("Current point: ", self.x, self.y)
        print("Next point: ", next_point)

        assert bool(self.x == next_point[0]) ^ bool(
            self.y == next_point[1]
        )  # performing xor
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

    def move(self, interval):
        # # step = speed * interval
        # # print("step = ", step)
        # coor = list()
        # t = 0
        # queue = []  # list of the points to be visited

        # next_idx = find_next_crosslane(self.x, self.y, self.direction)
        # next_dir, next_lane_no = None, None
        #
        # # enter the 1st element of queue
        # if self.direction == "left" or self.direction == "right":
        #     queue.append((lane_x_coor[next_idx], self.y))
        # elif self.direction == "up" or self.direction == "down":
        #     queue.append((self.x, lane_y_coor[next_idx]))
        # else:
        #     return "Error message"

        # print("Queue: ", queue)
        # t = 0
        # while t <= time:

        if self.direction in "right":
            self.x += self.speed * interval

            if self.x >= self.queue[0][0]:  # crossing an intersection
                self.x = self.queue[0][0]
                curr_pos = self.queue.pop(0)  # current intersection coordinates

                if len(self.queue) == 0:  # signifies entering a crossroad
                    # add to self.queue the points to visit in the current crossroad and first intersection in the next crossroad

                    next_dir, next_lane_no = self.decide_next_lane(
                        lane_x_coor.index(self.x)
                    )

                    if next_dir == "left":
                        n_y = lane_y_coor[next_lane_no]
                        self.queue.append((self.x, n_y))
                        # next crossroad
                        n_x = lane_x_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "right":
                        n_y = lane_y_coor[next_lane_no]
                        if self.lane_no != next_lane_no:
                            self.queue.append((self.x, n_y))
                        n_x = lane_x_coor[lane_x_coor.index(self.x) + 3]
                        self.queue.append((n_x, n_y))
                        # next crossroad
                        # nn_x = lane_x_coor[lane_x_coor.index(self.x) + 4]
                        # self.queue.append((nn_x, n_y))
                        n_x = lane_x_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "up":
                        n_x = lane_x_coor[next_lane_no]
                        n_y = self.y
                        if (n_x, n_y) != curr_pos:
                            self.queue.append((n_x, n_y))
                        if (self.lane_no + 1) in horizontal["right"]:
                            n_y = lane_y_coor[self.lane_no + 1]
                            self.queue.append((n_x, n_y))
                        # next crossroad
                        if len(self.queue):
                            n_y = lane_y_coor[
                                find_next_crosslane(
                                    self.queue[-1][0], self.queue[-1][1], next_dir
                                )
                            ]
                        else:
                            n_y = lane_y_coor[
                                find_next_crosslane(self.x, self.y, next_dir)
                            ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "down":
                        n_x = lane_x_coor[next_lane_no]
                        n_y = self.y
                        self.queue.append((n_x, n_y))
                        if (self.lane_no - 1) in horizontal["right"]:
                            n_y = lane_y_coor[self.lane_no - 3]
                            self.queue.append((n_x, n_y))
                        else:
                            n_y = lane_y_coor[self.lane_no - 2]
                            self.queue.append((n_x, n_y))
                        # next crossroad
                        n_y = lane_y_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))
                    else:
                        pass

                print("Queue : ", self.queue)
                next_point = self.queue[0]
                self.set_new_direction_lane(next_point)

        elif self.direction in "left":
            self.x -= self.speed * interval

            if self.x <= self.queue[0][0]:  # crossing an intersection
                self.x = self.queue[0][0]
                curr_pos = self.queue.pop(
                    0
                )  # current position i.e. intersection coordinates

                if len(self.queue) == 0:  # signifies entering a crossroad
                    # add to queue the points to visit in the current crossroad and first intersection in the next crossroad

                    next_dir, next_lane_no = self.decide_next_lane(
                        lane_x_coor.index(self.x)
                    )

                    if next_dir == "right":
                        n_y = lane_y_coor[next_lane_no]
                        self.queue.append((self.x, n_y))
                        # next crossroad
                        n_x = lane_x_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "left":
                        n_y = lane_y_coor[next_lane_no]
                        if self.lane_no != next_lane_no:
                            self.queue.append((self.x, n_y))
                        n_x = lane_x_coor[lane_x_coor.index(self.x) - 3]
                        self.queue.append((n_x, n_y))
                        # next crossroad
                        # nn_x = lane_x_coor[lane_x_coor.index(self.x) - 4]
                        # self.queue.append((nn_x, n_y))
                        n_x = lane_x_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "down":
                        n_x = lane_x_coor[next_lane_no]
                        n_y = self.y
                        if (n_x, n_y) != curr_pos:
                            self.queue.append((n_x, n_y))
                        if (self.lane_no - 1) in horizontal["left"]:
                            n_y = lane_y_coor[self.lane_no - 1]
                            self.queue.append((n_x, n_y))
                        # next crossroad
                        if len(self.queue):
                            n_y = lane_y_coor[
                                find_next_crosslane(
                                    self.queue[-1][0], self.queue[-1][1], next_dir
                                )
                            ]
                        else:
                            n_y = lane_y_coor[
                                find_next_crosslane(self.x, self.y, next_dir)
                            ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "up":
                        n_x = lane_x_coor[next_lane_no]
                        n_y = self.y
                        self.queue.append((n_x, n_y))
                        if (self.lane_no + 1) in horizontal["left"]:
                            n_y = lane_y_coor[self.lane_no + 3]
                            self.queue.append((n_x, n_y))
                        else:
                            n_y = lane_y_coor[self.lane_no + 2]
                            self.queue.append((n_x, n_y))
                        # next crossroad
                        n_y = lane_y_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))
                    else:
                        pass

                print("Queue : ", self.queue)
                next_point = self.queue[0]
                self.set_new_direction_lane(next_point)

        elif self.direction in "up":
            self.y += self.speed * interval

            if self.y >= self.queue[0][1]:  # crossing an intersection
                self.y = self.queue[0][1]
                curr_pos = self.queue.pop(
                    0
                )  # current position i.e. intersection coordinates

                if len(self.queue) == 0:  # signifies entering a crossroad
                    # add to queue the points to visit in the current crossroad and first intersection in the next crossroad

                    next_dir, next_lane_no = self.decide_next_lane(
                        lane_y_coor.index(self.y)
                    )

                    if next_dir == "down":
                        n_x = lane_x_coor[next_lane_no]
                        n_y = self.y
                        self.queue.append((n_x, n_y))
                        # next crossroad
                        n_y = lane_y_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "up":
                        n_x = lane_x_coor[next_lane_no]
                        n_y = self.y
                        if self.lane_no != next_lane_no:
                            self.queue.append((n_x, n_y))
                        n_y = lane_y_coor[lane_y_coor.index(self.y) + 3]
                        self.queue.append((n_x, n_y))
                        # next crossroad
                        # nn_x = lane_x_coor[lane_x_coor.index(self.x) + 4]
                        # self.queue.append((nn_x, n_y))
                        n_y = lane_y_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "left":
                        n_y = lane_y_coor[next_lane_no]
                        n_x = self.x
                        if (n_x, n_y) != curr_pos:
                            self.queue.append((n_x, n_y))
                        if (self.lane_no - 1) in vertical["up"]:
                            n_x = lane_x_coor[self.lane_no - 1]
                            self.queue.append((n_x, n_y))
                        # next crossroad
                        if len(self.queue):
                            n_x = lane_x_coor[
                                find_next_crosslane(
                                    self.queue[-1][0], self.queue[-1][1], next_dir
                                )
                            ]
                        else:
                            n_x = lane_x_coor[
                                find_next_crosslane(self.x, self.y, next_dir)
                            ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "right":
                        n_y = lane_y_coor[next_lane_no]
                        n_x = self.x
                        self.queue.append((n_x, n_y))
                        if (self.lane_no - 1) in vertical["up"]:
                            n_x = lane_x_coor[self.lane_no + 2]
                            self.queue.append((n_x, n_y))
                        else:
                            n_x = lane_x_coor[self.lane_no + 3]
                            self.queue.append((n_x, n_y))
                        # next crossroad
                        n_x = lane_x_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))
                    else:
                        pass

                print("Queue : ", self.queue)
                next_point = self.queue[0]
                self.set_new_direction_lane(next_point)

        elif self.direction in "down":
            self.y -= self.speed * interval

            if self.y <= self.queue[0][1]:  # crossing an intersection
                self.y = self.queue[0][1]
                curr_pos = self.queue.pop(0)  # current position i.e. intersection coordinates

                if len(self.queue) == 0:  # signifies entering a crossroad
                    # add to queue the points to visit in the current crossroad and first intersection in the next crossroad

                    next_dir, next_lane_no = self.decide_next_lane(
                        lane_y_coor.index(self.y)
                    )

                    if next_dir == "up":
                        n_x = lane_x_coor[next_lane_no]
                        n_y = self.y
                        self.queue.append((n_x, n_y))
                        # next crossroad
                        n_y = lane_y_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "down":
                        n_x = lane_x_coor[next_lane_no]
                        n_y = self.y
                        if self.lane_no != next_lane_no:
                            self.queue.append((n_x, n_y))
                        n_y = lane_y_coor[lane_y_coor.index(self.y) - 3]
                        self.queue.append((n_x, n_y))
                        # next crossroad
                        # nn_x = lane_x_coor[lane_x_coor.index(self.x) + 4]
                        # self.queue.append((nn_x, n_y))
                        n_y = lane_y_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "right":
                        n_y = lane_y_coor[next_lane_no]
                        n_x = self.x
                        if (n_x, n_y) != curr_pos:
                            self.queue.append((n_x, n_y))
                        if (self.lane_no + 1) in vertical["down"]:
                            n_x = lane_x_coor[self.lane_no + 1]
                            self.queue.append((n_x, n_y))
                        # next crossroad
                        if len(self.queue):
                            n_x = lane_x_coor[
                                find_next_crosslane(
                                    self.queue[-1][0], self.queue[-1][1], next_dir
                                )
                            ]
                        else:
                            n_x = lane_x_coor[
                                find_next_crosslane(self.x, self.y, next_dir)
                            ]
                        self.queue.append((n_x, n_y))

                    elif next_dir == "left":
                        n_y = lane_y_coor[next_lane_no]
                        n_x = self.x
                        self.queue.append((n_x, n_y))
                        if (self.lane_no + 1) in vertical["down"]:
                            n_x = lane_x_coor[self.lane_no - 2]
                            self.queue.append((n_x, n_y))
                        else:
                            n_x = lane_x_coor[self.lane_no - 3]
                            self.queue.append((n_x, n_y))
                        # next crossroad
                        n_x = lane_x_coor[
                            find_next_crosslane(
                                self.queue[-1][0], self.queue[-1][1], next_dir
                            )
                        ]
                        self.queue.append((n_x, n_y))
                    else:
                        pass

                print("Queue : ", self.queue)
                next_point = self.queue[0]
                self.set_new_direction_lane(next_point)

        else:
            print("XXXXXXXXXXXXXX")
            return

        self.coor.append((self.x, self.y))
        # t += interval

        # return coor


def find_pairs(vehicles, max_sep):
    # vehicles -> list of Vehicle objects
    # max_sep -> maximum separation between 2 vehicles to form a pair
    n = len(vehicles)
    pairs = []
    v1, v2 = None, None
    for i in range(n):
        for j in range(i + 1, n):
            v1, v2 = vehicles[i], vehicles[j]
            if (v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2 <= max_sep ** 2:
                pairs.append((v1.id, v2.id))
    return pairs


def in_same_lane(v1, v2):
    return v1.lane_no == v2.lane_no and v1.direction == v2.direction


def is_LOS(vehicles, v1, v2):
    assert in_same_lane(v1, v2)
    for v in vehicles:
        if not in_same_lane(v, v1):
            continue
        if v1.direction == "left" or v1.direction == "right":
            if (v.x - v1.x) * (v.x - v2.x) < 0:  # v is in between v1 and v2
                return False
        else:
            if (v.y - v1.y) * (v.y - v2.y) < 0:
                return False
    return True


def calculate_PL_shadow(n, vehicles, D, PL, S, N_S, fc, d_corr, sigmaLOS, sigmaNLOS):
    # n = len(vehicles)
    # PT = np.ones((n, n))
    # PL = np.ones((n, n))

    for i in range(n):
        for j in range(i + 1, n):
        
            if in_same_lane(vehicles[i], vehicles[j]):
                # if is_LOS(vehicles, vehicles[i], vehicles[j]):
                PL[i][j] = 38.77 + 16.7*log10(D[i][j]) + 18.2*log10(fc)
                N_S[i][j] = np.random.normal(0, sigmaLOS)
            else:
                PL[i][j] = 36.85 + 30*log10(D[i][j]) + 18.9*log10(fc)
                N_S[i][j] = np.random.normal(0, sigmaNLOS)

            # PL[j][i] = PL[i][j]
            # N_S[j][i] = N_S[i][j]

    # print(N_S)
    # print("************************************")
    S = math.e**(-D/d_corr) * S + (1 - math.e**(-2*D/d_corr))**0.5 * N_S
    # print(S)

    # PR = PT / 10**(PL/10)
    return S

def apply_rayleigh(Pr, N):
    for i in range(N):
        for j in range(i+1, N):
            Pr_lin_ij = 10**(Pr[i][j]/10)
            Pr[i][j] = 10*log10(np.random.exponential(1)*Pr_lin_ij)
            # Pr[j][i] = Pr[i][j]
    return


def main():
    x, y = 240, lane_y_coor[4]
    d = "right"
    l = 4
    speed = 20

    vehicles = []

    vehicles.append(Vehicle(x, y, d, l, speed, 1))
    vehicles.append(Vehicle(x - 5, y, d, l, speed, 2))
    # vehicles.append(Vehicle(x - 10, y, d, l, speed, 3))
    # vehicles.append(Vehicle(x - 15, y, d, l, speed, 4))
    # vehicles.append(Vehicle(x - 20, y, d, l, speed, 5))
    # vehicles.append(Vehicle(x - 25, y, d, l, speed, 6))

    N = len(vehicles)
    time, interval = 15, 0.1
    assert speed * interval < 3.5

    # print(v.move(time, interval))

    # pairs_over_time = []  # list of lists of tuples
    # pairs = []  # lists of tuples

    Pt = np.full((N, N), 20)        #20dB tramsmit power, 100 in linear
    D = np.zeros((N, N))
    PL, S, N_S = np.zeros((N, N)), np.zeros((N, N)), np.zeros((N, N))

    PL_array = []
    D_array = []
    Pr_array = []

    t = 0

    while t <= time:
        print(f'At time = {t} ms: ')
        for v in vehicles:
            v.move(interval)

        # pairs = find_pairs(vehicles, 10)
        # pairs_over_time.append(pairs)

        for i in range(N):
            for j in range(i+1, N):
                D[i][j] = ((vehicles[i].x - vehicles[j].x)**2 + (vehicles[i].y - vehicles[j].y)**2)**0.5
                # D[j][i] = D[i][j]
        
        S = calculate_PL_shadow(N, vehicles, D, PL, S, N_S, fc=30, d_corr=10, sigmaLOS=3, sigmaNLOS=4)
        # print(D)
        # print(PL)
        # print(N_S)
        # print(S)

        Pr = Pt - PL - S
        apply_rayleigh(Pr, N)
        # print(Pr)

        t += interval

        print("**************************************************")
        D_array.append(D[0][1])
        PL_array.append(PL[0][1])
        Pr_array.append(Pr[0][1])
        
    
    # plt.plot(D_array)
    plt.plot(PL_array)
    plt.plot(Pr_array)
    plt.show()
    
    # for v in vehicles:
    #     print(v.coor, "\n\n")
    #     pass

    # for l in pairs_over_time:
    #     print(l)
  

if __name__ == "__main__":
    main()