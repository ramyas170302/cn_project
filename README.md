# 📡 Smart Wi-Fi Connectivity Mapper & Dead-Zone Analyzer

## 📌 Project Overview

**Smart Wi-Fi Connectivity Mapper & Dead-Zone Analyzer** is a Computer Networks project designed to analyze Wi-Fi and network connectivity at different locations.

In a college campus, some areas may have good Wi-Fi while other areas may experience weak signals, high latency, packet loss, or slow internet speed. These areas can be difficult to identify manually.

This project collects network parameters from different locations and analyzes them to determine the overall connectivity quality.

The system classifies locations into:

* 🟢 **Good Connectivity**
* 🟡 **Weak Connectivity**
* 🔴 **Poor / Dead Zone**

The results can be displayed through a simple dashboard and connectivity map.

---

# 🎯 Problem Statement

Wi-Fi connectivity can vary significantly depending on the location of a device.

Traditional Wi-Fi checking methods may focus mainly on signal strength. However, a strong signal does not always mean good internet performance.

For example:

* A location may have good signal strength but high latency.
* A location may have reasonable signal strength but high packet loss.
* A location may have a stable connection but very low internet speed.

Therefore, there is a need for a system that considers multiple network parameters instead of relying only on signal strength.

---

# 💡 Proposed Solution

The proposed system measures multiple network parameters and combines them to analyze the quality of connectivity.

The main parameters considered are:

| Parameter             | Purpose                                                       |
| --------------------- | ------------------------------------------------------------- |
| Wi-Fi Signal Strength | Determines the strength of the wireless connection            |
| Ping / Latency        | Measures the time required for packets to reach a destination |
| Packet Loss           | Determines how many packets fail to reach the destination     |
| Internet Speed        | Measures approximate network data transfer speed              |

Based on these measurements, the system classifies the location and provides a basic recommendation.

---

# 🎯 Objectives

The main objectives of the project are:

1. To monitor Wi-Fi connectivity at different locations.
2. To measure important network parameters.
3. To identify weak and poor connectivity areas.
4. To classify locations based on network quality.
5. To visualize connectivity across different campus areas.
6. To provide simple recommendations for areas with poor connectivity.
7. To create an easy-to-use interface for network analysis.

---

# ✨ Main Features

### 📶 1. Wi-Fi Signal Monitoring

The system can obtain the available Wi-Fi network information and signal strength.

Signal strength helps identify areas where the wireless signal may be weak.

---

### ⏱️ 2. Ping / Latency Measurement

The system sends packets to a network destination and measures the response time.

Lower latency generally indicates a faster response.

Example:

```text
Ping: 25 ms → Good
Ping: 80 ms → Acceptable
Ping: 180 ms → High latency
```

---

### 📦 3. Packet Loss Detection

Packet loss represents the percentage of packets that do not successfully reach the destination.

Example:

```text
Packet Loss: 0%  → Good
Packet Loss: 3%  → Slight problem
Packet Loss: 15% → Poor
```

High packet loss can result in unstable connections.

---

### ⚡ 4. Internet Speed Measurement

The system estimates the download speed of the current network connection.

This helps identify locations where the connection may be slow even if the Wi-Fi signal appears acceptable.

---

### 🧠 5. Connectivity Classification

The measured parameters are analyzed and the location is classified as:

```text
🟢 Good
🟡 Weak
🔴 Poor / Dead Zone
```

---

### 🗺️ 6. Connectivity Map

The system can visualize different campus locations using status indicators.

Example:

```text
              🟢 Classroom

 🟢 Lab      🟡 Library      🔴 Corridor

       🟡 Canteen       🟢 Seminar Hall

              🔴 Parking
```

This makes it easier to identify areas that require better Wi-Fi coverage.

---

### 💡 7. Recommendations

For locations with poor connectivity, the system can provide basic suggestions such as:

* Reposition the Wi-Fi access point.
* Add an additional access point.
* Check network congestion.
* Check for wireless interference.
* Monitor bandwidth usage.

---

# 🔄 System Workflow

The overall working of the system is:

```text
          Start
            ↓
     Select Location
            ↓
       Scan Wi-Fi
            ↓
   Collect Network Data
            ↓
 ┌─────────────────────────┐
 │ Signal Strength         │
 │ Ping / Latency          │
 │ Packet Loss             │
 │ Internet Speed          │
 └─────────────────────────┘
            ↓
     Analyze Parameters
            ↓
    Classify Connectivity
            ↓
 ┌─────────────────────────┐
 │ 🟢 Good                 │
 │ 🟡 Weak                 │
 │ 🔴 Poor / Dead Zone     │
 └─────────────────────────┘
            ↓
    Generate Recommendation
            ↓
    Display Dashboard/Map
            ↓
           End
```

---

# 🏗️ System Architecture

```text
                    User
                     │
                     ▼
              Streamlit UI
                     │
                     ▼
             Wi-Fi Scanner
                     │
                     ▼
           Network Analyzer
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     Signal        Ping       Packet Loss
     Strength                   + Speed
        │            │            │
        └────────────┼────────────┘
                     ▼
             Zone Classifier
                     │
                     ▼
             Recommendation
                     │
                     ▼
          Dashboard / Map
```

---

# 📂 Project Structure

