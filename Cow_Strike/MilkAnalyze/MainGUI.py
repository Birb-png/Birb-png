"""
MainGUI.py (View)
- จัดการการแสดงผลของ  USER และการจัดระเบียบของ GUI

: Main Function :
- create_mainGUI(): สร้างหน้าต่างหลักของระบบ รวมถึงป้ายชื่อ, ช่องกรอก ID, ปุ่มค้นหา, เช็คบ็อกซ์สำหรับมะนาว, ปุ่มรีดนม
"""
import tkinter as tk
from FunctionGUI import search_cow_gui, milk_cow_gui

def create_mainGUI():
    global root, id, search_button, milk_button, lemon_button_frame, result_label, report_label, back_button_frame, var_lemon
    
    root = tk.Tk()
    root.title("Cow Milking Analysis")
    
    root.geometry("900x800")  
    root.minsize(900, 800) 
    root.maxsize(1280, 720) 

    title_label = tk.Label(root, text="Cow Information and Milk Analysis", font=("Arial", 24, "bold"))
    title_label.pack(pady=20)
    

    id_label = tk.Label(root, text="Enter Cow ID:", font=("Arial", 16))
    id_label.pack(pady=10)
    
    id = tk.Entry(root, font=("Arial", 14))
    id.pack(pady=10)
    
    search_button = tk.Button(root, text="Search", font=("Arial", 14), 
                              command=lambda: search_cow_gui(id, result_label, milk_button, lemon_button_frame, search_button))
    search_button.pack(pady=10)
    

    milk_button = tk.Button(root, text="Milk Cow", font=("Arial", 14), 
                            command=lambda: milk_cow_gui(id, result_label, milk_button, var_lemon, report_label, back_button_frame, search_button, lemon_check), state='disabled')
    milk_button.pack(pady=10)
    
    var_lemon = tk.BooleanVar()
    lemon_button_frame = tk.Frame(root)
    lemon_check = tk.Checkbutton(lemon_button_frame, text="Add Lemon for Sour Milk", font=("Arial", 14), 
                                 variable=var_lemon)
    lemon_check.pack(pady=5)
    
    result_label = tk.Label(root, text="", font=("Arial", 14), wraplength=600)
    result_label.pack(pady=20)
    
    report_label = tk.Label(root, text="", font=("Arial", 14), wraplength=600)
    report_label.pack(pady=20)
    
    back_button_frame = tk.Frame(root)
    back_button = tk.Button(back_button_frame, text="Back", font=("Arial", 14), command=lambda: back_to_main())
    
    def back_to_main():
        milk_button.pack(pady=10)  
        search_button.config(state='normal') 
        id.config(state='normal')  
        lemon_check.config(state='normal')
        lemon_button_frame.pack_forget() 
        result_label.config(text="")
        report_label.config(text="")
        back_button_frame.pack_forget()  
    
    back_button.pack(pady=5)
    
    # MAIN LOOP
    root.mainloop()

# GUI main
if __name__ == "__main__":
    create_mainGUI()
