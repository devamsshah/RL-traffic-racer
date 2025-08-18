#!/bin/zsh
DEVTYPE="com.apple.CoreSimulator.SimDeviceType.iPhone-15-Pro"
RUNTIME="com.apple.CoreSimulator.SimRuntime.iOS-18-0"
COUNT=4

# 1. Make devices
for i in $(seq 1 $COUNT); do
  UDID=$(xcrun simctl create "RLPhone$i" "$DEVTYPE" "$RUNTIME")
  UDIDS+=($UDID)
done

# 2. Boot & open windows
for UDID in "${UDIDS[@]}"; do
  xcrun simctl boot "$UDID"
  open -n "$(xcrun -f Simulator)" --args -CurrentDeviceUDID "$UDID" &
done

