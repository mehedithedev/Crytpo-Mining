#!/bin/bash

# Define the list of pools and coins
pools=(
  "stratum+tcp://pool1.com 20 ABC"
  "stratum+tcp://pool2.com 60 XYZ"
  "stratum+tcp://pool3.com 30 AAA"
)

# Port number to listen on
port=3333

# Loop through the list of pools and coins
for pool in "${pools[@]}"; do
  # Split the pool information into separate variables
  IFS=' ' read -r -a pool_info <<< "$pool"
  address="${pool_info[0]}"
  duration="${pool_info[1]}"
  coin="${pool_info[2]}"

  # Connect to the pool and mine the coin for the specified duration
  echo "Connecting to pool $address for $duration minutes to mine $coin"
  # Start a stratum proxy on the specified port, forwarding connections to the pool
  # Replace $address with the actual pool address and $port with the desired port number
  ./stratum-proxy -o $address -p $port &

  # Pause the script for the specified duration before moving on to the next pool
  sleep $((duration * 60))

  # Kill the stratum proxy process
  kill $!
done
