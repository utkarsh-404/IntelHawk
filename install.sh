#!/bin/bash
echo "Installing IntelHawk dependencies..."
sudo apt update
sudo apt install -y \
    nmap \
    sublist3r \
    whatweb \
    git \
    python3-pip \
    python3-nmap
# Install Breach-Checker
https://github.com/x404xx/Breach-Checker
cd Breach-Checker
pip install -r requirements.txt
cd ..
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
pip install -r requirements.txt
cd ..

pip install -r requirements.txt
echo "Installation complete! Run with: python app.py"
