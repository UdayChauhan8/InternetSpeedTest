Python Internet Speed Test
A simple, command-line Python script to measure your internet download speed, upload speed, and ping using the speedtest-cli library.

🚀 Features
Download Speed: Measures your internet's download speed in Mbps.

Upload Speed: Measures your internet's upload speed in Mbps.

Ping: Determines the latency to the optimal server in milliseconds.

Best Server: Automatically finds the best server to ensure accurate results.

📋 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine. This guide is tailored for Ubuntu-based Linux systems.

Prerequisites
Make sure you have Python 3 and the venv module installed on your system.


# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

Your terminal prompt will now be prefixed with (venv).

Install the required packages:
The necessary Python library is listed in the requirements.txt file.

pip install -r requirements.txt

Note: If you don't have a requirements.txt file, you can create one by running pip freeze > requirements.txt after installing the package below, or just install the package directly:

pip install speedtest-cli

⚙️ Usage
With your virtual environment still active, run the script from the terminal:

python my_speed_test.py

Example Output
You will see an output similar to the following:

Running speed test, please wait... ⏳
Finding the best server...
Testing download speed...
Download Speed: 94.52 Mbps 🔽
Testing upload speed...
Upload Speed: 45.18 Mbps 🔼
Ping: 12.345 ms 핑

📜 License
This project is licensed under the MIT License - see the LICENSE.md file for details.

🙌 Contributing
Contributions are welcome! If you have suggestions for improving the script, feel free to fork the repository and submit a pull request.
