#!/usr/bin/env python3

import time
import subprocess

# Define a list of pools and coins to be mined
pools_and_coins = [
    {"pool": "stratum+tcp://pool1.com", "coin": "Coin ABC", "duration": 20},
    {"pool": "stratum+tcp://pool2.com", "coin": "Coin XYZ", "duration": 60},
    {"pool": "stratum+tcp://pool3.com", "coin": "Coin AAA", "duration": 30}
]

# Set the current pool and coin to be mined
current_pool_and_coin = pools_and_coins[0]

# Function to switch to the next pool and coin
def switch_pool_and_coin():
    global current_pool_and_coin, pools_and_coins
    current_index = pools_and_coins.index(current_pool_and_coin)
    if current_index == len(pools_and_coins) - 1:
        current_pool_and_coin = pools_and_coins[0]
    else:
        current_pool_and_coin = pools_and_coins[current_index + 1]

# Main loop
while True:
    print("Mining " + current_pool_and_coin["coin"] + " at " + current_pool_and_coin["pool"])

    # Start the mining process for the current pool and coin
    subprocess.run(["miner_command", "-o", current_pool_and_coin["pool"], "-u", "username", "-p", "password"])

    # Wait for the specified duration
    time.sleep(current_pool_and_coin["duration"] * 60)

    # Switch to the next pool and coin
    switch_pool_and_coin()

    # Wait for 5 minutes before restarting the mining process for the current pool and coin
    time.sleep(5 * 60)
            
# End of program
# d:\Mehedi Hasan\Cloud\One Drive\OneDrive\Programming\AI\Mining\mining.py (python) 
#!/usr/bin/
import time;
import subprocess
    
