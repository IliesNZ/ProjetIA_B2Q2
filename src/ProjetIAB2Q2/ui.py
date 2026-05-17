import tkinter as tk
import threading

# Colors
TRANSPARENT_COLOR = "#123456"
BG_MAIN = TRANSPARENT_COLOR
BTN_BG = TRANSPARENT_COLOR
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
        # Try to enable color-key transparency (works on Windows)
        try:
            self.root.attributes("-transparentcolor", TRANSPARENT_COLOR)
        except Exception:
            pass
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.bind("<Escape>", lambda _event: self.root.destroy())

    def setup_ui(self):
        # Main container
        self.container = tk.Frame(self.root, bg=BG_MAIN)
        self.container.pack(fill="both", expand=True)

        # Drag handle
        # Make handle background transparent (color-key) so only the mark remains visible
        handle = tk.Frame(self.container, bg=BTN_BG, width=16, cursor="fleur")
        handle.pack(side="left", fill="y")
        handle.pack_propagate(False)

        handle_mark = tk.Label(
            handle,
            text="||",
            font=("Segoe UI", 8, "bold"),
            bg=BTN_BG,
            fg="white",
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
            activebackground=BTN_BG,
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

        # Close button: larger hitbox for easier closing
        btn_close = tk.Button(
            self.container,
            text="×",
            font=("Segoe UI Semibold", 16),
            bg=BTN_BG,
            fg="white",
            activebackground=BTN_BG,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=8,
            pady=0,
            width=2,
            cursor="hand2",
            command=self.root.destroy,
        )
        btn_close.pack(side="right", fill="y", padx=(0, 2), pady=2)

        # Spinner wheel (custom canvas animation)
        self.spinner_canvas = tk.Canvas(
            self.container,
            width=34,
            height=34,
            bg=BTN_BG,
            highlightthickness=0,
            bd=0,
        )
        self.spinner_arc = self.spinner_canvas.create_arc(
            6,
            6,
            28,
            28,
            start=0,
            extent=300,
            style=tk.ARC,
            outline="white",
            width=3,
        )
        self._spinner_angle = 0
        self._spinner_job = None
        self._busy = False

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
        # No hover background effect: keep transparent look
        return

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

    def _animate_spinner(self):
        if not self._busy:
            return
        self._spinner_angle = (self._spinner_angle + 18) % 360
        self.spinner_canvas.itemconfig(self.spinner_arc, start=self._spinner_angle)
        self._spinner_job = self.root.after(40, self._animate_spinner)

    def set_busy(self, is_busy):
        if is_busy:
            self._busy = True
            self.btn_play.config(state=tk.DISABLED, bg=BTN_ACTIVE)
            self.btn_play.pack_forget()
            self.spinner_canvas.pack(side="left", expand=True, fill="both", padx=4, pady=4)
            self._animate_spinner()
        else:
            self._busy = False
            if self._spinner_job is not None:
                self.root.after_cancel(self._spinner_job)
                self._spinner_job = None
            self.spinner_canvas.pack_forget()
            self.btn_play.config(state=tk.NORMAL, bg=BTN_BG)
            self.btn_play.pack(side="left", expand=True, fill="both", padx=4, pady=4)

    def run(self):
        self.root.mainloop()
