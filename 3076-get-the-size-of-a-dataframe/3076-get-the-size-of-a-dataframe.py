import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    data_shape = [i for i in players.shape]
    return data_shape


data = pd.DataFrame({
    "values": [1,2],
    "data": [3, 4]
})
result = getDataframeSize(data)    
    