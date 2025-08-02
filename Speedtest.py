import speedtest as st

def speed_test():
    
    print("Running speed test, please wait... ")
    
    # Initialize the speedtest client
    test = st.Speedtest()
    
    # Get the best server based on ping
    print("Finding the best server...")
    test.get_best_server()
    
    # Test download speed
    print("Testing download speed...")
    down_speed = test.download()
    down_speed_mbps = round(down_speed / 10**6, 2)
    print(f"Download Speed: {down_speed_mbps} Mbps ")
    
    # Test upload speed
    print("Testing upload speed...")
    up_speed = test.upload()
    up_speed_mbps = round(up_speed / 10**6, 2)
    print(f"Upload Speed: {up_speed_mbps} Mbps ")
    
    # Get the ping
    ping = test.results.ping
    print(f"Ping: {ping} ms 핑")

# Run the function
if __name__ == "__main__":
    speed_test()