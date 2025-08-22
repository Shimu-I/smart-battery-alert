![GitHub last commit](https://img.shields.io/github/last-commit/Shimu-I/smart-battery-alert)
![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=Shimu-I/smart-battery-alert)

# Battery Reminder

A lightweight Python script to monitor laptop battery levels and send desktop notifications to maintain battery health by keeping the charge between 40% and 80%. Designed for Windows 11, tested on an MSI Modern 15 B7M.

## Features
- Monitors battery level every minute using the `psutil` library.
- Sends notifications:
  - Every 5 minutes when the battery is ≤40% and unplugged, prompting to plug in the charger.
  - Once when the battery is ≥80% and plugged in, prompting to unplug the charger.
- Stops gracefully with the `Esc` key, using the `keyboard` library.
- Runs in the background with minimal CPU/memory usage.
- Displays startup and shutdown notifications for user feedback.
- Handles errors (e.g., inaccessible battery data) with informative notifications.

## Prerequisites
- **Operating System**: Windows 11 (other Windows versions may work but are untested).
- **Python**: Version 3.8 or higher.
- **Python Libraries**:
  - `psutil`: For battery monitoring.
  - `plyer`: For cross-platform desktop notifications.
  - `keyboard`: For detecting the `Esc` key to stop the script.

## Installation
1. **Install Python**:
   - Download and install Python 3.8+ from [python.org](https://www.python.org/downloads/).
   - Ensure Python is added to your PATH during installation.

2. **Install Required Libraries**:
   Open a Command Prompt and run:
   ```bash
   pip install psutil plyer keyboard
   ```

3. **Download the Script**:
   - Clone or download this repository to your local machine.
   - Save `BatteryReminder.py` to a desired location (e.g., `<path_to_script>/BatteryReminder.py`).

## Usage
1. **Run the Script**:
   - Open a Command Prompt and navigate to the script’s directory:
     ```bash
     cd <path_to_script>
     ```
   - Run the script:
     ```bash
     <path_to_python>/python.exe BatteryReminder.py
     ```
     Replace `<path_to_python>` with the path to your Python executable (e.g., `C:\Python39`).
   - Alternatively, create a shortcut (see below) for easier access.

2. **Stop the Script**:
   - Press the `Esc` key to stop the script. A “Battery Reminder Stopped” notification will appear.
   - If running in a terminal, you can also press `Ctrl + C` or close the terminal window.

3. **Silent Execution** (Optional):
   - Rename `BatteryReminder.py` to `BatteryReminder.pyw`.
   - Run with `pythonw.exe` to avoid a terminal window:
     ```bash
     <path_to_python>/pythonw.exe <path_to_script>/BatteryReminder.pyw
     ```
   - Stop with the `Esc` key or end the `pythonw.exe` process in Task Manager.

4. **Create a Shortcut** (Optional):
   - Right-click `BatteryReminder.py`, select **Create shortcut**.
   - Edit the shortcut’s **Properties**:
     - **Target**: `<path_to_python>/python.exe "<path_to_script>/BatteryReminder.py"`
     - **Start in**: `<path_to_script>`
     - Set **Run** to **Minimized** (optional).
   - For silent execution, use `BatteryReminder.pyw` and `pythonw.exe` in the **Target**.
   - Double-click the shortcut to run.

5. **Run on Startup** (Optional):
   - Copy the shortcut to the Startup folder:
     - Press `Win + R`, type `shell:startup`, and press Enter.
     - Move the shortcut to this folder (e.g., `C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`).
   - The script will start automatically on login.

## How It Works
- **Battery Monitoring**: Uses `psutil.sensors_battery()` to check battery percentage and charging status every 60 seconds.
- **Notifications**: Uses `plyer.notification` to display Windows desktop notifications:
  - **Low Battery**: When ≤40% and unplugged, notifies every 5 minutes.
  - **High Battery**: When ≥80% and plugged in, notifies once.
  - **Errors**: Notifies if battery data is unavailable or errors occur.
- **Termination**: Listens for the `Esc` key using `keyboard.wait('esc')` to stop the script cleanly via a `threading.Event`.
- **Threading**: Runs battery monitoring in a separate thread to allow simultaneous key listening.

## Troubleshooting
- **No Notifications**:
  - Ensure notifications are enabled: Windows Settings > System > Notifications > Python.
  - Verify libraries: `pip show psutil plyer keyboard`.
- **Esc Key Doesn’t Work**:
  - Run the shortcut as administrator: **Properties > Compatibility > Run as administrator**.
  - Ensure `keyboard` is installed.
- **Script Errors**:
  - Run in a terminal to see errors:
    ```bash
    <path_to_python>/python.exe <path_to_script>/BatteryReminder.py
    ```
  - Check for battery driver issues if “Battery Reminder Error” notifications appear.
- **Multiple Instances**:
  - End `python.exe` or `pythonw.exe` processes in Task Manager if duplicate notifications occur.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue on GitHub.

## Author
- Jasmin Sultana Shimu (GitHub: [Shimu-I])
