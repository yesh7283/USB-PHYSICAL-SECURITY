import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import mysql.connector
import os

# Define user roles and permissions
users = {
    "admin": {"password": "adminpass", "role": "admin"},
    "user": {"password": "userpass", "role": "user"}
}

def main():
    def pro_info():
        import webbrowser
        with open("1.html", "w") as f:
            message = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <style>
                table {
                  border-collapse: collapse;
                  width: 100%;
                  margin-bottom: 20px;
                }
                th, td {
                  border: 1px solid #ddd;
                  padding: 8px;
                  text-align: left;
                }
                th {
                  background-color: #f2f2f2;
                }
                tr:nth-child(even) {
                  background-color: #f9f9f9;
                }
                tr:hover {
                  background-color: #f5f5f5;
                }
              </style>
              <title>USB PHYSICAL SECURITY</title>
            </head>
            <body>
              <h2>PROJECT INFORMATION</h2>
              <p>This project was developed by <b>team-5</b> as part of cyber security internship<br>
                 This project is designed to protect the system from the usb threat by disabling the usb ports</p>
              <table>
                <thead>
                  <tr style="color: black;background-color:#green;">
                    <th>Project details</th>
                    <th>Info</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Project Name</td>
                    <td>USB Physical Security</td>
                  </tr>
                  <tr>
                    <td>Project Description</td>
                    <td>The USB Physical Security refers to the set of mechanisms and techniques used to secure and control the access of devices to USB ports</td>
                  </tr>
                  <tr>
                    <td>Project Start Date</td>
                    <td>26-05-24</td>
                  </tr>
                  <tr>
                    <td>Project End Date</td>
                    <td>29-06-24</td>
                  </tr>
                  <tr>
                    <td>Project Status</td>
                    <td><b>In Progress</b></td>
                  </tr>
                </tbody>
              </table>
              <h2><b>DEVELOPER DETAILS</b></h2>
              <table>
                <thead>
                  <tr>
                    <th>Employee ID</th>
                    <th>Employee Name</th>
                    <th>Email ID</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>ST#IS#6360</td>
                    <td>Singireddy Hasini</td>
                    <td>hasinisingireddy2@gmail.com</td>
                  </tr>
                  <tr>
                    <td>ST#IS#6361</td>
                    <td>Yeswanth Sai Mahesh Jagu</td>
                    <td>yesh7283@gmail.com</td>
                  </tr>
                  <tr>
                    <td>ST#IS#6362</td>
                    <td>Dumpa venkata Harsha vardhan</td>
                    <td></td>
                  </tr>
                  <tr>
                    <td>ST#IS#6363</td>
                    <td>Saisrikar Devasani</td>
                    <td></td>
                  </tr>
                  <tr>
                    <td>ST#IS#6364</td>
                    <td>Shaik Masthan</td>
                    <td></td>
                  </tr>
                </tbody>
              </table>
              <h2><b>MENTOR DETAILS</b></h2>
              <table>
                <thead>
                  <tr>
                    <th>Mentor Names</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Santosh Chaluvadi(CEO)</td>
                  </tr>
                  <tr>
                    <td>Upendar</td>
                  </tr>
                  <tr>
                    <td>Krishna (Junior Security Analyst)</td>
                  </tr>
                </tbody>
              </table>
            </body>
            </html>
            '''
            f.write(message)
        webbrowser.open_new_tab("1.html")

    root = tk.Tk()
    image = Image.open(r'C:\Users\yeswa\Downloads\image.jpg')  # Use raw string or double backslashes
    new_size = (200, 200)
    b3 = tk.Button(root, text="Project INFO", font=("Menlo", 11), bg="red", fg="white", command=pro_info)
    b3.pack()
    project_label = tk.Label(root, text="***USB Physical Security***", font=("Arial", 18, "bold"), bg="white", fg="black")
    project_label.pack(pady=10)
    images = image.resize(new_size)
    tk_image = ImageTk.PhotoImage(images)
    label = tk.Label(root, image=tk_image)
    label.pack(pady=10)
    root.title("USB PHYSICAL SECURITY FOR SYSTEM")
    root.geometry('700x700')
    root.configure(bg='gray')
    button_frame = tk.Frame(root, bg='white')
    success_label = tk.Label(button_frame, text="", font=("Didot", 12), height=10, width=60, bg='black')
    success_label.pack()

    def b1_click():
        pass_open = tk.Toplevel(root)
        pass_open.title("Enter the password to disable the USB")
        pass_open.geometry("400x300")
        pass_label = tk.Label(pass_open, text="Enter the password")
        pass_label.pack()
        pass_enter = tk.Entry(pass_open, show="$")
        pass_enter.pack()

        def ok_btn():
            entered_password = pass_enter.get()
            if entered_password in [user["password"] for user in users.values() if user["role"] == "admin"]:
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="7283", database="sup_database")
                    my_cursor = conn.cursor()
                    command = r'reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v "start" /t REG_DWORD /d 4 /f > nul'
                    subprocess.call(command, shell=True)
                    success_label.config(text="USB PORTS ARE DISABLED SUCCESSFULLY", bg='black', fg='white')
                    pass_open.destroy()
                    my_cursor.close()
                    conn.close()
                except mysql.connector.Error as err:
                    messagebox.showerror("Database Error", f"Error: {err}")
            else:
                error_label.config(text="INCORRECT PASSWORD. PLEASE TRY AGAIN", bg='black', fg='white')
                pass_enter.delete(0, tk.END)

        ok_btn = tk.Button(pass_open, text="ENTER", command=ok_btn)
        ok_btn.pack()
        error_label = tk.Label(pass_open, text="", font=("Didot", 11), bg="#f2f2f2", fg="#ff0000")
        error_label.pack()

    def b2_click():
        pass_open = tk.Toplevel(root)
        pass_open.title("Enter the password to enable the USB")
        pass_open.geometry("400x300")
        pass_label = tk.Label(pass_open, text="Enter the enable password")
        pass_label.pack()
        pass_enter = tk.Entry(pass_open, show="$")
        pass_enter.pack()
        
        def ok_btn():
            entered_password = pass_enter.get()
            if entered_password in [user["password"] for user in users.values() if user["role"] == "admin"]:
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="7283", database="sup_database")
                    my_cursor = conn.cursor()
                    command = r'reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v "start" /t REG_DWORD /d 3 /f > nul'
                    subprocess.call(command, shell=True)
                    success_label.config(text="USB PORTS ARE ENABLED SUCCESSFULLY", bg='black', fg='white')
                    pass_open.destroy()
                    my_cursor.close()
                    conn.close()
                except mysql.connector.Error as err:
                    messagebox.showerror("Database Error", f"Error: {err}")
            else:
                error_label.config(text="INCORRECT PASSWORD. PLEASE TRY AGAIN", bg='black', fg='white')
                pass_enter.delete(0, tk.END)

        ok_btn = tk.Button(pass_open, text="ENTER", command=ok_btn)
        ok_btn.pack()
        error_label = tk.Label(pass_open, text="", font=("Didot", 11), bg="#f2f2f2", fg="#ff0000")
        error_label.pack()

    def list_usb_files():
        usb_path = "H:\bcm2710-rpi-2-b.dtb"  # Replace with the actual USB mount path
        try:
            files = os.listdir(usb_path)
            if files:
                file_list = "\n".join(files)
                messagebox.showinfo("Files in USB", file_list)
            else:
                messagebox.showinfo("Files in USB", "No files found.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not access USB: {e}")

    def login():
        login_window = tk.Toplevel(root)
        login_window.title("Login")
        login_window.geometry("300x200")

        tk.Label(login_window, text="Username:").pack()
        username_entry = tk.Entry(login_window)
        username_entry.pack()

        tk.Label(login_window, text="Password:").pack()
        password_entry = tk.Entry(login_window, show="*")
        password_entry.pack()

        def login_btn():
            username = username_entry.get()
            password = password_entry.get()
            if username in users and users[username]["password"] == password:
                role = users[username]["role"]
                if role == "admin":
                    messagebox.showinfo("Login Successful", "Welcome, Admin!")
                elif role == "user":
                    messagebox.showinfo("Login Successful", "Welcome, User!")
                login_window.destroy()
            else:
                messagebox.showerror("Login Failed", "Invalid credentials, please try again.")
        
        tk.Button(login_window, text="Login", command=login_btn).pack()

    b1 = tk.Button(button_frame, text="DISABLE THE USB PORTS", font=("Helvetica", 11), bg="red", fg="white", command=b1_click)
    b1.pack(pady=10)
    b2 = tk.Button(button_frame, text="ENABLE THE USB PORTS", font=("Helvetica", 11), bg="red", fg="white", command=b2_click)
    b2.pack(pady=10)
    b4 = tk.Button(button_frame, text="LIST FILES ON USB", font=("Helvetica", 11), bg="red", fg="white", command=list_usb_files)
    b4.pack(pady=10)
    b5 = tk.Button(button_frame, text="LOGIN", font=("Helvetica", 11), bg="blue", fg="white", command=login)
    b5.pack(pady=10)
    button_frame.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
