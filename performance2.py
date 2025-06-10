import concurrent.futures
import time

def process_data_chunk(chunk):
    result = 0
    for _ in range(1_000_000):
        result += sum(c * 0.01 for c in chunk)
    return result

def analyze_large_dataset_parallel(dataset):
    total_result = 0
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_data_chunk, chunk) for chunk in dataset]
        for future in concurrent.futures.as_completed(futures):
            total_result += future.result()
    return total_result