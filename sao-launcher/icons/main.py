#!/usr/bin/env python3
import gi, os, functools, subprocess
gi.require_version("Gtk", "4.0")
gi.require_version("Gio", "2.0")
from gi.repository import Gtk, GLib, Gdk, Gio

class RPGLauncher(Gtk.Application):
    def __init__(self, triangle_width=20, triangle_height=30, button_width=160):
        super().__init__(application_id="org.example.rpglauncher")
        self.win = None
        self.floating_menus = []
        self.active_parents = []
        self.all_buttons = []
        self.main_buttons = []
        self.triangle_width = triangle_width
        self.triangle_height = triangle_height
        self.button_width = button_width
        self.MAX_VISIBLE_BUTTONS = 5
        self.FLOATING_BUTTON_HEIGHT = 40


        self.ICON_DIR = os.path.join(os.path.dirname(__file__), "icons")
        self.ICON_MAP = {
            "Gaming": "One-Handed Straight Sword.svg",
            
            "Games": "Dual Blades.svg",
            
            "Steam": "Steam.svg",
            "Heroic Games Launcher": "Heroic.png",
            
            "Vocal": "Calling.svg",
            
            "Discord": "Discord.png",
            
            "Desktop": "List.svg",
            
            "Mail": "Party & Profile.svg",
            
            "Thunderbird": "Thunderbird.png",
            
            "Office Suite": "Quest & Message Box.svg",
            
            "Only Office": "Office.png",
            
            "Web": "Searching.svg",
            
            "Chrome": "Chrome.png",
            
            "Scanner": "Details.svg",
            
            "Document Scanner": "SimpleScan.svg",
            
            "Image Editing": "Guild.svg",
            
            "Krita": "Krita.png",
            "Inkscape": "Inkscape.png",
            
            "Coding": "Dungeon Map.svg",
            
            "Geany": "Geany.png",
            "FileZilla": "Filezilla.png",
            
            "Explorer": "Items.svg",
            
            "Files": "Fichiers.svg",
            
            "Settings": "Option.svg",
            
            "Input Remapper": "Remapper.png",
            "Software": "Logiciels.png",
            "Extension Manager": "Extension.png",
            "System Update": "Update.svg",
            "Nobara Driver Manager": "Driver.svg",
            "Terminal": "Ptyxis.svg",
            "Disks": "Disque.svg",
            "Disk Usage Analyzer": "Baobab.png",
            "System Monitor": "Moniteur.svg",
            "Adjustments": "Ajustement.svg",
            "Parameters": "Paramètres.svg",
            
            "Close": "Logout.svg"
        }
        self.ICON_HOVER_MAP = {
            "Gaming": "One-Handed Straight Sword_on.svg",
            
            "Games": "Dual Blades_on.svg",
            "Vocal": "Calling_on.svg",
            
            "Desktop": "List_on.svg",
            
            "Office Suite": "Quest & Message Box_on.svg",
            
            "Mail": "Party & Profile_on.svg",
            
            "Web": "Searching_on.svg",
            
            "Scanner": "Details_on.svg",
            
            "Image Editing": "Guild_on.svg",
            
            "Coding": "Dungeon Map_on.svg",
            
            "Explorer": "Items_on.svg",
            
            "Settings": "Option_on.svg",
            
            "Close": "Logout_on.svg"
        }
        self.ICON_ACTIVE_MAP = {
            "Gaming": "One-Handed Straight Sword_on.svg",
            
            "Games": "Dual Blades_on.svg",
            "Vocal": "Calling_on.svg",
            
            "Desktop": "List_on.svg",
            
            "Office Suite": "Quest & Message Box_on.svg",
            
            "Mail": "Party & Profile_on.svg",
            
            "Web": "Searching_on.svg",
            
            "Scanner": "Details_on.svg",
            
            "Image Editing": "Guild_on.svg",
            
            "Coding": "Dungeon Map_on.svg",
            
            "Explorer": "Items_on.svg",
            
            "Settings": "Option_on.svg",
            
            "Close": "Logout_on.svg"
        }

    # ---------- OPEN STEAM ----------
    def open_steam(self):
        try:
            subprocess.Popen(["steam"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Steam :", e)

    # ---------- OPEN HEROIC GAMES LAUNCHER ----------
    def open_heroic(self):
        try:
            subprocess.Popen(["flatpak", "run", "com.heroicgameslauncher.hgl"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Heroic Games Launcher :", e)

    # ---------- OPEN DISCORD ----------
    def open_discord(self):
        try:
            subprocess.Popen(["flatpak", "run", "com.discordapp.Discord"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Discord :", e)

    # ---------- OPEN THUNDERBIRD ----------
    def open_thunderbird(self):
        try:
            subprocess.Popen(["flatpak", "run", "org.mozilla.Thunderbird"], start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Thunderbird :", e)

    # ---------- OPEN ONLY OFFICE ----------
    def open_office(self):
        try:
            subprocess.Popen(["flatpak", "run", "org.onlyoffice.desktopeditors"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Only Office :", e)

    # ---------- OPEN CHROME ----------
    def open_chrome(self):
        try:
            subprocess.Popen(["flatpak", "run", "com.google.Chrome"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Chrome :", e)

    # ---------- OPEN SCANNER ----------
    def open_scanner(self):
        try:
            subprocess.Popen(["simple-scan"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Document Scanner :", e)

    # ---------- OPEN KRITA ----------
    def open_krita(self):
        try:
            subprocess.Popen(["flatpak", "run", "org.kde.krita"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Krita :", e)

    # ---------- OPEN INKSCAPE ----------
    def open_inkscape(self):
        try:
            subprocess.Popen(["inkscape"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Inkscape :", e)

    # ---------- OPEN GEANY ----------
    def open_geany(self):
        try:
            subprocess.Popen(["flatpak", "run", "org.geany.Geany"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Geany :", e)

    # ---------- OPEN FILEZILLA ----------
    def open_filezilla(self):
        try:
            subprocess.Popen(["flatpak", "run", "org.filezillaproject.Filezilla"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening FileZilla :", e)

    # ---------- OPEN FICHIERS ----------
    def open_fichiers(self):
        try:
            subprocess.Popen(["nautilus"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Files :", e)

    # ---------- OPEN INPUT REMAPPER ----------
    def open_remapper(self):
        try:
            subprocess.Popen(["sudo", "/usr/bin/input-remapper-gtk"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Input Remapper :", e)

    # ---------- OPEN LOGICIELS ----------
    def open_logiciels(self):
        try:
            subprocess.Popen(["gnome-software"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Software :", e)

    # ---------- OPEN GESTIONNAIRE D'EXTENSIONS ----------
    def open_extensions(self):
        try:
            subprocess.Popen(["flatpak", "run", "com.mattjakeman.ExtensionManager"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Extension Manager :", e)

    # ---------- OPEN UPDATE SYSTEM ----------
    def open_update(self):
        try:
            subprocess.Popen(["sudo", "/usr/bin/nobara-updater"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening System Update :", e)

    # ---------- OPEN NOBARA DRIVER MANAGER ----------
    def open_driver(self):
        try:
            subprocess.Popen(["nobara-driver-manager"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Nobara Driver Manager :", e)

    # ---------- OPEN TERMINAL ----------
    def open_terminal(self):
        try:
            subprocess.Popen(["ptyxis"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Terminal :", e)

    # ---------- OPEN DISQUES ----------
    def open_disques(self):
        try:
            subprocess.Popen(["gnome-disks"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Disks :", e)

    # ---------- OPEN ANALYSEUR D'UTILISATION DES DISQUES ----------
    def open_utilisation(self):
        try:
            subprocess.Popen(["baobab"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Disk Usage Analyzer :", e)

    # ---------- OPEN MONITEUR SYSTEME ----------
    def open_moniteur(self):
        try:
            subprocess.Popen(["gnome-system-monitor"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            self.close_app_sequence()
        except Exception as e:
            print("Error opening System Monitor :", e)

    # ---------- OPEN AJUSTEMENTS ----------
    def open_ajustements(self):
        try:
            subprocess.Popen(["gnome-tweaks"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Ajustments :", e)

    # ---------- OPEN PARAMETRES ----------
    def open_parametres(self):
        try:
            subprocess.Popen(["gnome-control-center"])
            self.close_app_sequence()
        except Exception as e:
            print("Error opening Parameters :", e)
            
    # ---------- CLOSE CONFIRMATION WINDOW ----------
    def show_close_confirmation(self):
        fixed = self.win.get_child()

        # Full Screen Overlay
        overlay = Gtk.Fixed()
        overlay.set_size_request(self.win.get_width(), self.win.get_height())
        fixed.put(overlay, 0, 0)

        # Dialog
        dialog_width = 200
        dialog_height = 100
        dialog_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        dialog_box.set_size_request(dialog_width, dialog_height)
        dialog_box.add_css_class("confirm-box")

        # Text
        label = Gtk.Label(label="Do you want to close the menu ?")
        label.add_css_class("confirm-label")
        dialog_box.append(label)

        # Buttons
        buttons_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
        buttons_box.set_halign(Gtk.Align.CENTER)
        dialog_box.append(buttons_box)

        def create_icon_btn(icon_name, callback):
            btn = Gtk.Button()
            btn.add_css_class("icon-button")  
            btn.set_size_request(48, 48)

            # Overlay to constrain the icon size
            overlay_icon = Gtk.Overlay()
            overlay_icon.set_size_request(48, 48)

            pic = Gtk.Picture.new_for_filename(os.path.join(self.ICON_DIR, icon_name))
            pic.set_content_fit(Gtk.ContentFit.CONTAIN)   # adapt the icon to the box
            overlay_icon.set_child(pic)

            btn.set_child(overlay_icon)
            btn.connect("clicked", callback)
            return btn

        btn_on = create_icon_btn("Yes.svg", lambda *_: self.close_app_sequence())
        btn_off = create_icon_btn("No.svg", lambda *_: fixed.remove(overlay))

        buttons_box.append(btn_on)
        buttons_box.append(btn_off)

        # Centering of the dialog
        win_w = self.win.get_width()
        win_h = self.win.get_height()
        center_x = (win_w - dialog_width) // 2
        center_y = (win_h - dialog_height) // 2
        overlay.put(dialog_box, center_x, center_y)

    # ---------- FADE HOVER ----------
    def fade_hover(self, img, target_opacity, duration_ms=100):
        if not img: return
        steps = 10
        delay = duration_ms // steps
        start_opacity = img.get_opacity()
        delta = (target_opacity - start_opacity) / steps
        def step(frame=0):
            new_opacity = start_opacity + delta * frame
            img.set_opacity(new_opacity)
            if frame < steps:
                GLib.timeout_add(delay, functools.partial(step, frame+1))
            return False
        step()

    # ---------- FADE OUT ----------
    def fade_out_widget(self, widget, duration_ms=150, steps=10):
        if not widget: return
        start_opacity = getattr(widget, "get_opacity", lambda: 1.0)()
        delta = start_opacity / steps
        def step(frame=0):
            new_opacity = max(0.0, start_opacity - delta * frame)
            if hasattr(widget, "set_opacity"):
                widget.set_opacity(new_opacity)
            if frame < steps:
                GLib.timeout_add(duration_ms // steps, functools.partial(step, frame+1))
            else:
                if widget.get_parent():
                    widget.get_parent().remove(widget)
            return False
        step()

    # ---------- CREATE ICON BUTTON ----------
    def create_icon_button(self, label, icon_only=False, floating=False):
        btn = Gtk.Button()
        btn.label_str = label
        btn.is_active = False
        
        if floating:
            btn.set_size_request(self.button_width, self.FLOATING_BUTTON_HEIGHT)
    
        icon_size = 32 if floating else 48

        # Button Size
        if icon_only:
           btn.set_size_request(icon_size, icon_size)
        else:
            btn.set_size_request(self.button_width, -1)

        # ---------- Overlay ----------
        overlay = Gtk.Overlay()
        overlay.set_size_request(icon_size, icon_size)
        overlay.set_hexpand(False)
        overlay.set_vexpand(False)
        overlay.set_halign(Gtk.Align.CENTER if icon_only else Gtk.Align.START)
        overlay.set_valign(Gtk.Align.CENTER)

        # ---------- Load image helper ----------
        def load_image(file_name):
            if not file_name:
                return None

            full_path = os.path.join(self.ICON_DIR, file_name)
            if not os.path.exists(full_path):
                print(f"[Warning] Image file not found: {full_path}")
                return None

            try:
                pic = Gtk.Picture.new_for_filename(full_path)
                pic.set_content_fit(Gtk.ContentFit.CONTAIN)
                pic.set_can_shrink(True)
                pic.set_halign(Gtk.Align.CENTER)
                pic.set_valign(Gtk.Align.CENTER)
                return pic

            except Exception as e:
                print(f"[Error] Failed to load image {full_path}: {e}")
                return None

        # ----------  Base Icon ----------
        icon_path = self.ICON_MAP.get(label)
        btn.img_base = load_image(icon_path)
        if btn.img_base:
            overlay.set_child(btn.img_base)

        # ---------- Hover Icon ----------
        icon_hover_path = self.ICON_HOVER_MAP.get(label)
        btn.img_hover = load_image(icon_hover_path)
        if btn.img_hover:
            btn.img_hover.set_opacity(0.0)
            overlay.add_overlay(btn.img_hover)

        # ---------- Frame contraint (FIX GTK4 SIZE) ----------
        frame = Gtk.Box()
        frame.set_size_request(icon_size, icon_size)
        frame.set_halign(Gtk.Align.CENTER)
        frame.set_valign(Gtk.Align.CENTER)
        frame.append(overlay)

        # ---------- Button Construction ----------
        if not icon_only:
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
            box.append(frame)
            box.append(Gtk.Label(label=label, xalign=0))
            btn.set_child(box)
        else:
            btn.set_child(frame)

        # ---------- Hover ----------
        if btn.img_hover:
            pointer = Gtk.EventControllerMotion.new()
            btn.add_controller(pointer)

            pointer.connect(
                "enter",
                lambda *args: self.fade_hover(btn.img_hover, 1.0) if not btn.is_active else None
            )
            pointer.connect(
                "leave",
                lambda *args: self.fade_hover(btn.img_hover, 0.0) if not btn.is_active else None
            )

        btn.child_selected = False
        btn.children_dict = None
        btn.triangle_widget = None
        btn.line_widget = None

        return btn

    # ---------- UPDATE ICON STATE ----------
    def set_button_icon_state(self, btn, state="normal"):
        if state=="active":
            btn.is_active = True
            if btn.img_hover: self.fade_hover(btn.img_hover,0.0)
            icon_path = self.ICON_ACTIVE_MAP.get(btn.label_str, self.ICON_MAP.get(btn.label_str))
            if icon_path and btn.img_base:
                full_path = os.path.join(self.ICON_DIR, icon_path)
                if os.path.exists(full_path): btn.img_base.set_filename(full_path)
        else:
            btn.is_active = False
            icon_path = self.ICON_MAP.get(btn.label_str)
            if icon_path and btn.img_base:
                full_path = os.path.join(self.ICON_DIR, icon_path)
                if os.path.exists(full_path): btn.img_base.set_filename(full_path)

    # ---------- CLOSE APP SEQUENCE ----------
    def close_app_sequence(self):
        fixed = self.win.get_child()
        for menu in self.floating_menus:
            for btn in menu:
                self.fade_out_widget(btn)
        for btn in self.active_parents:
            self.fade_out_widget(btn.triangle_widget)
            self.fade_out_widget(btn.line_widget)

        def animate_main_contract(index=None):
            if index is None:
                index = len(self.main_buttons) - 1
            if index < 0:
                GLib.timeout_add(200, self.quit)
                return False
            btn, _ = self.main_buttons[index]
            start_y = btn.translate_coordinates(fixed, 0, 0)[1]
            steps = 12
            def animate(b, frame=0):
                progress = 1 - frame / steps
                new_y = start_y - 64 * (1 - progress)
                b.set_opacity(progress)
                fixed.move(b, b.translate_coordinates(fixed,0,0)[0], int(new_y))
                if frame < steps:
                    GLib.timeout_add(25, lambda: animate(b, frame+1))
            animate(btn)
            GLib.timeout_add(75, lambda: animate_main_contract(index-1))
        GLib.timeout_add(50, animate_main_contract)

    # ---------- HANDLE MENU CLICK ----------
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
        if label == "Discord":
            self.open_discord()
            return
        if label == "Thunderbird":
            self.open_thunderbird()
            return
        if label == "Only Office":
            self.open_office()
            return
        if label == "Chrome":
            self.open_chrome()
            return
        if label == "Document Scanner":
            self.open_scanner()
            return
        if label == "Krita":
            self.open_krita()
            return
        if label == "Inkscape":
            self.open_inkscape()
            return
        if label == "Geany":
            self.open_geany()
            return
        if label == "FileZilla":
            self.open_filezilla()
            return
        if label == "Files":
            self.open_fichiers()
            return
        if label == "Input Remapper":
            self.open_remapper()
            return
        if label == "Software":
            self.open_logiciels()
            return
        if label == "Extension Manager":
            self.open_extensions()
            return
        if label == "System Update":
            self.open_update()
            return
        if label == "Nobara Driver Manager":
            self.open_driver()
            return
        if label == "Terminal":
            self.open_terminal()
            return
        if label == "Disks":
            self.open_disques()
            return
        if label == "Disk Usage Analyzer":
            self.open_utilisation()
            return
        if label == "System Monitor":
            self.open_moniteur()
            return
        if label == "Adjustments":
            self.open_ajustements()
            return
        if label == "Parameters":
            self.open_parametres()
            return
        if children:
            create_floating_menu(children, level+1, btn)
        btn.child_selected = True
        if parent_btn.triangle_widget:
            parent_btn.triangle_widget.queue_draw()
        if parent_btn.line_widget:
            parent_btn.line_widget.queue_draw()
        print(f"{label} clicked")

    # ---------- ACTIVATE APPLICATION ----------
    def do_activate(self):
        if self.win:
            self.win.present()
            return

        self.win = Gtk.ApplicationWindow(application=self)
        self.win.set_title("Launcher")
        self.win.set_default_size(1920,1080)
        self.win.set_resizable(False)
        self.win.set_decorated(False)
        key_controller = Gtk.EventControllerKey()
        key_controller.connect("key-pressed", self.on_key_press)
        self.win.add_controller(key_controller)

        # ---------- CSS ----------
        css = Gtk.CssProvider()
        css.load_from_data(b"""
            window { background-color: rgba(0,0,0,0.01); font-size: 18px; letter-spacing: 1px; }
            * { font-family: "SAO UI TT"; }
            button { background: rgba(230,230,230,1); color: black; border:none; border-radius:0px ; padding:5px 20px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.35)); transition: all 0.1s ease; }
            button:hover { background: white; }
            button.inactive-parent { opacity:0.5; }
            button.inactive-parent:hover { opacity:1; background:white; }
            button.active-parent { background: rgba(235,166,1,1); color:white; font-weight:bold; }
            image { opacity:1; }
            button.main-icon-button { background: transparent; border: none; padding: 0; border-radius: 50%; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.35)); transition: all 0.1s ease; }
            .tooltip-label { background-color: rgba(50,50,50,1); color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; box-shadow: 0 0 6px 1px rgba(255,255,255,0.35); transition: opacity 0.1s ease; }
            .invisible-scrollbar scrollbar { min-width:0; min-height:0; background-color:transparent; border:none; }
            .invisible-scrollbar scrollbar slider { background-color: transparent; border:none; }
            .confirm-box { background-color: rgba(255,255,255,1); padding: 20px; }
            .confirm-label { font-size: 18px; font-weight: bold; color: black; }
            .icon-button { background: transparent; border: none; box-shadow: none; padding: 0; min-width: 0px; min-height: 0px; border-radius: 50%; }
        """)
        Gtk.StyleContext.add_provider_for_display(self.win.get_display(), css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        fixed = Gtk.Fixed()
        self.win.set_child(fixed)

        # ---------- MENU ITEMS ----------
        menu_items = {
            "Gaming": {"Games": {"Steam": None, "Heroic Games Launcher": None}, "Vocal": {"Discord": None}},
            "Desktop": {"Mail": {"Thunderbird": None}, "Office Suite": {"Only Office": None}, "Scanner": {"Document Scanner": None}, "Image Editing": {"Krita": None, "Inkscape": None}, "Coding": {"Geany": None, "FileZilla": None}},
            "Web": {"Chrome": None},
            "Explorer": {"Files": None},
            "Settings": {"Input Remapper": None, "Software": None, "Extension Manager": None, "System Update": None, "Nobara Driver Manager": None, "Terminal": None, "Disks": None, "Disk Usage Analyzer": None, "System Monitor": None, "Adjustments": None, "Parameters": None},
            "Close": None
        }

        # ---------- UTILS ----------
        def update_opacity():
            for btn in self.all_buttons:
                if btn in self.active_parents:
                    btn.remove_css_class("inactive-parent")
                else:
                    btn.add_css_class("inactive-parent")

        def has_active_descendant(btn):
            if not btn.children_dict: return False
            for child_btn, grandchildren in btn.children_dict.items():
                if child_btn.child_selected: return True
                if has_active_descendant(child_btn): return True
            return False

        def clear_floating_from(level):
            for btn in self.active_parents[level:]:
                btn.remove_css_class("active-parent")
                btn.child_selected = False
                btn.is_active = False
                self.set_button_icon_state(btn,"normal")
                self.fade_out_widget(btn.line_widget)
                btn.line_widget = None
                self.fade_out_widget(btn.triangle_widget)
                btn.triangle_widget = None
            self.active_parents[level:] = []

            for menu in self.floating_menus[level:]:
                for b in menu:
                    self.fade_out_widget(b)
            self.floating_menus[level:] = []
            update_opacity()

        # ---------- TOOLTIP ----------
        tooltip_label = Gtk.Label()
        tooltip_label.add_css_class("tooltip-label")
        tooltip_label.set_opacity(0.0)
        tooltip_label.set_can_focus(False)
        tooltip_label.set_can_target(False)
        tooltip_label.set_sensitive(False)
        fixed.put(tooltip_label, 0, 0)
        tooltip_label.set_visible(True)

        def show_tooltip(text, b):
            tooltip_label.set_text(text)
            tooltip_label.set_opacity(1.0)
            tooltip_label.queue_resize()
            tw, th = tooltip_label.get_preferred_size().natural_size.width, tooltip_label.get_preferred_size().natural_size.height
            px, py = b.translate_coordinates(fixed, 0, 0)
            tooltip_x = px + (b.get_width() - tw)//2
            tooltip_y = py - th - 8
            if tooltip_label.get_parent():
                tooltip_label.get_parent().remove(tooltip_label)
            fixed.put(tooltip_label, tooltip_x, tooltip_y)

        # ---------- CREATE DRAW WIDGET ----------
        def create_draw_widget(parent_btn, wtype="triangle", height=0):
            area = Gtk.DrawingArea()
            if wtype=="triangle":
                area.set_content_width(self.triangle_width)
                area.set_content_height(self.triangle_height)
            else:
                area.set_content_width(2)
                area.set_content_height(height)
            area.parent_btn = parent_btn
            def draw(area, cr, dw, dh):
                btn = area.parent_btn
                shadow_alpha = 0.03 if wtype=="triangle" else 0.025
                steps = 5
                for i in range(1, steps+1):
                    alpha = shadow_alpha*(1-(i-1)/steps)
                    for dx in (-i,0,i):
                        for dy in (-i,0,i):
                            if dx==0 and dy==0: continue
                            cr.set_source_rgba(0,0,0,alpha)
                            cr.set_line_width(1.5)
                            if wtype=="triangle":
                                cr.move_to(0+dx, dh/2+dy)
                                cr.line_to(dw+dx, dh/2-10+dy)
                                cr.line_to(dw+dx, dh/2+10+dy)
                                cr.close_path()
                                cr.fill()
                            else:
                                cr.move_to(0+dx, 0+dy)
                                cr.line_to(0+dx, dh+dy)
                                cr.stroke()
                active = has_active_descendant(btn)
                color_main = (1,0.7,0.15,1) if active else (1,1,1,1)
                if wtype=="triangle":
                    cr.set_source_rgba(*color_main)
                    cr.move_to(0, dh/2)
                    cr.line_to(dw, dh/2-10)
                    cr.line_to(dw, dh/2+10)
                    cr.close_path()
                    cr.fill()
                    circle_radius = 3
                    color_circle = (1,0.7,0.15,1) if active else (0.7,0.7,0.7,1)
                    cr.set_source_rgba(*color_circle)
                    cr.arc(dw*0.65, dh/2, circle_radius, 0, 2*3.1416)
                    cr.fill()
                else:
                    cr.set_source_rgba(*color_main)
                    cr.set_line_width(1)
                    cr.move_to(0,0)
                    cr.line_to(0,dh)
                    cr.stroke()
            area.set_draw_func(draw)
            return area

        # ---------- CREATE FLOATING MENU ----------
        def create_floating_menu(items, level, parent_btn):
            clear_floating_from(level)
            parent_btn.add_css_class("active-parent")
            parent_btn.is_active = True
            self.active_parents.append(parent_btn)
            self.set_button_icon_state(parent_btn,"active")
            update_opacity()
            parent_btn.children_dict = {}

            px, py = parent_btn.translate_coordinates(fixed, 0, 0)
            pw, ph = parent_btn.get_width(), parent_btn.get_height()
            triangle_x = px + pw + 12
            triangle_y = py + ph // 2

            buttons = []
            spacing = 3
            for label, children in items.items():
                btn = self.create_icon_button(label, floating=True)
                btn.hovered = False
                buttons.append(btn)
                self.all_buttons.append(btn)
                parent_btn.children_dict[btn] = children

                pointer = Gtk.EventControllerMotion.new()
                btn.add_controller(pointer)
                pointer.connect("enter", lambda *args, b=btn: setattr(b,"hovered",True) or b.set_opacity(1.0))
                pointer.connect("leave", lambda *args, b=btn: setattr(b,"hovered",False) or (update_opacity_scroll() if update_opacity_scroll else None))

                btn.connect("clicked", lambda b=btn,l=label,c=children: self.handle_menu_click(b,l,c,level,parent_btn,create_floating_menu))

            self.floating_menus.append(buttons)

            # ---------- Triangle ----------
            triangle = create_draw_widget(parent_btn,"triangle")
            fixed.put(triangle, triangle_x, triangle_y - self.triangle_height//2)
            parent_btn.triangle_widget = triangle

            # ---------- Container ----------
            container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=spacing)
            button_height = self.FLOATING_BUTTON_HEIGHT
            update_opacity_scroll = None
            line_height = sum([button_height + spacing for _ in buttons])

            if len(buttons) > self.MAX_VISIBLE_BUTTONS:
                # Placeholders for scroll
                for _ in range(2):
                    ph = Gtk.Label()
                    ph.set_size_request(1, button_height)
                    container.append(ph)

                for btn in buttons:
                    container.append(btn)

                for _ in range(2):
                    ph = Gtk.Label()
                    ph.set_size_request(1, button_height)
                    container.append(ph)

                # Scrollable
                scroll = Gtk.ScrolledWindow()
                scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
                scroll.set_overlay_scrolling(False)
                scroll.add_css_class("invisible-scrollbar")
                scroll.set_propagate_natural_height(False)
                scroll.set_propagate_natural_width(False)
                scroll.set_child(container)
                scroll_height = self.MAX_VISIBLE_BUTTONS * button_height + (spacing*self.MAX_VISIBLE_BUTTONS-1)
                scroll.set_size_request(self.button_width, scroll_height)
                fixed.put(scroll, triangle_x + self.triangle_width + 5, triangle_y - scroll_height//2)
                line_height = scroll_height

                adjustment = scroll.get_vadjustment()

                # Function to set Opacity
                def update_opacity_scroll(*args):
                    scroll_y = adjustment.get_value()
                    for i, btn in enumerate(list(container)):
                        if getattr(btn,"hovered",False) or getattr(btn,"is_active",False):
                            btn.set_opacity(1.0)
                            continue
                        btn_y = i * (button_height + spacing) - scroll_y
                        btn_h = button_height
                        center = scroll_height / 2
                        btn_center = btn_y + btn_h / 2
                        dist = abs(center - btn_center)
                        max_dist = scroll_height / 2
                        t = dist / max_dist
                        alpha = max(0.0, 1 - t**2)
                        btn.set_opacity(alpha)
                    return True

                adjustment.connect("value-changed", update_opacity_scroll)

                # Initial offset to hide the top placeholders
                initial_scroll = (button_height + spacing) * 2

                def set_initial_scroll():
                    adjustment.set_value(initial_scroll)
                    update_opacity_scroll()
                    return False  # run one time only

                GLib.idle_add(set_initial_scroll)

            else:
                for btn in buttons:
                    container.append(btn)
                fixed.put(container, triangle_x + self.triangle_width + 5, triangle_y - line_height//2)

            # ---------- Vertical line ----------
            if not parent_btn.line_widget:
                line = create_draw_widget(parent_btn,"line", line_height)
                fixed.put(line, triangle_x + self.triangle_width, triangle_y - line_height//2)
                parent_btn.line_widget = line
                
        def get_max_depth(menu_dict, level=1):
            if not isinstance(menu_dict, dict) or not menu_dict:
                return level

            depths = [
                get_max_depth(v, level + 1)
                for v in menu_dict.values()
                if isinstance(v, dict) and v
            ]

            if not depths:
                return level

            return max(depths)


        max_depth = get_max_depth(menu_items)
        
        screen_width = self.win.get_display().get_monitors()[0].get_geometry().width
        
        main_button_width = 48  # icon_only
        submenu_block_width = self.triangle_width + 5 + self.button_width + 12

        total_launcher_width = main_button_width + (max_depth * submenu_block_width)

        # ---------- MAIN MENU ----------
        x_start = (screen_width - total_launcher_width) // 2
        main_spacing = 64

        # Window height
        win_height = self.win.get_default_size()[1]

        # Force a temporary for GTK to set the sizes
        for label, children in menu_items.items():
            btn = self.create_icon_button(label, icon_only=True)
            btn.add_css_class("main-icon-button")
            btn.set_visible(False)
            self.all_buttons.append(btn)
            self.main_buttons.append((btn, children))
            fixed.put(btn, x_start, 0)

        # Real button size setting
        self.win.set_visible(True)
        self.win.present()

        total_height = 0
        button_heights = []

        for btn, _ in self.main_buttons:
            btn.set_visible(True)
            self.win.queue_resize()
            h = btn.get_preferred_size().natural_size.height
            button_heights.append(h)
            total_height += h

        total_height += main_spacing * (len(self.main_buttons) - 1)

        # Centered Y position
        y_start = (win_height - total_height) // 2

        # Definitive placement
        y_offset = 0
        for index, (btn, children) in enumerate(self.main_buttons):
            current_label = btn.label_str

            btn.set_visible(False)
            fixed.move(btn, x_start, y_start + y_offset)
            y_offset += button_heights[index] + main_spacing

            pointer = Gtk.EventControllerMotion.new()
            btn.add_controller(pointer)
            pointer.connect("enter", lambda c,x,y,b=btn: show_tooltip(b.label_str,b))
            pointer.connect("leave", lambda *args: tooltip_label.set_opacity(0.0))

            if children:
                btn.connect(
                    "clicked",
                    lambda b=btn, c=children: create_floating_menu(c, 0, b)
                )
            else:
                btn.connect(
                    "clicked",
                    lambda b=btn, l=current_label: self.handle_menu_click(b, l, None, 0, b, None)
               )

        # ---------- CASCADING ANIMATION ----------
        def animate_button(btn, start_y, target_y, steps=12, step_delay=25, frame=0):
            progress = frame / steps
            new_y = start_y + (target_y - start_y) * progress
            btn.set_opacity(progress)
            fixed.move(btn, x_start, int(new_y))
            if frame < steps:
                GLib.timeout_add(step_delay, functools.partial(animate_button, btn, start_y, target_y, steps, step_delay, frame + 1))
            return False

        def animate_main_menu_cascade():
            # Real window height (Wayland safe)
            win_height = self.win.get_height()

            main_spacing = 64

            # Real total height setting
            total_height = 0
            button_heights = []

            for btn, _ in self.main_buttons:
                btn.set_visible(True)
                h = btn.get_height()
                button_heights.append(h)
                total_height += h

            total_height += main_spacing * (len(self.main_buttons) - 1)

            # Real vertical centering
            y_start = (win_height - total_height) // 2

            # Animation
            y_offset = 0
            delay_per_btn = 0

            for index, (btn, children) in enumerate(self.main_buttons):
                target_y = y_start + y_offset
                y_offset += button_heights[index] + main_spacing

                start_y = target_y - 64
                btn.set_opacity(0.0)
                fixed.move(btn, 50, start_y)

                GLib.timeout_add(
                    delay_per_btn,
                    functools.partial(animate_button, btn, start_y, target_y)
                )

                delay_per_btn += 100

            return False

        GLib.timeout_add(50, animate_main_menu_cascade)
        self.win.present()

    # ---------- KEY PRESS ----------
    def on_key_press(self, controller, keyval, keycode, state):
        if keyval == Gdk.KEY_Escape:
            self.close_app_sequence()
            return True
        return False

# ---------- RUN APP ----------
if __name__ == "__main__":
    app = RPGLauncher()
    app.run()
