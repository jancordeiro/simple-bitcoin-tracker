#!/bin/bash

APP_NAME="simple-bitcoin-tracker"
VERSION="1.0"

echo "📦 Building $APP_NAME .deb package..."

# Define permissions
chmod 755 $APP_NAME/usr/bin/install-simple-bitcoin-tracker.sh
chmod 755 $APP_NAME/usr/bin/simple-bitcoin-tracker
chmod 644 $APP_NAME/usr/share/applications/simple-bitcoin-tracker.desktop
chmod 644 $APP_NAME/usr/share/pixmaps/simple-bitcoin-tracker.png

# Cria o pacote .deb
dpkg-deb --build "$APP_NAME"

# Renomeia com versão
mv "${APP_NAME}.deb" "${APP_NAME}_${VERSION}.deb"

echo "✅ Package created: ${APP_NAME}_${VERSION}.deb"
