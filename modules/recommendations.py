def get_recommendation(signal, ping, packet_loss, speed, status):
    """Generate a recommendation based on network conditions."""

    recommendations = []

    if signal < 50:
        recommendations.append(
            "Consider repositioning the Wi-Fi access point or adding another access point."
        )

    if ping > 100:
        recommendations.append(
            "High latency detected. Check network traffic or router connectivity."
        )

    if packet_loss > 5:
        recommendations.append(
            "Packet loss is high. Check for interference or unstable network connections."
        )

    if speed < 10:
        recommendations.append(
            "Low internet speed detected. Check bandwidth usage or network capacity."
        )

    if status == "Good":
        return "Wi-Fi connectivity is stable. No major issues detected."

    if not recommendations:
        return "Network conditions should be monitored further."

    return " ".join(recommendations)