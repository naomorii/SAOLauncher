#!/usr/bin/env bash

APPDIR="/opt/saolauncher"
CONFIGDIR="$HOME/.config/saolauncher"

# Suppress errors
exec 2>/dev/null

# Ask user to confirm installation
zenity --question \
--title="SAO Launcher Installer" \
--width=300 \
--text="Install SAO Launcher?"

if [ $? -eq 0 ]; then

    zenity --info --text="Installing dependencies..." --timeout=2

    # Install required dependencies
    sudo dnf install -y python3-gobject gtk4 gdk-pixbuf2 librsvg2

    zenity --info --text="Installing application..." --timeout=2

    {
        # Create app directory and copy files
        sudo mkdir -p "$APPDIR"
        sudo cp saolauncher.py "$APPDIR/"
        sudo chmod +x "$APPDIR/saolauncher.py"

        # Install desktop entry
        sudo cp saolauncher.desktop /usr/share/applications/

        # Create config directory in user's home and copy config
        sudo mkdir -p "$CONFIGDIR"
        sudo cp launcher_config.json "$CONFIGDIR/"
        sudo cp -r icons "$CONFIGDIR/"

    }

    zenity --info \
    --width=300 \
    --text="Installation completed successfully!"

fi
