import pandas as pd

def transform_data(data):
    current = data["current_weather"]

    cleaned = {
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "winddirection": current["winddirection"],
        "time": current["time"]
    }

    df = pd.DataFrame([cleaned])

    return df