import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("ASM Files", "*.asm")])
    if file_path:
        file_label.config(text=file_path)
        run_button.config(state=tk.NORMAL)  # Enable the run button

def run_emu8086():
    emu_path = r"C:\Users\Lenovo\Desktop\emu8086\emu8086.exe"  # Path to EMU8086 executable
    
    asm_file = file_label.cget("text")  # Get the selected file's path
    
    if asm_file:
        print(f"Running EMU8086 with file: {asm_file}")
        subprocess.run([emu_path, asm_file])

# Create the main GUI window
root = tk.Tk()
root.title("EMU8086 GUI")
root.geometry("400x200")

# Label to display the selected file
file_label = tk.Label(root, text="Select an ASM file", width=40, height=2)
file_label.pack(pady=20)

# Button to choose the file
choose_button = tk.Button(root, text="Choose File", command=choose_file)
choose_button.pack(pady=5)

# Button to run EMU8086
run_button = tk.Button(root, text="Run EMU8086", state=tk.DISABLED, command=run_emu8086)
run_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
