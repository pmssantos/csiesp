## AP and STA Example

Big thanks to Noel Hiller to have shared this code
This is currently WORKING and tested (still some improvements to be made)

### How to use 

Upload the client on one board and the server on another board. Monitor the client and wait for CSI.

### Goal 

This sends UDP packets from one board to the other and triggers CSI callback.

### Warning

You probably want to customice the MAC filters so you don't receive frames from surrounding AP.

### Result example

![Alt text](capture.png?raw=true "Title")

## Current understanding

    CSI is a preamble to frames.
    It is used to determin the "noise" between the STA and the AP (which is assumed to be the same as the AP to the STA)
    It is a specificity of the 802.11n mode, which is enabled only under certain conditions. 
    Exemple : 

STA is sender
AP echoes    
    
1. STA send a frame to the AP at speed > 6mb/s [which is OFDM] 
2. AP respond with a frame at speed > 6 mb/s [which is OFDM]
3. The ESP32 extract the CSI header 
    
This means that to generate CSI preamble with an ESP32 you need to be connected to the AP, else you can't send at >6mb/s ans there will be no CSI preamble. 

You can't only use "esp_wifi_80211_tx" without being connected (because it will only send at 1 mb/s). So you also need to use the hidden "esp_wifi_internal_set_rate" function.

# Plan

1. Setting up client on PC
2. 
