#!/bin/bash

echo "📦 Checking dependencies..."

sudo apt update

# Install required dependencies for GTK 3 + WebKit2 + Requests
sudo apt install -y python3-gi gir1.2-gtk-3.0 gir1.2-webkit2-4.0 python3-requests \
    python3-certifi python3-charset-normalizer python3-idna

echo "🚀 Installing Simple Bitcoin Tracker..."
sudo dpkg -i simple-bitcoin-tracker_1.0.deb

echo "✅ Installation completed successfully!"
