1. Create an Account:
   Go to the DuckDNS website (https://www.duckdns.org/) and create an account.

2. Create a Domain:
   Once you have an account, log in, and create a domain name (e.g., "yourdomainname").

3. Get Your Token:
   On the DuckDNS dashboard, you'll see your token associated with the domain you created.
   Copy this token; you'll need it in both `client.py` and `server.py` scripts.

4. Modify `client.py` and `server.py`:
   In both scripts, replace "your_dynamic_dns_domain" with the domain name you created on DuckDNS.
   Also, replace "YOUR_DUCKDNS_TOKEN" with the token you obtained from DuckDNS.

5. Run `server.py` on Your Linux Machine:
   Execute the `server.py` script on your Linux machine. This will install the SSH server, start it,
   and update the DNS record on DuckDNS with the current IP address.

6. Run `client.py` on Your Laptop:
   Execute the `client.py` script on your laptop. It will generate an SSH key pair (if not already present)
   and connect to your Linux machine using the Dynamic DNS domain and the private key.

Now, you should be able to connect to your Linux machine from your laptop using the Dynamic DNS domain name,
and the DNS record will automatically update if your IP address changes.
