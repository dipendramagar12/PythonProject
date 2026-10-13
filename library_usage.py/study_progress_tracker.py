from tqdm import tqdm
import time

print("STUDY PROGRESS TACKER")

for i in tqdm(range(20), desc="Completing study task"):
    time.sleep(0.5)

print("All 20 task completed")
