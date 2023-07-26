import os
import paramiko

def generate_ssh_key():
    home_dir = os.path.expanduser("~")
    ssh_key_dir = os.path.join(home_dir, ".ssh")

    if not os.path.exists(ssh_key_dir):
        os.makedirs(ssh_key_dir)

    key_file = os.path.join(ssh_key_dir, "id_rsa")

    if not os.path.exists(key_file):
        # Generate the SSH key pair
        key = paramiko.RSAKey.generate(2048)
        with open(key_file, "w") as f:
            key.write_private_key(f)
        os.chmod(key_file, 0o600)

        public_key_file = key_file + ".pub"
        with open(public_key_file, "w") as f:
            f.write(f"{key.get_name()} {key.get_base64()}")

def ssh_connect(dynamic_dns_domain, port, username, private_key_path):
    try:
        # Use the dynamic DNS domain instead of the IP address
        hostname = dynamic_dns_domain

        # Create an SSH client instance
        ssh_client = paramiko.SSHClient()

        # Automatically add the server's host key (this is insecure, and you should use the host key verification in a production environment)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server using the private key
        ssh_client.connect(hostname, port=port, username=username, key_filename=private_key_path)

        # Example: Run a command on the remote server
        stdin, stdout, stderr = ssh_client.exec_command("uname -a")
        print("Command Output:")
        print(stdout.read().decode())

        # Close the SSH connection
        ssh_client.close()

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as ssh_ex:
        print(f"SSH connection error: {ssh_ex}")
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    # Replace these with your Dynamic DNS domain and Linux machine's credentials
    dynamic_dns_domain = "your_dynamic_dns_domain"
    ssh_port = 22  # Default SSH port is 22
    user = "your_username"

    # Generate the SSH key pair if not already present
    generate_ssh_key()

    # Use the private key path for authentication
    private_key_path = os.path.expanduser("~/.ssh/id_rsa")

    ssh_connect(dynamic_dns_domain, ssh_port, user, private_key_path)
