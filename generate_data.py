import pandas as pd
import random

data = []

for _ in range(150):
    study_hours = random.randint(0, 24)
    attendance = random.randint(40, 100)
    previous_marks = random.randint(40, 100)

    # Realistic formula with noise
    final_score = (
        0.3 * study_hours +
        0.3 * attendance +
        0.4 * previous_marks +
        random.randint(-5, 5)
    )

    # Cap between 0 and 100
    final_score = max(0, min(100, round(final_score)))

    data.append([study_hours, attendance, previous_marks, final_score])

df = pd.DataFrame(
    data,
    columns=["study_hours", "attendance", "previous_marks", "final_score"]
)

df.to_csv("data.csv", index=False)

print("New dataset generated with 150 rows.")
