import tkinter as tk
from tkinter import messagebox

def calculate_salary():
    try:
        # Get input
        input_val = entry_basic.get()
        if not input_val:
            return # Do nothing if empty
        
        basic_salary = float(input_val)

        # Calculations
        hra = 0.20 * basic_salary
        da = 0.10 * basic_salary
        gross_salary = basic_salary + hra + da
        
        pf = 0.12 * basic_salary
        tax = 0.05 * gross_salary
        net_salary = gross_salary - (pf + tax)

        # Update Result Labels
        # We format to 2 decimal places for currency precision
        lbl_hra_val.config(text=f"{hra:.2f}")
        lbl_da_val.config(text=f"{da:.2f}")
        lbl_gross_val.config(text=f"{gross_salary:.2f}")
        lbl_pf_val.config(text=f"{pf:.2f}")
        lbl_tax_val.config(text=f"{tax:.2f}")
        lbl_net_val.config(text=f"{net_salary:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric value for Basic Salary.")

# --- GUI Setup ---

# Aesthetic Color Palette
COLOR_BG = "#E0F2F1"       # Light Teal Background
COLOR_FRAME = "#FFFFFF"    # White Card
COLOR_PRIMARY = "#00695C"  # Dark Teal Text
COLOR_ACCENT = "#26A69A"   # Medium Teal Button
COLOR_TEXT = "#37474F"     # Dark Grey Text
FONT_HEADER = ("Helvetica", 16, "bold")
FONT_BODY = ("Helvetica", 11)
FONT_BOLD = ("Helvetica", 11, "bold")

root = tk.Tk()
root.title("Salary Calculator")
root.geometry("400x550")
root.configure(bg=COLOR_BG)
root.resizable(False, False)

# Main Container (Card Style)
frame = tk.Frame(root, bg=COLOR_FRAME, padx=30, pady=30, relief="flat", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Header
lbl_header = tk.Label(frame, text="Salary Calculator", font=FONT_HEADER, bg=COLOR_FRAME, fg=COLOR_PRIMARY)
lbl_header.pack(pady=(0, 20))

# Input Section
input_frame = tk.Frame(frame, bg=COLOR_FRAME)
input_frame.pack(fill="x", pady=5)

lbl_basic = tk.Label(input_frame, text="Basic Salary:", font=FONT_BODY, bg=COLOR_FRAME, fg=COLOR_TEXT)
lbl_basic.pack(anchor="w")

entry_basic = tk.Entry(input_frame, font=FONT_BODY, bg="#F5F5F5", relief="flat", bd=1, highlightthickness=1, highlightbackground="#B2DFDB")
entry_basic.pack(fill="x", ipady=5, pady=5)

# Button
btn_calc = tk.Button(frame, text="CALCULATE", font=FONT_BOLD, bg=COLOR_ACCENT, fg="white", 
                     activebackground=COLOR_PRIMARY, activeforeground="white", 
                     relief="flat", cursor="hand2", command=calculate_salary)
btn_calc.pack(fill="x", pady=20, ipady=5)

# Results Section
results_frame = tk.Frame(frame, bg=COLOR_FRAME)
results_frame.pack(fill="x")

def create_result_row(parent, label_text):
    row = tk.Frame(parent, bg=COLOR_FRAME)
    row.pack(fill="x", pady=2)
    lbl = tk.Label(row, text=label_text, font=FONT_BODY, bg=COLOR_FRAME, fg=COLOR_TEXT)
    lbl.pack(side="left")
    val = tk.Label(row, text="0.00", font=FONT_BOLD, bg=COLOR_FRAME, fg=COLOR_PRIMARY)
    val.pack(side="right")
    return val

lbl_hra_val = create_result_row(results_frame, "HRA (20%):")
lbl_da_val = create_result_row(results_frame, "DA (10%):")
lbl_gross_val = create_result_row(results_frame, "Gross Salary:")

# Divider
tk.Frame(results_frame, bg="#E0E0E0", height=1).pack(fill="x", pady=10)

lbl_pf_val = create_result_row(results_frame, "PF Deduction (12%):")
lbl_tax_val = create_result_row(results_frame, "Tax Deduction (5%):")

# Divider
tk.Frame(results_frame, bg="#E0E0E0", height=1).pack(fill="x", pady=10)

# Net Salary (Highlighted)
row_net = tk.Frame(results_frame, bg=COLOR_FRAME)
row_net.pack(fill="x", pady=5)
tk.Label(row_net, text="Net Salary:", font=("Helvetica", 13, "bold"), bg=COLOR_FRAME, fg=COLOR_TEXT).pack(side="left")
lbl_net_val = tk.Label(row_net, text="0.00", font=("Helvetica", 13, "bold"), bg=COLOR_FRAME, fg="#D84315") # Orange for emphasis
lbl_net_val.pack(side="right")

# Copyright Footer
lbl_copyright = tk.Label(root, text="© Anshita @ 2026 NIELIT Ropar", font=("Helvetica", 9), bg=COLOR_BG, fg="#78909C")
lbl_copyright.pack(side="bottom", pady=15)

# Trigger calculation on "Enter" key press
root.bind('<Return>', lambda event: calculate_salary())

root.mainloop()