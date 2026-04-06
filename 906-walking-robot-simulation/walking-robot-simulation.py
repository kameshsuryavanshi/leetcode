class Solution:
    def robotSim(self, commands, obstacles):
        x_co = 0
        y_co = 0
        direction = 0  # 0: North, 1: East, 2: South, 3: West
        max_d_s = 0

        obstacle_set = set((x, y) for x, y in obstacles)

        dir_offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                for _ in range(command):
                    dx, dy = dir_offsets[direction]
                    new_x = x_co + dx
                    new_y = y_co + dy

                    if (new_x, new_y) in obstacle_set:
                        break

                    x_co = new_x
                    y_co = new_y

                    max_d_s = max(max_d_s, x_co * x_co + y_co * y_co)

        return max_d_s