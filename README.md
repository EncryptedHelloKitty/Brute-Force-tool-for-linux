# Brute-Force Tool

## Description
This repository contains a Linux Python-based brute-force tool developed for educational purposes as part of a university project. The tool is designed to simulate brute-force attacks on systems, such as web login forms or SSH servers, by systematically trying every combination from a specified wordlist.

> **Disclaimer:** This tool is intended for ethical hacking and educational purposes only. Unauthorized use of this tool on systems you do not own or have explicit permission to test is illegal and unethical.

## Features
- **Custom Wordlist Support:** Use any wordlist to attempt password cracking.
- **HTTP Brute-Forcing:** Automate login attempts on web forms.
- **SSH Brute-Forcing:** Test SSH credentials using the `paramiko` library.
- **Error Handling & Rate Limiting:** Graceful handling of network errors and optional delay between attempts to avoid detection.

## Installation

### Prerequisites
- Linux
- Python 3.x
- Required Python packages:
  - `requests` for HTTP brute-forcing
  - `paramiko` for SSH brute-forcing

### Setting Up the Environment
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/brute-force-tool.git
   cd brute-force-tool
