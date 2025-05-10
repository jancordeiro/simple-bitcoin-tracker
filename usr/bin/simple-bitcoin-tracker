#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib, Gdk
import requests
from datetime import datetime
import webbrowser

class BitcoinTracker(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.simple.BitcoinTracker")
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = Gtk.ApplicationWindow(application=self)
            self.window.set_title("Simple Bitcoin Tracker")
            self.window.set_default_size(550, 500)

            self.apply_css()

            notebook = Gtk.Notebook()
            self.window.set_child(notebook)

            # Tracker tab
            self.price_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.price_box.set_name("price-box")

            self.labels = {
                "usd": Gtk.Label(label=""),
                "eur": Gtk.Label(label=""),
                "brl": Gtk.Label(label=""),
                "market_cap": Gtk.Label(label="")
            }

            for lbl in self.labels.values():
                lbl.set_name("price-label")
                self.price_box.append(lbl)

            self.last_update_label = Gtk.Label(label="Last update: —")
            self.last_update_label.set_name("update-label")

            refresh_button = Gtk.Button(label="Refresh")
            refresh_button.connect("clicked", self.refresh_data)

            donate_button = Gtk.Button(label="Donate")
            donate_button.connect("clicked", lambda b: webbrowser.open("https://jancordeiro.github.io/donate"))

            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10, margin_top=15)

            # Imagem
            image = Gtk.Picture.new_for_filename("/usr/share/pixmaps/screen-01.png")
            image.set_content_fit(Gtk.ContentFit.SCALE_DOWN)
            image.set_size_request(400, 148)
            box.append(image)

            # Conteúdo da aba Tracker
            box.append(self.price_box)
            box.append(self.last_update_label)
            box.append(refresh_button)
            box.append(donate_button)

            tab_tracker = Gtk.ScrolledWindow()
            tab_tracker.set_child(box)
            notebook.append_page(tab_tracker, Gtk.Label(label="Tracker"))

            # Info tab
            info_text = (
                "Simple Bitcoin Tracker\n"
                "Version: 1.0\n"
                "Author: Jan Cordeiro\n"
                "Website: https://jancordeiro.github.io"
            )

            info_label = Gtk.Label(label=info_text)
            info_label.set_justify(Gtk.Justification.LEFT)
            info_label.set_wrap(True)
            info_label.set_name("info-label")

            info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            info_box.set_margin_top(10)
            info_box.set_margin_bottom(10)
            info_box.set_margin_start(5)
            info_box.set_margin_end(5)
            info_box.append(info_label)

            notebook.append_page(info_box, Gtk.Label(label="Info"))

            self.refresh_data()

        self.window.present()

    def refresh_data(self, *_):
        try:
            res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur,brl&include_market_cap=true&include_24hr_change=true")
            data = res.json()["bitcoin"]
            self.labels["usd"].set_label(f"USD: ${data['usd']:.2f} ({data['usd_24h_change']:.2f}% 24h)")
            self.labels["eur"].set_label(f"EUR: €{data['eur']:.2f} ({data['eur_24h_change']:.2f}% 24h)")
            self.labels["brl"].set_label(f"BRL: R${data['brl']:.2f} ({data['brl_24h_change']:.2f}% 24h)")
            self.labels["market_cap"].set_label(f"Market Cap: ${data['usd_market_cap'] / 1e9:.2f} B")
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.last_update_label.set_label(f"Last update: {now}")
        except Exception as e:
            self.labels["usd"].set_label(f"Error fetching data: {e}")

    def apply_css(self):
        css = b"""
        window {
            background-color: #0f0f1a;
        }
        #price-label {
            font-size: 18px;
            color: #00ffcc;
        }
        #update-label {
            font-size: 12px;
            color: #8888aa;
        }
        button {
            background: #222244;
            color: #00ffcc;
        }
        button:hover {
            background: #333366;
        }
        #info-label {
            font-size: 16px;
            font-family: "Monospace";
            color: #39ff14;
            background-color: #1a1a2f;
            padding: 10px;
        }
        """

        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(css)

        display = Gdk.Display.get_default()
        Gtk.StyleContext.add_provider_for_display(display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

app = BitcoinTracker()
app.run()
