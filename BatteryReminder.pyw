import psutil
import time
import threading
import keyboard
from plyer import notification

def show_notification(title, message):
    """Display a desktop notification."""
    notification.notify(
        title=title,
        message=message,
        app_name="Battery Reminder",
        timeout=10  # Notification stays for 10 seconds
    )

def check_battery(stop_event):
    """Monitor battery and trigger notifications based on charge levels."""
    last_low_battery_notification = 0  # Track time of last low battery notification
    notification_interval = 300  # 5 minutes in seconds

    while not stop_event.is_set():
        try:
            battery = psutil.sensors_battery()
            if battery is None:
                show_notification(
                    "Battery Reminder Error",
                    "Unable to access battery information. Ensure battery is present."
                )
                time.sleep(60)
                continue

            percent = battery.percent
            is_plugged = battery.power_plugged

            # Check if battery is <= 40% and not plugged in
            if percent <= 40 and not is_plugged:
                current_time = time.time()
                if current_time - last_low_battery_notification >= notification_interval:
                    show_notification(
                        "Low Battery Warning",
                        f"Battery at {percent}%. Please plug in your charger."
                    )
                    last_low_battery_notification = current_time

            # Check if battery is >= 80% and plugged in
            elif percent >= 80 and is_plugged:
                show_notification(
                    "Battery Charged",
                    f"Battery at {percent}%. Please unplug your charger to maintain battery health."
                )

            time.sleep(60)  # Check every 1 minute

        except Exception as e:
            show_notification(
                "Battery Reminder Error",
                f"An error occurred: {str(e)}"
            )
            time.sleep(60)

def main():
    """Start battery monitoring and keyboard listener."""
    stop_event = threading.Event()

    # Start battery monitoring in a separate thread
    battery_thread = threading.Thread(target=check_battery, args=(stop_event,))
    battery_thread.daemon = True  # Exit thread when main program exits
    battery_thread.start()

    print("Battery Reminder is running. Press Esc to stop.")
    show_notification(
        "Battery Reminder Started",
        "Battery monitoring is active. Press Esc to stop."
    )

    # Listen for Esc key to stop the program
    keyboard.wait('esc')
    stop_event.set()  # Signal the battery thread to stop
    print("Battery Reminder stopped.")
    show_notification(
        "Battery Reminder Stopped",
        "The battery monitoring program has been terminated."
    )

if __name__ == "__main__":
    main()
