"""
FunctionGUI.py (Controller)
================
- จัดการกับการกับ Action

: Main Function:
- search_cow_gui(id, milk_button, result_label, var_lemon): จัดการการค้นหาวัวและแสดงผลลัพธ์
- milk_cow_gui(id, milk_button, var_lemon, result_label): จัดการการรีดนมและแสดงผลลัพธ์
- gen_report(): สร้างรายงานและแสดงผล รวมถึงปุ่มรีเซ็ต BSOD
- back_to_main(reset_button): กลับไปยังหน้าหลัก
"""

import tkinter as tk
from tkinter import messagebox
from MilkAnalyze import load_cows, search_cow, milk_cow, generate_report, reset_BSOD_cows

cows = load_cows('Cow_Strike/pythonData/Cow.csv')

def search_cow_gui(id, result_label, button_milk, lemon_button_frame, search_button):
    cow_id = id.get().strip()
    #print(cow_id)
    result = search_cow(cows, cow_id)
    
    if isinstance(result, str):  # <========= if Error 
        if result == "Invalid ID":
            result_label.config(text="Invalid ... ID must be an 8 digit number not starting with zero .")
            button_milk.config(state='disabled')
            lemon_button_frame.pack_forget()  
        elif result == "Not Found":
            result_label.config(text="Cow ID not found err.")
            button_milk.config(state='disabled')
            lemon_button_frame.pack_forget() 
        elif result == "BSOD":
            result_label.config(text="Cow has BSOD. Please reset the cow.")
            button_milk.config(state='disabled')
            lemon_button_frame.pack_forget()  #
    else:
        cow = result
        info = f"ID: {cow.cow_id}\nColor: {cow.color}\nAge: {cow.age_years} years and {cow.age_months} months"
        result_label.config(text=info)
        button_milk.config(state='normal')  # enable the button if cow is found
        
        if cow.color == 'White':# show and hide lemon
            lemon_button_frame.pack(pady=10)  
        else:
            lemon_button_frame.pack_forget() 
def milk_cow_gui(id, result_label, button_milk, var_lemon, report_label, back_button_frame, search_button, lemon_check):
    cow_id = id.get().strip()
    cow = cows.get(cow_id)
    
    if cow:
        milk_type = milk_cow(cow)
        if milk_type.endswith("(BSOD)"):
            result_label.config(text=f"The milk is {milk_type}.")
            button_milk.pack_forget() 
        else:
            result_label.config(text=f"The milk is {milk_type}.")
        GenReport(report_label, back_button_frame)
        
        # ============Disable input===========
        id.config(state='disabled')
        search_button.config(state='disabled')
        lemon_check.config(state='disabled')
    else:
        result_label.config(text="Cow ID not found.")

def GenReport(report_label, back_button_frame):
    report, bsod_cows = generate_report(cows)
    
    reportMsg = (
        f"Total Regular Milk: {report['Regular Milk']}\n"
        f"Total Sour Milk: {report['Sour Milk']}\n"
        f"Total Chocolate Milk: {report['Chocolate Milk']}\n"
        f"Total Bottles: {sum(report.values())}\n"
        f"BSOD Cows: {', '.join(bsod_cows)}"
    )
    
    report_label.config(text=reportMsg)
    
    # ============Remove existing reset button if any===========
    for widget in report_label.master.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") == "Reset BSOD Cows":
            widget.pack_forget()
    
    if bsod_cows:
        reset_button = tk.Button(report_label.master, text="Reset BSOD Cows", command=reset_bsod)
        reset_button.pack(pady=5)
         
    
    # back butt
    back_button_frame.pack(pady=5)

def reset_bsod():
    reset_BSOD_cows(cows)
    messagebox.showinfo("Reset", "BSOD cows have been reset.")
    # ------------Re gen result----------
   # Report = tk.Label(root, text="", font=("Arial", 14), wraplength=600)
    gen_report(Report, back_button_frame)

