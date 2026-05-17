import tkinter as tk
from tkinter import ttk
import threading

# Colors
BG_MAIN = "#000000"
BTN_BG = "#000000"
BTN_HOVER = "#1a1a1a"
BTN_ACTIVE = "#0d0d0d"
HANDLE_BG = "#1a1a1a"
HANDLE_FG = "#666666"


class MinimalUI:
    def __init__(self, on_play_callback):
        self.on_play_callback = on_play_callback
        self.root = tk.Tk()
        self.setup_window()
        self.setup_ui()

    def setup_window(self):
        self.root.title("Bot IA - B2Q2")
        self.root.geometry("130x64")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_MAIN)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)

    def setup_ui(self):
        # Style for progress bar
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(
            "Tiny.Horizontal.TProgressbar",
            troughcolor="#e2e2e2",
            bordercolor="#e2e2e2",
            background=BTN_BG,
            lightcolor=BTN_BG,
            darkcolor=BTN_BG,
            thickness=7,
        )

        # Main container
        self.container = tk.Frame(self.root, bg=BG_MAIN)
        self.container.pack(fill="both", expand=True)

        # Drag handle
        handle = tk.Frame(self.container, bg=HANDLE_BG, width=16, cursor="fleur")
        handle.pack(side="left", fill="y")
        handle.pack_propagate(False)

        handle_mark = tk.Label(
            handle,
            text="||",
            font=("Segoe UI", 8, "bold"),
            bg=HANDLE_BG,
            fg=HANDLE_FG,
        )
        handle_mark.pack(expand=True)

        handle.bind("<ButtonPress-1>", self._start_move)
        handle.bind("<B1-Motion>", self._move_window)
        handle_mark.bind("<ButtonPress-1>", self._start_move)
        handle_mark.bind("<B1-Motion>", self._move_window)

        # Play button
        self.btn_play = tk.Button(
            self.container,
            text="▶",
            font=("Segoe UI Semibold", 16),
            bg=BTN_BG,
            fg="white",
            activebackground=BTN_ACTIVE,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=0,
            pady=0,
            cursor="hand2",
            command=self._on_play_click,
        )
        self.btn_play.pack(side="left", expand=True, fill="both", padx=4, pady=4)
        self.btn_play.bind("<Enter>", self._on_enter_play)
        self.btn_play.bind("<Leave>", self._on_leave_play)

        # Close button
        btn_close = tk.Button(
            self.container,
            text="×",
            font=("Segoe UI Semibold", 14),
            bg=BTN_BG,
            fg="white",
            activebackground=BTN_ACTIVE,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=4,
            pady=0,
            cursor="hand2",
            command=self.root.quit,
        )
        btn_close.pack(side="right", fill="y", padx=2)

        # Spinner
        self.spinner = ttk.Progressbar(
            self.container,
            mode="indeterminate",
            style="Tiny.Horizontal.TProgressbar",
        )

    def _start_move(self, event):
        self.root._drag_start_x = event.x_root
        self.root._drag_start_y = event.y_root
        self.root._win_start_x = self.root.winfo_x()
        self.root._win_start_y = self.root.winfo_y()

    def _move_window(self, event):
        dx = event.x_root - self.root._drag_start_x
        dy = event.y_root - self.root._drag_start_y
        self.root.geometry(f"+{self.root._win_start_x + dx}+{self.root._win_start_y + dy}")

    def _on_enter_play(self, _event):
        if self.btn_play["state"] == tk.NORMAL:
            self.btn_play.config(bg=BTN_HOVER)

    def _on_leave_play(self, _event):
        if self.btn_play["state"] == tk.NORMAL:
            self.btn_play.config(bg=BTN_BG)

    def _on_play_click(self):
        self.set_busy(True)

        def background_task():
            try:
                self.on_play_callback()
            except Exception as e:
                print(f"Erreur: {e}")
            finally:
                self.root.after(0, lambda: self.set_busy(False))

        threading.Thread(target=background_task, daemon=True).start()

    def set_busy(self, is_busy):
        if is_busy:
            self.btn_play.config(state=tk.DISABLED, bg=BTN_ACTIVE)
            self.btn_play.pack_forget()
            self.spinner.pack(side="left", expand=True, fill="both", padx=4, pady=4)
            self.spinner.start(12)
        else:
            self.spinner.stop()
            self.spinner.pack_forget()
            self.btn_play.config(state=tk.NORMAL, bg=BTN_BG)
            self.btn_play.pack(side="left", expand=True, fill="both", padx=4, pady=4)

    def run(self):
        self.root.mainloop()
