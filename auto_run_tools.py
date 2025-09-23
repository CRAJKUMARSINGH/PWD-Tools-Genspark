"""
Automation: Open each PWD tool three times and capture screenshots of landing views.

Notes:
- Uses tkinter's `after` scheduling to allow UI to render before screenshot.
- Saves screenshots under screenshots/<tool_name>/run_<n>.png
"""

import os
import time
from pathlib import Path

import customtkinter as ctk

from main import PWDToolsApp


def ensure_dir(path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)


def save_root_screenshot(root: ctk.CTk, out_path: Path) -> None:
        # Defer import to avoid hard dependency if not installed
        try:
                from PIL import ImageGrab
        except Exception:
                raise RuntimeError("Pillow ImageGrab is required for screenshots. Please ensure Pillow is installed.")

        # Update and get geometry
        root.update()
        root.update_idletasks()
        geo = root.winfo_geometry()  # e.g. "1400x900+100+100"
        wh, _, xy = geo.partition("+")
        width_str, _, height_str = wh.partition("x")
        try:
                width = int(width_str)
                height = int(height_str)
                x = root.winfo_rootx()
                y = root.winfo_rooty()
        except Exception:
                # Fallback to full screen grab
                bbox = None
        else:
                bbox = (x, y, x + width, y + height)

        img = ImageGrab.grab(bbox=bbox)
        ensure_dir(out_path.parent)
        img.save(str(out_path))


def open_tool(main_window, tool_key: str) -> None:
        # Map keys to methods on main_window
        key_to_method = {
                "excel_emd": main_window.open_excel_emd,
                "bill_note": main_window.open_bill_note,
                "emd_refund": main_window.open_emd_refund,
                "deductions_table": main_window.open_deductions_table,
                "delay_calculator": main_window.open_delay_calculator,
                "security_refund": main_window.open_security_refund,
                "financial_progress": main_window.open_financial_progress,
                "stamp_duty": main_window.open_stamp_duty,
                "bill_deviation": main_window.open_bill_deviation,
                "tender_processing": main_window.open_tender_processing,
        }
        method = key_to_method.get(tool_key)
        if method is None:
                raise ValueError(f"Unknown tool key: {tool_key}")
        method()


def run_scenario() -> None:
        app = PWDToolsApp()
        # Allow splash to transition to main window
        app.root.after(2500, lambda: None)
        app.root.update()
        app.root.update_idletasks()

        # Wait for main_window to be created by initialize_main_app
        start = time.time()
        while not hasattr(app, "main_window"):
                app.root.update()
                time.sleep(0.05)
                if time.time() - start > 6:
                        raise TimeoutError("Main window not initialized in time")

        tools = [
                "excel_emd",
                "bill_note",
                "emd_refund",
                "deductions_table",
                "delay_calculator",
                "security_refund",
                "financial_progress",
                "stamp_duty",
                "bill_deviation",
                "tender_processing",
        ]

        # Three runs per tool
        for tool in tools:
                for n in range(1, 4):
                        # Open tool window
                        open_tool(app.main_window, tool)
                        # Give time to render
                        for _ in range(10):
                                app.root.update()
                                app.root.update_idletasks()
                                time.sleep(0.05)
                        # Screenshot main window (landing) to capture color templates/elegance
                        out_path = Path("screenshots") / tool / f"run_{n}.png"
                        save_root_screenshot(app.root, out_path)
                        # Close any modal grab to avoid stacking
                        app.root.focus_force()

        # Final screenshot of landing
        final_path = Path("screenshots") / "landing" / "main.png"
        save_root_screenshot(app.root, final_path)

        # Quit the app
        app.root.after(100, app.root.quit)
        app.root.update()


if __name__ == "__main__":
        run_scenario()