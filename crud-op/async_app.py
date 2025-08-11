import time
from timeit import default_timer as timer
import asyncio

async def run_task(name, seconds):
    start = timer()
    print(f"Task {name} started at {round(start, 2)}")
    await asyncio.sleep(seconds)
    end = timer()
    print(f"Task {name} ended at {round(end, 2)}")
    print(f"Task {name} completed in {round(end - start, 2)} seconds")

async def main():
    start = timer()
    tasks = [
        asyncio.create_task(run_task("A", 2)),
        asyncio.create_task(run_task("B", 1)),
        asyncio.create_task(run_task("C", 3))
    ]
    await asyncio.gather(*tasks)
    print("All tasks completed")
    print(f"Total time taken: {round(timer() - start, 2)} seconds")

asyncio.run(main())