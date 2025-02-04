# Indigo Hartsell
# 20250204 110000
# hog

import psutil
import time

def consume_memory(step_mb=100, sleep_time=0.5):
    """Consumes memory progressively until nearly 100% usage."""
    consumed = []
    total_mem = psutil.virtual_memory().total
    print(f"Total system memory: {total_mem / (1024**3):.2f} GB")

    try:
        while True:
            used_mem = psutil.virtual_memory().used
            free_mem = total_mem - used_mem
            if free_mem < step_mb * 1024 * 1024:
                print("Almost out of memory, stopping allocation.")
                break

            print(f"Allocating {step_mb}MB, Free: {free_mem / (1024**3):.2f} GB")
            consumed.append(bytearray(step_mb * 1024 * 1024))
            time.sleep(sleep_time)

    except MemoryError:
        print("Memory allocation failed! Out of memory.")

    finally:
        print("Releasing memory...")
        consumed.clear()

if __name__ == "__main__":
    consume_memory()
