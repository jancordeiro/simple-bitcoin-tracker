#!/bin/bash

echo "📦 Checking dependencies..."

sudo apt update

# Install required dependencies
sudo apt install -y gir1.2-gtk-4.0 python3-requests \
    gir1.2-graphene-1.0 python3-certifi python3-charset-normalizer \
    python3-idna python3-chardet

echo "🚀 Installing Simple Bitcoin Tracker..."
sudo dpkg -i simple-bitcoin-tracker.deb

# Check if icon file exists
ICON_NAME="simple-bitcoin-tracker.png"
if [ -f "$ICON_NAME" ]; then
    echo "📁 Installing icon to /usr/share/pixmaps/..."
    sudo cp "$ICON_NAME" /usr/share/pixmaps/
else
    echo "⚠️ File $ICON_NAME not found! Icon was not installed."
fi

echo "✅ Installation completed successfully!"
