import numpy as np

import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap

from multiprocessing import Pool

import time





def initialize_board(size, density=0.2):

    return np.random.choice([0, 1], size=size, p=[1 - density, density])





def count_neighbors(board, x, y):

    neighbors = [

        (-1, -1), (-1, 0), (-1, 1),

        (0, -1),         (0, 1),

        (1, -1), (1, 0), (1, 1)

    ]

    count = 0

    for dx, dy in neighbors:

        nx, ny = x + dx, y + dy

        if 0 <= nx < board.shape[0] and 0 <= ny < board.shape[1]:

            count += board[nx, ny]

    return count





def process_chunk(args):

    board, x_start, x_end = args

    size_y = board.shape[1]

    new_chunk = np.copy(board[x_start:x_end])



    for x in range(x_start, x_end):

        for y in range(size_y):

            count = count_neighbors(board, x, y)

            if board[x, y] == 1:

                new_chunk[x - x_start, y] = 1 if 2 <= count <= 3 else 0

            else:

                new_chunk[x - x_start, y] = 1 if count == 3 else 0



    return new_chunk





def update_board_parallel_optimized(board, pool):

    size_x = board.shape[0]

    chunk_indices = np.array_split(range(size_x), pool._processes)

    chunk_ranges = [(board, indices[0], indices[-1] + 1) for indices in chunk_indices]

    results = pool.map(process_chunk, chunk_ranges)

    return np.vstack(results)





def update_board_serial(board):

    new_board = np.copy(board)

    size_x, size_y = board.shape

    for x in range(size_x):

        for y in range(size_y):

            count = count_neighbors(board, x, y)

            if board[x, y] == 1:

                new_board[x, y] = 1 if 2 <= count <= 3 else 0

            else:

                new_board[x, y] = 1 if count == 3 else 0

    return new_board





def run_experiment(initial_size=100, increment=100, steps=20, density=0.2, frames_per_size=5):

    serial_times = []

    parallel_times = []

    sizes = []

    cmap = ListedColormap(['white', 'pink'])



    for step in range(steps):

        size = (initial_size + step * increment, initial_size + step * increment)

        sizes.append(size[0])

        board = initialize_board(size, density)



        serial_time_accum = 0

        plt.figure(figsize=(6, 6))

        for frame in range(frames_per_size):

            start_time = time.time()

            board = update_board_serial(board)

            serial_time_accum += time.time() - start_time

            plt.clf()

            plt.imshow(board, cmap=cmap)

            plt.title(f"Liniowe - Klatka {frame + 1}, Rozmiar {size}")

            plt.axis('off')

            plt.pause(0.1)

        avg_serial_time = serial_time_accum / frames_per_size

        serial_times.append(avg_serial_time)

        plt.close()



        board = initialize_board(size, density)

        parallel_time_accum = 0

        with Pool(processes=8) as pool:

            plt.figure(figsize=(6, 6))

            for frame in range(frames_per_size):

                start_time = time.time()

                board = update_board_parallel_optimized(board, pool)

                parallel_time_accum += time.time() - start_time

                plt.clf()

                plt.imshow(board, cmap=cmap)

                plt.title(f"Rownolegly - Klatka {frame + 1}, Rozmiar {size}")

                plt.axis('off')

                plt.pause(0.1)

            plt.close()

        avg_parallel_time = parallel_time_accum / frames_per_size

        parallel_times.append(avg_parallel_time)

        print(f"{step + 1}/{steps}: Rozmiar={size}, Liniowe Sredni czas={avg_serial_time:.4f}s, Rownolegle Sredni czas={avg_parallel_time:.4f}s")



    return sizes, serial_times, parallel_times





def plot_results(sizes, serial_times, parallel_times):

    plt.figure(figsize=(10, 6))

    plt.plot(sizes, serial_times, label="Liniowe", marker='o')

    plt.plot(sizes, parallel_times, label="Rownolegle", marker='o')

    plt.title("Porownanie czasu Liniowe x Rownolegle‚e")

    plt.xlabel("Rozmiar planszy (N x N)")

    plt.ylabel("Sredni czas obliczen (sekundy)")

    plt.legend()

    plt.grid(True)

    plt.show()



if __name__ == "__main__":
    sizes, serial_times, parallel_times, parallel_core_timings = run_experiment(
        initial_size=10, increment=10, steps=5, frames_per_size=10
    )

    plot_results(sizes, serial_times, parallel_times)

    # Print timing details for parallel cores
    for i, timings in enumerate(parallel_core_timings):
        print(f"Step {i + 1}: Core Timings = {timings}")
