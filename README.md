SAOLauncher
=====

![screenshot](screenshot.png)

This app is a fan-based desktop app launcher for Linux, based on Sword Art Online.

It shows an animated drop down menu to start your selected apps as Kirito uses his in-game menu in SAO.

When the command is used (or the shortcut, if set), the launcher appears in the foreground for you to start the app you want, without having to look for it.
As soon as the chosen app starts, the launcher collapses and closes itself.

Compatibility
-----

This app has been written to work on Nobara (Fedora 42) distribution.

It is made for Gnome (49) Wayland, but could be used by any Linux system.


Installation
-----

1 - Download the files.

2 - Extract the files from the archive

3 - Move the sao-launcher folder to /opt/

You may need to open the folder as admin.

4 - Install all the dependencies with this command in the terminal :

    sudo dnf install python3-gobject gtk4 gdk-pixbuf2 librsvg2


Customization
-----

You can edit the structure of the launcher as you want :

1 - Architecture of the menu

        menu_items = {
            "Gaming": {"Games": {"Steam": None, "Heroic Games Launcher": None}, "Vocal": {"Discord": None}},
            "Desktop": {"Mail": {"Thunderbird": None}, "Office Suite": {"Only Office": None}, "Scanner": {"Document Scanner": None}, "Image Editing": {"Krita": None, "Inkscape": None}, "Coding": {"Geany": None, "FileZilla": None}},
            "Web": {"Chrome": None},
            "Explorer": {"Files": None},
            "Settings": {"Input Remapper": None, "Software": None, "Extension Manager": None, "System Update": None, "Nobara Driver Manager": None, "Terminal": None, "Disks": None, "Disk Usage Analyzer": None, "System Monitor": None, "Adjustments": None, "Parameters": None},
            "Close": None
        }

In the first menu will appear : Gaming, Desktop, Web, Explorer, settings and close.

If you click Gaming, a sub-menu will open with : Games and Vocal.

If you click Games, an other sub-menu will open with : Steam and Heroic Games Launcher

You can add as many buttons as you like, following the pattern above.


2 - Definition of the button functions

    # ---------- OPEN INPUT REMAPPER ----------
    def open_remapper(self):
        try:
            subprocess.Popen(["sudo", "/usr/bin/input-remapper-gtk"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Input Remapper :", e)

    # ---------- OPEN SOFTWARE ----------
    def open_logiciels(self):
        try:
            subprocess.Popen(["gnome-software"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Software :", e)

    # ---------- OPEN EXTENSION MANAGER ----------
    def open_extensions(self):
        try:
            subprocess.Popen(["flatpak", "run", "com.mattjakeman.ExtensionManager"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Extension Manager :", e)

Depending of the way the app you want to start has been installed, you have to add a block with one of these 3 structures, from top to bottom :
- package manager
- Gnome store
- flatpak
The label has to be exactly the same as in the architecture.


3 - Call of the button functions

    def handle_menu_click(self, btn, label, children, level, parent_btn, create_floating_menu):
        if label == "Close":
            self.show_close_confirmation()
            return
        if label == "Steam":
            self.open_steam()
            return
        if label == "Heroic Games Launcher":
            self.open_heroic()
            return
        [...]
        if children:
            create_floating_menu(children, level+1, btn)
        btn.child_selected = True
        if parent_btn.triangle_widget:
            parent_btn.triangle_widget.queue_draw()
        if parent_btn.line_widget:
            parent_btn.line_widget.queue_draw()
        print(f"{label} clicked")

For each added button that should open an app, add the corresponding 3 lines as shown here to create a function stat will start the app.
The label has to be exactly the same as in the architecture.
The name of the function has to be exactly the same as in the function definition.


4 - Icon setting

        self.ICON_MAP = {
            "Gaming": "One-Handed Straight Sword.svg",
            
            "Games": "Dual Blades.svg",
            [...]
        }
        self.ICON_HOVER_MAP = {
            "Gaming": "One-Handed Straight Sword_on.svg",
            
            "Games": "Dual Blades_on.svg",
            [...]
        }
        self.ICON_ACTIVE_MAP = {
            "Gaming": "One-Handed Straight Sword_on.svg",
            
            "Games": "Dual Blades_on.svg",
            [...]
        }

Each button has 3 icons to be set :
- one base icon in self.ICON_MAP
- one hover icon in self.ICON_HOVER_MAP (visible when the mouse passes over the button)
- one active icon in self.ICON_ACTIVE_MAP (visible when you click the button)
The label has to be exactly the same as in the architecture.


Launch
-----

1 - Open your keyboard options and create a new shortcut for you to open the launcher.

2 - Set the shortcut to issue the following command :

    python3 /opt/sao-launcher/main.py

3 - Once the shortcut is set, you can use it to open the launcher at any time.


Go further
-----

For further immersion, you can install the font : SAO UI TT.

To make the launcher more visible, you can install the extension Blur my Shell, to set a blur on the background.
