import numpy as np

colors = {
    'BG': (0, 16, 17),
    'BLUE': (255, 230, 232),
    'VIOLET': (63, 48, 71),
}

NB_STATE = 2
color_ids = {
    1: 'BLUE',
    2: 'VIOLET',
}

CELL_WIDTH = 20
SPEED = 0.02
ALIVE = 1
DEAD = 0

kernel_3x3 = np.ones((3, 3), dtype=bool)
kernel_3x3[1, 1] = False
