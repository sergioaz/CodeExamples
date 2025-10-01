import pandas as pd
from tqdm import tqdm
import time

# Initialize tqdm for pandas
tqdm.pandas(desc="Applying Function")

df = pd.DataFrame({'a': range(1000000)})

# Use progress_apply instead of apply
df['b'] = df['a'].progress_apply(lambda x: x * 2)


for i in tqdm(range(500), desc="Processing Users"):
    time.sleep(0.01)

for i in tqdm(range(500), desc="Analyzing Data"):
    time.sleep(0.01)