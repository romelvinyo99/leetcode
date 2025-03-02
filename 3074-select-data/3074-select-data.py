import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    data = students[students["student_id"]==101]
    return data.drop(columns = ["student_id"], axis = 1)
