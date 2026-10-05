import subprocess
import re
import requests
import time


def measure_ping(host="8.8.8.8"):
    """Measure network ping in milliseconds."""

    try:
        result = subprocess.run(
            ["ping", "-n", "4", host],
            capture_output=True,
            text=True
        )

        output = result.stdout

        match = re.search(r"Average = (\d+)ms", output)

        if match:
            return int(match.group(1))

        return 999

    except Exception:
        return 999


def measure_packet_loss(host="8.8.8.8"):
    """Calculate packet loss percentage."""

    try:
        result = subprocess.run(
            ["ping", "-n", "4", host],
            capture_output=True,
            text=True
        )

        output = result.stdout

        match = re.search(r"\((\d+)% loss\)", output)

        if match:
            return int(match.group(1))

        return 100

    except Exception:
        return 100


def measure_speed():
    """Estimate download speed."""

    try:
        url = "https://speedtest.tele2.net/1MB.zip"

        start_time = time.time()

        response = requests.get(url, timeout=10)

        end_time = time.time()

        file_size = len(response.content)

        duration = end_time - start_time

        if duration == 0:
            return 0

        speed_mbps = (file_size * 8) / duration / 1_000_000

        return round(speed_mbps, 2)

    except Exception:
        return 0


def analyze_network():

    ping = measure_ping()

    packet_loss = measure_packet_loss()

    speed = measure_speed()

    if ping < 50 and packet_loss < 2 and speed > 20:
        status = "Good"

    elif ping < 100 and packet_loss < 5 and speed > 10:
        status = "Weak"

    else:
        status = "Poor / Dead Zone"

    return {
        "Ping": ping,
        "Packet Loss": packet_loss,
        "Speed": speed,
        "Status": status
    }
