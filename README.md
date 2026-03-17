# Network Traffic Analytics API

## 🚀 Overview

This project is a backend system that processes network packet captures (.pcap files) and provides insights through REST APIs.

## 🛠 Tech Stack

* Python
* Flask
* Pandas
* SQLite
* Wireshark (PCAP data)

## ⚙️ Features

* Extracts packet data (IP, protocol)
* Stores data in SQLite database
* Provides REST APIs:

  * `/top-ips` → Top communicating IP addresses
  * `/protocols` → Protocol distribution

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the server:

```
python app.py
```

3. Open in browser:

* http://127.0.0.1:5000/load
* http://127.0.0.1:5000/top-ips
* http://127.0.0.1:5000/protocols

## 📊 Output Example

Returns JSON data showing IP activity and protocol usage.

## 💡 Use Case

Helps analyze network traffic and detect unusual patterns.

---

