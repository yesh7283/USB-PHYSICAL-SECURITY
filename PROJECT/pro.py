import tkinter as tk
from tkinter import Label, messagebox
import subprocess
from PIL import Image, ImageTk
from tkinter import Tk
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector

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
              <p>This project was developed by <b>team-9</b> as part of cyber security internship<br>
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
                    <td>17-12-23</td>
                  </tr>
                  <tr>
                    <td>Project End Date</td>
                    <td>31-12-23</td>
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
                    <td>ST#IS#6048</td>
                    <td>D.Spoorthi</td>
                    <td>domalaspoorthi@gmail.com</td>
                  </tr>
                  <tr>
                    <td>ST#IS#6049</td>
                    <td>M.Sai Ganesh Reddy</td>
                    <td>m.saiganesh2811@gmail.com</td>
                  </tr>
                  <tr>
                    <td>ST#IS#6050</td>
                    <td>V.Poojitha</td>
                    <td>saipoojitha.veggalam@gmail.com</td>
                  </tr>
                  <tr>
                    <td>ST#IS#6051</td>
                    <td>R.Nikitha</td>
                    <td>rnikitha458@gmail.com</td>
                  </tr>
                  <tr>
                    <td>ST#IS#6052</td>
                    <td>M.lahari</td>
                    <td>lahari4210@gmail.com</td>
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
                    <td>Krishna</td>
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
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="sup_database")
            my_cursor = conn.cursor()
            res = pass_enter.get()
            sql = "SELECT passwords FROM why WHERE passwords=%s AND sno=%s"
            val = (res, 1)
            my_cursor.execute(sql, val)
            results = my_cursor.fetchall()
            if results:
                command = r'reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v "start" /t REG_DWORD /d 4 /f > nul'
                subprocess.call(command, shell=True)
                success_label.config(text="USB PORTS ARE DISABLED SUCCESSFULLY", bg='black', fg='white')
                res2 = pass_enter.get()
                sql1 = "DELETE FROM why WHERE sno=%s AND passwords=%s"
                val1 = (1, res2)
                my_cursor.execute(sql1, val1)
                conn.commit()
                pass_enter.destroy()
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
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="sup_database")
            my_cursor = conn.cursor()
            res = pass_enter.get()
            sql = "SELECT passwords FROM why WHERE passwords=%s AND sno=%s"
            val = (res, 1)
            my_cursor.execute(sql, val)
            results = my_cursor.fetchall()
            if results:
                command = r'reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v "start" /t REG_DWORD /d 3 /f > nul'
                subprocess.call(command, shell=True)
                res1 = pass_enter.get()
                success_label.config(text="USB PORTS ARE ENABLED SUCCESSFULLY", bg='black', fg='white')
                sql1 = "DELETE FROM why WHERE sno=%s AND passwords=%s"
                val1 = (1, res1)
                my_cursor.execute(sql1, val1)
                conn.commit()
                pass_enter.destroy()
            else:
                error_label.config(text="INCORRECT PASSWORD. PLEASE TRY AGAIN", bg='black', fg='white')
                pass_enter.delete(0, tk.END)

        ok_btn = tk.Button(pass_open, text="ENTER", command=ok_btn)
        ok_btn.pack()
        error_label = tk.Label(pass_open, text="", font=("Didot", 11), bg="#f2f2f2", fg="#ff0000")
        error_label.pack()

    def b3_click():
        info_label = tk.Label(button_frame, text="", font=("Arial", 12), height=10, width=60, bg='black')
        info_label.pack()

    def b4_click():
        root.quit()

    b1 = tk.Button(button_frame, text="DISABLE USB", font=("Menlo", 11), bg="blue", fg="white", command=b1_click)
    b1.pack(pady=5)
    b2 = tk.Button(button_frame, text="ENABLE USB", font=("Menlo", 11), bg="green", fg="white", command=b2_click)
    b2.pack(pady=5)
    b3 = tk.Button(button_frame, text="PROJECT INFO", font=("Menlo", 11), bg="red", fg="white", command=b3_click)
    b3.pack(pady=5)
    b4 = tk.Button(button_frame, text="EXIT", font=("Menlo", 11), bg="black", fg="white", command=b4_click)
    b4.pack(pady=5)
    button_frame.pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()
