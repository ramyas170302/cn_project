import matplotlib.pyplot as plt


def create_connectivity_map(data):
    """
    Create a simple Wi-Fi connectivity map
    based on location status.
    """

    # Sample positions for demonstration
    positions = {
        "Classroom": (1, 4),
        "Computer Lab": (3, 4),
        "Library": (5, 4),
        "Corridor": (7, 4),
        "Canteen": (2, 2),
        "Seminar Hall": (4, 2),
        "Block A Entrance": (6, 2),
        "Block B Corridor": (8, 2),
        "Staff Room": (3, 6),
        "Parking Area": (7, 6)
    }

    fig, ax = plt.subplots(figsize=(10, 6))

    for _, row in data.iterrows():

        location = row["Location"]
        status = row["Status"]

        if location not in positions:
            continue

        x, y = positions[location]

        if status == "Good":
            color = "green"
        elif status == "Weak":
            color = "orange"
        else:
            color = "red"

        ax.scatter(
            x,
            y,
            s=300,
            color=color,
            edgecolors="black"
        )

        ax.text(
            x,
            y + 0.35,
            location,
            ha="center",
            fontsize=9
        )

    ax.set_title("Campus Wi-Fi Connectivity Map")
    ax.set_xlabel("Campus Area")
    ax.set_ylabel("Campus Area")

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)

    ax.grid(True, alpha=0.3)

    return fig