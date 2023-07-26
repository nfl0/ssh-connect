import os
import subprocess

def install_ssh_client():
    try:
        # Install the SSH client if not already installed
        install_command = "sudo apt-get update && sudo apt-get install -y openssh-client"
        subprocess.run(install_command, shell=True, check=True)
    except Exception as ex:
        print(f"Error installing SSH client: {ex}")

def setup_ssh_client():
    try:
        # Check if the SSH client is already installed
        ssh_client_installed = False
        try:
            subprocess.run(["which", "ssh"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            ssh_client_installed = True
        except subprocess.CalledProcessError:
            pass

        if not ssh_client_installed:
            print("SSH client not installed. Installing SSH client...")
            install_ssh_client()

        # Attempt to SSH into the server
        server_hostname = "inserthostname.noip.xx"  # Replace this with your server hostname
        ssh_command = f"ssh {server_hostname}"

        print("Attempting to SSH into the server...")
        os.system(ssh_command)

        # Check if SSH keys are set up for passwordless login
        public_key_path = os.path.expanduser("~/.ssh/id_rsa.pub")
        if not os.path.exists(public_key_path):
            print("Generating SSH key pair...")
            ssh_keygen_command = "ssh-keygen -f ~/.ssh/id_rsa -q -N ''"
            subprocess.run(ssh_keygen_command, shell=True, check=True)

        # Copy public key to the server for passwordless login
        print("Copying public key to the server...")
        copy_key_command = f"ssh-copy-id {server_hostname}"
        subprocess.run(copy_key_command, shell=True, check=True)

        print("Passwordless SSH setup is complete. You can now SSH into the server without a password.")
        print(f"To SSH into the server, use: ssh user@{server_hostname}")

    except Exception as ex:
        print(f"Error setting up SSH client: {ex}")

if __name__ == "__main__":
    setup_ssh_client()
