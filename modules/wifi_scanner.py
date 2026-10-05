import subprocess
import re


def scan_wifi():
    """
    Scan available Wi-Fi networks and return
    their names and signal strengths.
    """

    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        networks = []

        ssid = None
        signal = None

        for line in result.splitlines():

            line = line.strip()

            if line.startswith("SSID") and "BSSID" not in line:
                ssid = line.split(":", 1)[1].strip()

            elif "Signal" in line:
                signal_text = line.split(":", 1)[1].strip()

                match = re.search(r"(\d+)%", signal_text)

                if match and ssid:
                    signal = int(match.group(1))

                    networks.append({
                        "SSID": ssid,
                        "Signal": signal
                    })

        return networks

    except Exception as e:
        return [{
            "SSID": "Unable to scan",
            "Signal": 0,
            "Error": str(e)
        }]