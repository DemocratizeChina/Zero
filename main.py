from textual.app import App
from textual.widgets import Header, Footer, Button, Static
from textual.binding import Binding
from textual.containers import Container
import art

class Title(Static):
    DEFAULT_CSS = """
    Static {
        content-align: center middle;
        color: #ffffff;
    }
    """
    def compose(self):
        yield Static(art.text2art("Zero", font="random-large"))

class Description(Static):
    DEFAULT_CSS = """
    Static {
        content-align: center middle;
        color: #ffffff;
    }
    """
    def compose(self):
        

        yield Static()

class ZeroApp(App):

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]

    def action_quit(self):
        self.exit()

    def action_toggle_dark(self):
        self.dark = not self.dark

    def compose(self):
        yield Header()
        yield Title()
        # yield Footer()

ZeroApp().run()