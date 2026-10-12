import os
import tkinter as tk
from datetime import date
from pathlib import Path
from tkinter import messagebox
from typing import Optional


def get_start_date(storage_file: Path, today: Optional[date] = None) -> date:
    """Load the saved start date, creating it as today on the first run."""
    start_date = today if today is not None else date.today()
    storage_file.parent.mkdir(parents=True, exist_ok=True)

    if not storage_file.exists():
        storage_file.write_text(start_date.isoformat(), encoding="ascii")
        return start_date

    saved_date = storage_file.read_text(encoding="ascii").strip()
    try:
        return date.fromisoformat(saved_date)
    except ValueError as error:
        raise ValueError(
            f"The saved start date in {storage_file} is invalid."
        ) from error


def get_day_number(start_date: date, today: Optional[date] = None) -> int:
    current_date = today if today is not None else date.today()
    return max(1, (current_date - start_date).days + 1)


def get_storage_file() -> Path:
    app_data = Path(
        os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming")
    )
    return app_data / "DayCounter" / "start_date.txt"


class DayCounterApp:
    def __init__(self, root: tk.Tk, start_date: date) -> None:
        self.root = root
        self.start_date = start_date

        root.title("Day Counter")
        root.geometry("400x300")
        root.minsize(340, 260)
        root.configure(bg="#f3f5f9")

        card = tk.Frame(root, bg="white", padx=32, pady=28)
        card.pack(expand=True, fill="both", padx=24, pady=24)

        tk.Label(
            card,
            text="YOUR COUNTER",
            bg="white",
            fg="#687386",
            font=("Segoe UI", 10, "bold"),
        ).pack(pady=(4, 8))

        self.day_label = tk.Label(
            card,
            bg="white",
            fg="#202b42",
            font=("Segoe UI", 46, "bold"),
        )
        self.day_label.pack()

        tk.Label(
            card,
            text=f"Started {start_date.strftime('%B %d, %Y')}",
            bg="white",
            fg="#687386",
            font=("Segoe UI", 11),
        ).pack(pady=(8, 0))

        tk.Label(
            card,
            text="The count starts at Day 1",
            bg="white",
            fg="#8791a2",
            font=("Segoe UI", 9),
        ).pack(pady=(18, 0))

        self.refresh_count()

    def refresh_count(self) -> None:
        day_number = get_day_number(self.start_date)
        self.day_label.configure(text=f"DAY {day_number:,}")
        self.root.after(60_000, self.refresh_count)


def main() -> None:
    root = tk.Tk()
    try:
        start_date = get_start_date(get_storage_file())
    except (OSError, ValueError) as error:
        messagebox.showerror("Day Counter", str(error), parent=root)
        root.destroy()
        return

    DayCounterApp(root, start_date)
    root.mainloop()


if __name__ == "__main__":
    main()
