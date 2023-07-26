import os
import subprocess

def is_ssh_installed():
    try:
        subprocess.run(["which", "ssh"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def is_ssh_running():
    try:
        status_output = subprocess.check_output(["ps", "-C", "sshd", "-o", "comm="]).decode("utf-8")
        return "sshd" in status_output
    except subprocess.CalledProcessError:
        return False

def start_ssh_server():
    try:
        start_command = "sudo service ssh start"
        os.system(start_command)
    except Exception as ex:
        print(f"Error starting SSH server: {ex}")

def setup_ssh_server():
    try:
        # Check if SSH is already installed
        if not is_ssh_installed():
            install_command = "apt-get update && apt-get install -y openssh-server"
            subprocess.run(["sudo", "sh", "-c", install_command], check=True)

        # Check if SSH is already running
        if not is_ssh_running():
            start_ssh_server()

        # Monitor the status of the SSH server
        status_output = subprocess.check_output(["service", "ssh", "status"]).decode("utf-8")
        print("SSH Server Status:")
        print(status_output)

        # Log the SSH server status to a file
        log_file = "/var/log/ssh_server_status.log"
        with open(log_file, "a") as f:
            f.write(status_output)

    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    setup_ssh_server()
