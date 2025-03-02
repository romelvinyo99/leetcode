import pandas as pd
import numpy as np

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by="score", ascending=False, inplace=True)
    scores["rank"] = scores["score"].rank(method = "dense", ascending=False)
    return scores[["score", "rank"]]            
        