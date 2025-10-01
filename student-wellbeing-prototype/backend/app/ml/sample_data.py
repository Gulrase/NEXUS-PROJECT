import pandas as pd
import numpy as np

def generate(n=200):
    rng = np.random.RandomState(42)
    data = []
    for i in range(n):
        gpa = np.round(rng.normal(2.8, 0.6), 2)
        attendance = np.round(rng.normal(80, 12), 2)
        chats = rng.poisson(5)
        dropped = int((gpa < 2.2 and attendance < 75) or rng.rand() < 0.05)
        data.append({"gpa": max(0, min(4.0, gpa)),
                     "attendance_percent": max(0, min(100, attendance)),
                     "n_chats": chats,
                     "dropped_out": dropped})
    df = pd.DataFrame(data)
    df.to_csv("backend/app/ml/student_features.csv", index=False)
    print("sample data written to student_features.csv")
