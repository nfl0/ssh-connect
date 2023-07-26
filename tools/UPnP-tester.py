import miniupnpc

def check_upnp_availability():
    try:
        # Create a UPnP object
        upnp = miniupnpc.UPnP()

        # Discover UPnP devices on the network
        upnp.discoverdelay = 200  # Increase this value if needed
        upnp.discover()

        # Get the number of discovered UPnP devices
        devices = upnp.selectigd()
        if devices:
            print("UPnP is available on your router.")
            return True
        else:
            print("UPnP is not available on your router.")
            return False

    except Exception as ex:
        print(f"Error checking UPnP availability: {ex}")
        return False

if __name__ == "__main__":
    check_upnp_availability()
