import pandas as pd


def load_wifi_data(file_path="data/wifi_data.csv"):
    """Load Wi-Fi data from CSV file."""

    try:
        data = pd.read_csv(file_path)
        return data

    except FileNotFoundError:
        return pd.DataFrame()


def get_status_count(data):
    """Count the number of locations in each status."""

    if data.empty:
        return {}

    return data["Status"].value_counts().to_dict()


def get_average_values(data):
    """Calculate average network values."""

    if data.empty:
        return {}

    return {
        "Average Signal": round(
            data["Signal_Strength_dBm"].mean(), 2
        ),
        "Average Ping": round(
            data["Ping_ms"].mean(), 2
        ),
        "Average Speed": round(
            data["Speed_Mbps"].mean(), 2
        ),
        "Average Packet Loss": round(
            data["Packet_Loss_Percent"].mean(), 2
        )
    }


def get_problem_areas(data):
    """Return locations with poor connectivity."""

    if data.empty:
        return pd.DataFrame()

    return data[
        data["Status"].isin(["Weak", "Dead Zone"])
    ]