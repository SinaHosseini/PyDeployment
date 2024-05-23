import time
import random
import asyncio

async def marriage(name):
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"{name} marriage after {r} years")


async def main():
    await asyncio.gather(marriage("mamad"), marriage("gholi"), marriage("goli"), marriage("alex"))

    


if __name__ == "__main__":
    stat_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - stat_time
    print(f"Executed in {total_time} seconds")
    