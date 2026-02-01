### Import Netmiko for SSH connectivity to network devices
from netmiko import ConnectHandler

### Import datetime to generate timestamped backup filenames
from datetime import datetime

### Import device inventory from separate file
from devices import devices

### Import OS module for directory and file handling
import os


def backup_device_config(device):
    ### Extract device name for folder creation
    device_name = device["name"]

    ### Timestamp for the backup filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")

    ### Backup directory path: backups/<device-name>/
    backup_dir = os.path.join("backups", device_name)

    ### Build the full backup file path with timestamp
    backup_file = os.path.join(backup_dir, f"{timestamp}.cfg")

    ### Create the backup directory if it does not already exist
    os.makedirs(backup_dir, exist_ok=True)

    try:
        ### Attempt SSH connection to the device
        print(f"[+] Connecting to {device_name} ({device['host']})")
        connection = ConnectHandler(**device)

        ### Enter enable mode (required for show running-config)
        connection.enable()

        ### Retrieve the running configuration
        running_config = connection.send_command("show running-config")

        ### Write the running configuration to a timestamped file
        with open(backup_file, "w") as f:
            f.write(running_config)

        ### Close the SSH connection cleanly
        connection.disconnect()

        ### Indicate successful backup
        print(f"[✔] Backup completed for {device_name}")

    except Exception as e:
        ### Handle unreachable devices or authentication failures gracefully
        print(f"[✖] Failed to backup {device_name}: {e}")


def main():
    ### Iterate through each device in the inventory
    for device in devices:
        backup_device_config(device)


### Ensure the script only runs when executed directly
if __name__ == "__main__":
    main()
