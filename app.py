import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Wi-Fi Connectivity Analyzer",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Smart Wi-Fi Connectivity Mapper")
st.write("Analyze Wi-Fi quality and identify weak or dead zones.")

st.divider()

# Location selection
location = st.selectbox(
    "📍 Select Test Location",
    ["Classroom", "Computer Lab", "Library", "Corridor", "Canteen"]
)

# Start scan
if st.button("🔍 Start Scan", use_container_width=True):

    # Demo data
    demo_data = {
        "Classroom": [-45, 25, 45, 0],
        "Computer Lab": [-58, 45, 35, 1],
        "Library": [-67, 80, 25, 3],
        "Corridor": [-82, 180, 8, 12],
        "Canteen": [-72, 110, 15, 6]
    }

    signal, ping, speed, packet_loss = demo_data[location]

    # Classification
    if signal >= -55 and ping < 50 and packet_loss < 2:
        status = "🟢 GOOD CONNECTION"
    elif signal >= -70 and ping < 100 and packet_loss < 5:
        status = "🟡 WEAK CONNECTION"
    else:
        status = "🔴 POOR / DEAD ZONE"

    st.subheader(f"📊 Network Analysis — {location}")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📶 Signal Strength", f"{signal} dBm")
    col2.metric("⏱️ Ping", f"{ping} ms")
    col3.metric("⚡ Speed", f"{speed} Mbps")
    col4.metric("📦 Packet Loss", f"{packet_loss}%")

    st.divider()

    st.subheader("Connectivity Status")
    st.info(status)

    # Recommendation
    if "GOOD" in status:
        recommendation = "Wi-Fi connectivity is stable in this location."
    elif "WEAK" in status:
        recommendation = "Consider improving Wi-Fi coverage or repositioning the access point."
    else:
        recommendation = "Poor connectivity detected. An additional or repositioned access point may be required."

    st.subheader("💡 Recommendation")
    st.write(recommendation)


st.divider()

# Connectivity map
st.subheader("🗺️ Campus Connectivity Overview")

map_data = pd.DataFrame({
    "Location": [
        "Classroom",
        "Computer Lab",
        "Library",
        "Corridor",
        "Canteen"
    ],
    "Status": [
        "🟢 Good",
        "🟢 Good",
        "🟡 Weak",
        "🔴 Dead Zone",
        "🟡 Weak"
    ]
})

st.dataframe(
    map_data,
    use_container_width=True,
    hide_index=True
)

st.caption("Smart Wi-Fi Connectivity Mapper & Dead-Zone Analyzer")