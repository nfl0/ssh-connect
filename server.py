import os
import paramiko

def setup_ssh_server(dynamic_dns_domain):
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


        # Update the DNS record with the dynamic DNS service (e.g., DuckDNS)
        update_dns_command = f"curl 'https://www.duckdns.org/update?domains={dynamic_dns_domain}&token=YOUR_DUCKDNS_TOKEN&ip='"
        os.system(update_dns_command)

    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    # Replace this with your Dynamic DNS domain
    dynamic_dns_domain = "your_dynamic_dns_domain"

    setup_ssh_server(dynamic_dns_domain)
