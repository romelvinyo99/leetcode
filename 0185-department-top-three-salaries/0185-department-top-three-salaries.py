import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    full = pd.merge(
        employee.drop(columns = ["id"]).rename(columns={"name":"Employee"}),
        department.rename(columns = {"name": "Department"}),
        how = "inner", 
        left_on="departmentId", 
        right_on="id").drop(columns = ["id", "departmentId"], axis=1)
    full["rank"] = full.groupby("Department")["salary"].rank(method="dense", ascending=False)
    result = full[full["rank"].isin([1, 2, 3])].drop(columns = ["rank"])
    return result
    
    

    