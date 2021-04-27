#!/bin/bash
#usage : bubble pwn_file
sudo chmod +x $1
touch $1.py
echo "[+]Touch Successful!"
sudo subl $1.py
sudo chmod +777 $1.py
template $1 > $1.py
echo "Over"