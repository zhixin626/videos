from manimlib import *
from manimlib.mobject.svg.old_tex_mobject import *

from custom.backdrops import *
from custom.banner import *
from custom.characters.pi_creature import *
from custom.characters.pi_creature_animations import *
from custom.characters.pi_creature_scene import *
from custom.deprecated import *
from custom.drawings import *
from custom.end_screen import *
from custom.filler import *
from custom.logo import *
from custom.opening_quote import *

# custom scene
import ctypes
from ctypes import wintypes
class InteractiveScene(InteractiveScene):
    def place_window_ontop(self):
        hwnd = self.window._window._hwnd
        user32 = ctypes.windll.user32
        SetWindowPos = user32.SetWindowPos
        SetWindowPos.argtypes = (
            wintypes.HWND,  # Handle to the window whose position is to be changed.
            wintypes.HWND,  # Handle to the window to precede the positioned window in the Z order.
            ctypes.c_int,   # X coordinate (ignored if SWP_NOMOVE flag is set).
            ctypes.c_int,   # Y coordinate (ignored if SWP_NOMOVE flag is set).
            ctypes.c_int,   # New width of the window (ignored if SWP_NOSIZE flag is set).
            ctypes.c_int,   # New height of the window (ignored if SWP_NOSIZE flag is set).
            ctypes.c_uint   # Flags that control window sizing, positioning, and visibility.
        )
        # Constants for setting window position:
        HWND_TOPMOST   = -1  # Places the window above all non-topmost windows.
        HWND_NOTOPMOST = -2  # Places the window above all non-topmost windows but below any topmost ones.
        SWP_NOSIZE     = 0x0001  # Retains the current size (ignores width and height parameters).
        SWP_NOMOVE     = 0x0002  # Retains the current position (ignores x and y parameters).
        SWP_SHOWWINDOW = 0x0040  # Displays the window.
        if not self.window._visible:
            self.window._window.maximize()
            self.window.to_default_position()
        # Bring the window to the foreground by temporarily setting it as topmost.
        SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW)
        # Remove the topmost attribute to allow normal window behavior while keeping it in front.
        SetWindowPos(hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW)
