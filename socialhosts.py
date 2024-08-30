import sys
import os

HOSTS = '/etc/hosts'
TEMP_FILE = '/etc/hosts.tmp'
BLOCKED_FILE = 'blocked_sites.txt'
MARKER = '### Block Distracting Sites ###'

def modify_hosts_file(command):
    unlocking = False

    with open(HOSTS, 'r') as input_file, open(TEMP_FILE, 'w') as output_file:
        for line in input_file:
            if line.strip() == MARKER:
                unlocking = True
                output_file.write(line)
            elif unlocking and command == 'unlock':
                output_file.write('#> ' + line if not line.startswith('#') else line)
            elif unlocking and command == 'lock':
                output_file.write(line.lstrip('#> ') if line.startswith('#> ') else line)
            else:
                output_file.write(line)

    os.replace(TEMP_FILE, HOSTS)

def create_backup(source, destination):
    with open(source, 'rb') as src, open(destination, 'wb') as dst:
        dst.write(src.read())
    # Copy permissions from source to destination
    st = os.stat(source)
    os.chmod(destination, st.st_mode)

def install():
    marker_exists = False
    with open(HOSTS, 'r') as file:
        content = file.read()
        marker_exists = MARKER in content

    if not marker_exists:
        # Backup the original file
        create_backup(HOSTS, HOSTS + '.bak')
        
        with open(HOSTS, 'a') as hosts_file, open(BLOCKED_FILE, 'r') as sites_file:
            hosts_file.write('\n')
            hosts_file.write(sites_file.read())
        print(f"Installed: Added entries from {BLOCKED_FILE} to {HOSTS}")
        print(f"A backup of the original file was created at {HOSTS}.bak")
    else:
        print(f"'{MARKER}' already exists in {HOSTS}. No changes were made.")
        print("If you want to update the entries, please remove the marker line and run install again.")

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ['lock', 'unlock', 'install']:
        print("Usage: python script.py [lock|unlock|install]")
        sys.exit(1)

    command = sys.argv[1]
    try:
        if command == 'install':
            install()
        else:
            modify_hosts_file(command)
            print(f"Successfully {command}ed the hosts file.")
    except PermissionError:
        print("Error: Permission denied. Please run the script with sudo.")
    except FileNotFoundError:
        print(f"Error: {BLOCKED_FILE} not found. Make sure it's in the same directory as the script.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")