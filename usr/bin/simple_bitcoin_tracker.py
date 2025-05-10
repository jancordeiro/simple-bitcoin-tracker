import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib
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
            self.window.set_default_size(400, 300)

            notebook = Gtk.Notebook()
            self.window.set_child(notebook)

            # Tracker tab
            self.price_label = Gtk.Label(label="Fetching data...")
            self.last_update_label = Gtk.Label(label="Last update: —")

            refresh_button = Gtk.Button(label="Refresh")
            refresh_button.connect("clicked", self.refresh_data)

            donate_button = Gtk.Button(label="Donate")
            donate_button.connect("clicked", lambda b: webbrowser.open("https://jancordeiro.github.io/donate"))

            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10, margin_top=15)
            box.append(self.price_label)
            box.append(self.last_update_label)
            box.append(refresh_button)
            box.append(donate_button)

            tab_tracker = Gtk.ScrolledWindow()
            tab_tracker.set_child(box)
            notebook.append_page(tab_tracker, Gtk.Label(label="Tracker"))

            # Info tab
            info_text = (
                "Simple Bitcoin Tracker\n\n"
                "Version: 1.0\n"
                "Author: Jan Cordeiro\n"
                "Website: https://jancordeiro.github.io\n"
                "Donate: https://jancordeiro.github.io/donate"
            )
            info_label = Gtk.Label(label=info_text)
            notebook.append_page(info_label, Gtk.Label(label="Info"))

            self.refresh_data()

        self.window.present()

    def refresh_data(self, *_):
        try:
            res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur,brl&include_market_cap=true&include_24hr_change=true")
            data = res.json()["bitcoin"]
            text = (
                f"USD: ${data['usd']:.2f} ({data['usd_24h_change']:.2f}% 24h)\n"
                f"EUR: €{data['eur']:.2f} ({data['eur_24h_change']:.2f}% 24h)\n"
                f"BRL: R${data['brl']:.2f} ({data['brl_24h_change']:.2f}% 24h)\n"
                f"Market Cap (USD): ${data['usd_market_cap'] / 1e9:.2f} B"
            )
            self.price_label.set_label(text)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.last_update_label.set_label(f"Last update: {now}")
        except Exception as e:
            self.price_label.set_label(f"Error fetching data: {e}")

app = BitcoinTracker()
app.run()
