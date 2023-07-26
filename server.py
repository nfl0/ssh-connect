import os

def setup_ssh_server():
    try:
        # Install the SSH server if not already installed
        install_command = "apt-get update && apt-get install -y openssh-server"
        os.system(f"sudo {install_command}")

        # Start the SSH server
        start_command = "service ssh start"
        os.system(f"sudo {start_command}")

        # Monitor the status of the SSH server
        status_command = "service ssh status"
        status_output = os.popen(f"sudo {status_command}").read()
        print("SSH Server Status:")
        print(status_output)

        # Log the SSH server status to a file
        log_file = "/var/log/ssh_server_status.log"
        os.system(f"sudo sh -c 'echo \"{status_output}\" >> {log_file}'")

    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    setup_ssh_server()
