from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS STUDENT_RECORDS")
mycursor.execute("USE STUDENT_RECORDS")
mycursor.execute("CREATE TABLE IF NOT EXISTS STU (ROLL_NO INT PRIMARY KEY NOT NULL, NAME VARCHAR(255), COURSE VARCHAR(255), EMAIL VARCHAR(255), GENDER VARCHAR(255), CONTACT VARCHAR(255), DOB VARCHAR(255), ADDRESS VARCHAR(255))")

class Students:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        color = "#210070"
        text_color="WHITE"

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"), bg=color, fg=text_color)
        title.pack(side=TOP, fill=X)

#=================All Variables
        self.Roll_no_var = StringVar()
        self.name_var = StringVar()
        self.course_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.searchby_var = StringVar()
        self.searchtxt_var = StringVar()

#=================MANAGE FRAME
        self.Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=color)
        self.Manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title = Label(self.Manage_Frame, text="Manage Students", bd=10, font=("times new roman", 30, "bold"), bg=color, fg=text_color)
        m_title.grid(row=0,columnspan=2,pady=0)

        lbl_roll = Label(self.Manage_Frame, text="ROLL NO.", font=("times new roman", 20, "bold"), bg=color, fg=text_color)
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(self.Manage_Frame, textvariable=self.Roll_no_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(self.Manage_Frame, text="Name", font=("times new roman", 20, "bold"), bg=color, fg=text_color)
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(self.Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_course = Label(self.Manage_Frame, text="Course", font=("times new roman", 20, "bold"), bg=color, fg=text_color)
        lbl_course.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_course = Entry(self.Manage_Frame, textvariable=self.course_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_course.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(self.Manage_Frame, text="Email", font=("times new roman", 20, "bold"), bg=color, fg=text_color)
        lbl_Email.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(self.Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(self.Manage_Frame, text="Gender", font=("times new roman", 20, "bold"), bg=color, fg=text_color)
        lbl_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(self.Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"), state="readonly")
        combo_gender['values']=("Male", "Female", "Other")
        combo_gender.grid(row=5, column=1, pady=10, padx=20)

        lbl_contact = Label(self.Manage_Frame, text="Contact", font=("times new roman", 20, "bold"), bg=color, fg=text_color)
        lbl_contact.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(self.Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(self.Manage_Frame, text="D.O.B", font=("times new roman", 20, "bold"), bg=color, fg=text_color)
        lbl_dob.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(self.Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(self.Manage_Frame, text="Address", font=("times new roman", 20, "bold"), bg=color, fg=text_color)
        lbl_address.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(self.Manage_Frame, font=("", 10, "bold"), height=3, width=30)
        self.txt_address.grid(row=8, column=1, pady=10, padx=20, sticky="w")

#=================BUTTON FRAME
        self.btn_Frame = Frame(self.Manage_Frame, bd=4, relief=RIDGE, bg=color)
        self.btn_Frame.place(x=18,y=540,width=420)

        add_btn = Button(self.btn_Frame, text="ADD", width=10, command=self.add_students).grid(row=0, column=0, padx=10, pady=5)
        update_btn = Button(self.btn_Frame, text="UPDATE", width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=5)
        delete_btn = Button(self.btn_Frame, text="DELETE", width=10, command=self.delete_data).grid(row=0, column=2, padx=10, pady=5)
        clear_btn = Button(self.btn_Frame, text="CLEAR", width=10, command=self.clear_data).grid(row=0, column=3, padx=10, pady=5)

#==================ON OFF BUTTON FRAME
        on_off_btn_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='red')
        on_off_btn_Frame.place(x=1305,y=100,width=55, height=70)

        on_btn = Button(on_off_btn_Frame, text='ON', command=self.on_all).pack(fill=X, side=TOP)
        off_btn = Button(on_off_btn_Frame, text='OFF', command=self.off_all).pack(fill=X, side=BOTTOM)

#=================DETAIL FRAME
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=color)
        self.Detail_Frame.place(x=500,y=100, width=800, height=600)

        lbl_search = Label(self.Detail_Frame, text="Search By", font=("times new roman", 20, "bold"), bg=color, fg=text_color)
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(self.Detail_Frame, width=10, font=("times new roman", 13, "bold"), state="readonly", textvariable=self.searchby_var)
        combo_search['values']=("ROLL_NO", "NAME", "CONTACT")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(self.Detail_Frame, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE, textvariable=self.searchtxt_var)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(self.Detail_Frame, text="SEARCH", width=10, pady=5, command=self.search_data).grid(row=0, column=3, padx=10, pady=5)
        showall_btn = Button(self.Detail_Frame, text="SHOW ALL", width=10, pady=5, command= self.fetch_data).grid(row=0, column=4, padx=10, pady=5)

#=================TABLE FRAME
        Table_Frame = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="black")
        Table_Frame.place(x=10,y=70, width=760, height=500)

        scrollx = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=("Roll", "Name", "Course", "Email", "Gender", "Contact", "dob", "Address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.Student_table.pack(fill=BOTH, expand=1)
        scrollx.config(command=self.Student_table.xview)
        scrolly.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll", text="Roll No.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Course", text="Course")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")

        self.Student_table['show']='headings'
        self.Student_table.column("Roll", width=100)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Course", width=100)
        self.Student_table.column("Email", width=100)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
        self.clear_data()

    def add_students(self):
        if self.Roll_no_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.dob_var.get()=="" or len(self.txt_address.get('1.0', END))==1:
            messagebox.showerror("Error", "All fields are mandatory.")
        else:
            try:
                mycursor.execute("INSERT INTO STU VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_no_var.get(),
                                                                                 self.name_var.get(),
                                                                                 self.course_var.get(),
                                                                                 self.email_var.get(),
                                                                                 self.gender_var.get(),
                                                                                 self.contact_var.get(),
                                                                                 self.dob_var.get(),
                                                                                 self.txt_address.get('1.0',END)
                                                                                 ))
                mydb.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo("Success", "Record has been added.")
            except Exception as e:
                print(e)
                messagebox.showerror("Invalid Entry", "Either this Roll_no already exist or invalid input.")

    def fetch_data(self):
        mycursor.execute("SELECT * FROM STU")
        rows = mycursor.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            mydb.commit()

    def clear_data(self):
        self.Roll_no_var.set("")
        self.name_var.set("")
        self.course_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0", END)

    def get_cursor(self, ev):
        contents = self.Student_table.item(self.Student_table.focus())      #.focus highlight the row/data and .item returns the highlighted row/data
        row = contents['values']
        self.Roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.course_var.set(row[2])
        self.email_var.set(row[3])
        self.gender_var.set(row[4])
        self.contact_var.set(row[5])
        self.dob_var.set(row[6])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[6])

    def update_data(self):

        mycursor.execute("UPDATE STU SET NAME=%s, COURSE=%s, EMAIL=%s, GENDER=%s, CONTACT=%s, DOB=%s, ADDRESS=%s WHERE ROLL_NO=%s",(
                                                                                                     self.name_var.get(),
                                                                                                     self.course_var.get(),
                                                                                                     self.email_var.get(),
                                                                                                     self.gender_var.get(),
                                                                                                     self.contact_var.get(),
                                                                                                     self.dob_var.get(),
                                                                                                     self.txt_address.get('1.0', END),
                                                                                                     self.Roll_no_var.get()
                                                                                                     ))
        mydb.commit()
        self.fetch_data()
        self.clear_data()

    def delete_data(self):
        mycursor.execute("DELETE FROM STU WHERE ROLL_NO=%s", (self.Roll_no_var.get(),))   #will show sql syntax error if ',' is not used in parameter part bcoz it needs parameters as tuples even for single parameter
        mydb.commit()
        self.fetch_data()
        self.clear_data()

    def search_data(self):
        print(type(self.searchby_var.get()))
        mycursor.execute(f"SELECT * FROM STU WHERE {self.searchby_var.get()} =%s", (self.searchtxt_var.get(),))
        rows = mycursor.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            mydb.commit()

    def on_all(self):
        self.Manage_Frame.place(x=20, y=100, width=450, height=600)
        self.Detail_Frame.place(x=500, y=100, width=800, height=600)

    def off_all(self):
        self.Manage_Frame.place(x=5000, y=100, width=760, height=500)
        self.Detail_Frame.place(x=5000, y=100, width=800, height=600)


root = Tk()
st = Students(root)
root.mainloop()