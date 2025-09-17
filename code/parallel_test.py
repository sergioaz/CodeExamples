import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def weight_squared(weight):
    """CPU-bound operation - squaring a number"""
    return weight ** 2

def weight_squared_with_delay(weight):
    """Simulated I/O-bound operation"""
    time.sleep(0.001)  # Simulate I/O delay
    return weight ** 2

if __name__ == '__main__':
    # Generate test data
    weights = list(range(1, 10001))  # 10,000 numbers

    print("Testing with CPU-bound operations (weight ** 2):")
    print("=" * 50)

    # Sequential execution
    start_time = time.time()
    sequential_results = [weight_squared(w) for w in weights]
    sequential_time = time.time() - start_time
    print(f"Sequential execution: {sequential_time:.4f} seconds")

    # ThreadPoolExecutor (won't help with CPU-bound)
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        thread_results = list(executor.map(weight_squared, weights))
    thread_time = time.time() - start_time
    print(f"ThreadPoolExecutor: {thread_time:.4f} seconds")

    # Skip ProcessPoolExecutor for now to avoid Windows multiprocessing issues
    print("ProcessPoolExecutor: [Skipped - Windows multiprocessing complexities]")

    print(f"\nSpeedup with threads: {sequential_time/thread_time:.2f}x")
    print("Note: Thread 'speedup' < 1.0 shows threads are SLOWER due to GIL + overhead")

    print("\n" + "=" * 50)
    print("Testing with I/O-bound operations (with artificial delay):")
    print("=" * 50)

    # Smaller dataset for I/O test (to avoid long waits)
    small_weights = list(range(1, 51))  # 50 numbers

    # Sequential execution with I/O
    start_time = time.time()
    sequential_io_results = [weight_squared_with_delay(w) for w in small_weights]
    sequential_io_time = time.time() - start_time
    print(f"Sequential I/O execution: {sequential_io_time:.4f} seconds")

    # ThreadPoolExecutor with I/O (will help significantly)
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        thread_io_results = list(executor.map(weight_squared_with_delay, small_weights))
    thread_io_time = time.time() - start_time
    print(f"ThreadPoolExecutor I/O: {thread_io_time:.4f} seconds")

    print(f"\nI/O Speedup with threads: {sequential_io_time/thread_io_time:.2f}x")
    print("Note: Thread speedup > 1.0 shows threads HELP with I/O-bound tasks")

    # Verify results are identical
    print(f"\nResults identical (CPU): {sequential_results == thread_results}")
    print(f"Results identical (I/O): {sequential_io_results == thread_io_results}")
