"""Script to generate data exam results data.
"""

import pandas as pd
import numpy as np

N = 2000000

df = pd.DataFrame({
    "roll_number": range(1000000, 1000000+N),
    "name": "Foo Bar",
})

for i in range(10):
    df[f'subject {i}'] = np.random.randint(0, 100, N)

df.to_csv("data.csv", index=False)
