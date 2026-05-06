import time
import tracemalloc

def tracking(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        tracemalloc.start()
        result = func(*args, **kwargs)
        current , peak  = tracemalloc.get_traced_memory()
        end = time.perf_counter()
        time_taken = end - start
        tracemalloc.stop()
        return float(f"{time_taken:.6f}") , float(f"{peak/(1024):.2f}") , result 
    return wrapper

#@tracking add this before the function it will return the time memory and then the result so be sure to accquire em time is in seconds and the memory in kbs