```text
wifi-connectivity-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── wifi_data.csv
│
├── modules/
│   ├── wifi_scanner.py
│   ├── network_analyzer.py
│   ├── zone_classifier.py
│   └── recommendations.py
│
└── utils/
    ├── data_processor.py
    └── map_generator.py
```

---

# 📁 Module Description

## `app.py`

The main application file.

It:

* Creates the Streamlit interface.
* Allows users to select locations.
* Displays network measurements.
* Displays connectivity status.
* Shows recommendations.
* Displays the connectivity overview.

---

## `wifi_scanner.py`

Responsible for detecting available Wi-Fi networks and obtaining their signal information.

It uses Windows network commands to retrieve Wi-Fi information.

---

## `network_analyzer.py`

Responsible for measuring network performance.

It handles:

* Ping
* Packet loss
* Approximate download speed

---

## `zone_classifier.py`

Analyzes the collected network parameters and classifies the location.

Example:

```text
Good
Weak
Poor / Dead Zone
```

---

## `recommendations.py`

Generates suggestions based on the detected network problem.

For example:

```text
High packet loss detected.
Check for wireless interference or network instability.
```

---

## `data_processor.py`

Handles stored Wi-Fi/network data.

It can:

* Read CSV data.
* Calculate averages.
* Count different zone types.
* Identify problem areas.

---

## `map_generator.py`

Creates a visual representation of connectivity across different locations.

Different colors represent different connectivity levels.

---

# 🛠️ Technologies Used

### Programming Language

**Python**

Used for implementing the network analysis and application logic.

### User Interface

**Streamlit**

Used to create the interactive web-based dashboard.

### Data Processing

**Pandas**

Used to read, process, and analyze network data.

### Visualization

**Matplotlib**

Used to create the connectivity map and visualizations.

### Network Testing

**Windows `netsh` and `ping`**

Used for Wi-Fi and network measurements on Windows.

### HTTP Requests

**Requests**

Used for approximate network speed testing.

---

# 💻 Requirements

* Windows operating system
* Python 3.x
* Wi-Fi/network connection
* VS Code or another Python IDE
* Internet connection for speed and external ping testing

---

# ⚙️ Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/wifi-connectivity-analyzer.git
```

### Step 2: Open the project

```bash
cd wifi-connectivity-analyzer
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run:

```bash
streamlit run app.py
```

The Streamlit application will open in the browser.

Usually it will be available at:

```text
http://localhost:8501
```

---

# 📊 Sample Data

The project includes sample network data for demonstration.

Example:

| Location     |  Signal |   Ping |   Speed | Packet Loss | Status    |
| ------------ | ------: | -----: | ------: | ----------: | --------- |
| Classroom    | -45 dBm |  25 ms | 45 Mbps |          0% | Good      |
| Computer Lab | -58 dBm |  45 ms | 35 Mbps |          1% | Good      |
| Library      | -67 dBm |  80 ms | 25 Mbps |          3% | Weak      |
| Corridor     | -82 dBm | 180 ms |  8 Mbps |         12% | Dead Zone |
| Canteen      | -72 dBm | 110 ms | 15 Mbps |          6% | Weak      |

> **Note:** Sample data is used for the initial demonstration. Real-time measurements can be collected from the device for live testing.

---

# 🧪 Demo Procedure

For the college demonstration:

### Step 1

Open the Streamlit application.

### Step 2

Select a campus location.

### Step 3

Start the network scan/analysis.

### Step 4

Display:

* Signal strength
* Ping
* Packet loss
* Internet speed

### Step 5

Show the connectivity classification.

Example:

```text
📶 Signal Strength: -82 dBm
⏱️ Ping: 180 ms
📦 Packet Loss: 12%
⚡ Speed: 8 Mbps

Status: 🔴 Poor / Dead Zone
```

### Step 6

Display the connectivity map.

### Step 7

Show the recommendation for improving connectivity.

---

# 📌 Computer Network Concepts Used

This project demonstrates several Computer Networks concepts:

* Wireless networking
* Wi-Fi signal strength
* Network latency
* Ping
* Packet loss
* Bandwidth
* Network performance
* Network monitoring
* Connectivity analysis
* Access point coverage

---

# ⚠️ Limitations

The current version has some limitations:

1. Signal strength depends on the device and operating system.
2. Internet speed can vary depending on network traffic.
3. Ping depends on the selected destination server.
4. Sample data may be used during demonstration.
5. The campus map is a simplified representation.
6. The system does not automatically determine the exact physical location of the device.

---

# 🚀 Future Enhancements

The project can be improved by adding:

* 📍 GPS/location-based mapping
* 🗺️ Real campus floor maps
* 📈 Historical connectivity graphs
* 📊 Real-time monitoring
* 🔔 Alerts when connectivity becomes poor
* 🤖 ML-based network quality prediction
* 📱 Mobile application
* 🏫 Automatic campus-wide Wi-Fi surveying
* 📡 Multiple access-point analysis
* 📅 Historical reports for network administrators

---

# 🎓 Project Type

**Computer Networks Mini Project**

### Project Title

**Smart Wi-Fi Connectivity Mapper & Dead-Zone Analyzer**

### Main Goal

> To analyze Wi-Fi connectivity using multiple network parameters and identify areas with weak or poor network performance.

---

# 👥 Team

Developed as a Computer Networks mini-project by:

**Team Members:**

* Member 1
* Member 2
* Member 3
* Member 4

---

# 📄 License

This project is developed for educational and academic purposes.
