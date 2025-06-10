import time

def process_data_chunk(chunk):
    result = 0
    for _ in range(1_000_000):
        result += sum(c * 0.01 for c in chunk)
    return result

def analyze_large_dataset(dataset):
    total_result = 0
    for chunk in dataset:
        total_result += process_data_chunk(chunk)
    return total_result