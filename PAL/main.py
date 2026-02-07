import tkinter as tk
import threading
import time
import dolphin_memory_engine as dme
import traceback

ADDRESS = 0x80463E78
UPDATE_DELAY = 0.01666

def memory_loop():
    print("[THREAD] Memory loop started")

    while True:
        try:
            if not dme.is_hooked():
                print("[HOOK] Not hooked → hook()")
                dme.hook()
                print("[HOOK] Hooked:", dme.is_hooked())

            value = dme.read_word(ADDRESS)
            print(f"[READ] 0x{ADDRESS:X} = {value}")

            label.config(text=f"Current Score (P1):\n{value}")

        except Exception as e:
            print("[ERROR]", repr(e))
            traceback.print_exc()
            label.config(text="Waiting for Dolphin…")

        time.sleep(UPDATE_DELAY)

root = tk.Tk()
root.title("Dolphin Memory Watch")
root.resizable(False, False)

label = tk.Label(root, font=("Consolas", 28), justify="center")
label.pack(padx=30, pady=25)

threading.Thread(target=memory_loop, daemon=True).start()
root.mainloop()