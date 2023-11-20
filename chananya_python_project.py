import tkinter as tk

def calculate_area():
    width = int(entry1.get())
    height = int(entry2.get())
    area = width * height
    create_result_window(area)

def create_result_window(area):
    result_window = tk.Toplevel(root)
    result_window.title("Area Calculator")
    result_label = tk.Label(result_window, text=f"Area of rectangle is : \n{area}")
    result_label.pack()
    retry_button = tk.Button(result_window, text="Retry", command=result_window.destroy)
    retry_button.pack()

root = tk.Tk()
root.title("Area Calculator")

label1 = tk.Label(root, text="Width")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Height")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

calculate_button = tk.Button(root, text="OK", command=calculate_area)
calculate_button.pack(side="left")
cancel_button = tk.Button(root, text="Cancel", command=root.quit)
cancel_button.pack(side="right")


root.mainloop()
