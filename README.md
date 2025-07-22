# 🔍 Multithreaded Port Scanner in Python

This is a simple yet powerful **multithreaded TCP port scanner** built using Python. It scans a target IP address for open ports in the range of 1 to 1024 and saves the results to a file.

---

## ⚙️ Features

- Scans a range of ports on a target IP
- Uses multithreading for fast and efficient scanning
- Detects open ports and logs them
- Saves scan results with timestamp to a `results.txt` file
- Thread-safe printing and list management using `threading.Lock`

---

## 🚀 How It Works

The scanner attempts to establish a TCP connection to each port. If the connection succeeds, the port is considered **open**.

Threads are used to divide the scanning task across multiple workers, increasing speed and efficiency.

---

## 🛠️ Technologies Used

- Python 3
- `socket` for low-level networking
- `threading` for concurrency
- `queue` for safe task distribution
- `datetime` for timestamping

---

📂 Output
Console Output: Displays open ports in real time.

File Output: Appends results with a timestamp to results.txt

⚠️ Disclaimer
This tool is for educational purposes only.
Do not use it to scan any network or host you do not have explicit permission to test.
Unauthorized scanning is illegal and unethical
