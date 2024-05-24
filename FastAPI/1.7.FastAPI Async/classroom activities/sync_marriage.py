import time
import random

def marriage(name):
    r = random.randint(0, 10)
    time.sleep(r)
    print(f"{name} marriage after {r} years")

def main():
    for child in ["mamad", "gholi", "goli", "alex"]:
        marriage(child)

if __name__ == "__main__":
    stat_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    total_time = end_time - stat_time
    print(f"Executed in {total_time} seconds")
    