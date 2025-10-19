import tkinter as tk
import time

class Stopwatch:
    def __init__(self, master):
        self.master = master
        master.title("Stopwatch")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.time_label = tk.Label(master, text="00:00:00.00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.display_time()
            self.master.after(10, self.update_time) # Update every 10 milliseconds

    def display_time(self):
        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        milliseconds = int((self.elapsed_time * 100) % 100)
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
        self.time_label.config(text=time_str)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time # Resume from current elapsed time
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def reset(self):
        self.stop()
        self.elapsed_time = 0
        self.display_time()
        self.reset_button.config(state=tk.DISABLED)

root = tk.Tk()
my_stopwatch = Stopwatch(root)
root.mainloop()
