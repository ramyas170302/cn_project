def classify_zone(signal, ping, packet_loss, speed):
    """
    Classify Wi-Fi/network quality based on
    signal strength, ping, packet loss and speed.
    """

    # Good connection
    if (
        signal >= 70
        and ping <= 50
        and packet_loss <= 2
        and speed >= 20
    ):
        return "Good"

    # Weak connection
    elif (
        signal >= 50
        and ping <= 100
        and packet_loss <= 5
        and speed >= 10
    ):
        return "Weak"

    # Poor / Dead Zone
    else:
        return "Poor / Dead Zone"


def get_zone_color(status):
    """Return color indicator for the zone."""

    if status == "Good":
        return "🟢"

    elif status == "Weak":
        return "🟡"

    else:
        return "🔴"


def get_zone_message(status):
    """Return a simple explanation."""

    if status == "Good":
        return "Wi-Fi connectivity is stable."

    elif status == "Weak":
        return "Wi-Fi is available but performance may be unstable."

    else:
        return "Poor connectivity detected. This area may require better Wi-Fi coverage."