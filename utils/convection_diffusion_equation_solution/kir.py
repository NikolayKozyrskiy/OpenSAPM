import numpy as np
"""Use numpy arrays and lists"""

def kir(x_nods_quantity, grid, transfer_velocity, time_step, x_step):
    sigma = transfer_velocity * time_step / x_step
    new_grid = np.zeros(grid.shape)
    for m in range(1, x_nods_quantity - 1):
        if (transfer_velocity >= 0):
            new_grid[m] = grid[m] - sigma * (grid[m] - grid[m-1])
        else:
            new_grid[m] = grid[m] - sigma * (grid[m+1] - grid[m])
    return new_grid[1:-1]
