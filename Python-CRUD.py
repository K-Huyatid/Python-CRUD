from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import tkinter as tk

# Declare class lists
class hospital_system():
    def __init__(self):
        self.id = []
        self.name = []
        self.room = []
        self.count = 0

    # Gets count value of name
    def get_name(self, count):
        return self.name[count]

    # Gets count value of id
    def get_ID(self, count):
        return self.id[count]

    # Gets count value of room
    def get_room(self, count):
        return self.room[count]

    # Gets count value of count
    def get_count(self):
        return self.__count

    # Function sets the value as count
    def set_count(self, count):
        self.__count = count

    # Appends name to txt file
    def a_name(self, name):
        self.name.append(name)

    # Appends patient ID to txt file
    def a_ID(self, id):
        self.id.append(id)

    # Appends room number to txt file
    def a_room(self, room):
        self.room.append(room)

    # Count value goes up by 1
    def a_add(self):
        self.__count = self.__count + 1

    def edit_data(self, name, room, index):

        self.name[index] = name
        self.room[index] = room

    # Identifies if ID already exists for error handling
    def ID_isDupe(self, id):
        if id in self.id:
            return True
        else:
            return False

    # Identifies if room# already exists for error handling
    def Room_isDupe(self, room):
        if room in self.room:
            return True
        else:
            return False

    # Function to search for ID
    def search(self, id):
        index = 0
        while index < self.get_count():
            if id == self.id[index]:
                return index
            index += 1
        return -1

    # Function to delete a record
    def delete_entry(self, id):
        if id != -1:
            result = id
            # del keyword
            del self.id[result]
            del self.name[result]
            del self.room[result]
            self.__count = self.__count - 1
            messagebox.showinfo("Deleted", "Patient Record successfully removed")
        else:
            messagebox.showerror('Error', 'Patient Record does not exist')

    # writes to txt file
    def update(self, data):
        f = open("patient_records.txt", "w")
        for line in data:
            f.write(line + '\n')
        f.close()

    # gets data from txt file
    def get_data(self):
        lst1 = []
        index = 0
        while index < self.get_count():
            lst1.append(self.id[index] + " " + self.name[index] + " " + self.room[index])
            index += 1
        return lst1

    # updates the file by using data from get_data
    def update_file(self):
        self.update(self.get_data())

    # reads data from txt file - file handling
    def read_data(self):
        try:
            f = open("patient_records.txt", "r+")
            output = f.read().splitlines()
            if output == '':
                messagebox.showerror('Error', 'No Records Found')
            else:
                index = 0
                for fields in output:
                    values = output[index].split(" ")
                    self.a_ID(values[0])
                    self.a_name(values[1])
                    self.a_room(values[2])
                    index += 1
                self.set_count(index)
            f.close()
        except IOError:
            messagebox.showerror('Error', 'No Records Found')

    # displays and functions for radio buttons
    def radio_menu(self):
        self.read_data()
        click = tk.StringVar()
        rad1 = ttk.Radiobutton(self.w, text='Add Patient Record', value=1, variable=click)
        rad1.configure(width=50)
        rad1.place(x=290, y=170)
        rad2 = ttk.Radiobutton(self.w, text='Display Patient Record', value=2, variable=click)
        rad2.configure(width=50)
        rad2.place(x=290, y=200)
        rad3 = ttk.Radiobutton(self.w, text='Update Patient Record', value=3, variable=click)
        rad3.configure(width=50)
        rad3.place(x=290, y=230)
        rad4 = ttk.Radiobutton(self.w, text='Delete Patient Record', value=4, variable=click)
        rad4.configure(width=50)
        rad4.place(x=290, y=260)

        def select():
            if (click.get() == '' or click.get() == 0):
                messagebox.showerror('Error', 'No option chosen')
            else:
                select_button.destroy()
                exit_button.destroy()
                rad1.destroy()
                rad2.destroy()
                rad3.destroy()
                rad4.destroy()
                main_label.destroy()
                self.select_operation(click.get())

        def exit():
            rad1.destroy()
            rad2.destroy()
            rad3.destroy()
            rad4.destroy()
            main_label.destroy()
            select_button.destroy()
            exit_button.destroy()
            self.w.destroy()

        main_label = Label(self.w, text='Patient Record System: Main Menu')
        main_label.place(x=135, y=60)
        main_label.configure(font=("Times", 32))
        select_button = ttk.Button(self.w, text='Confirm', command=select)
        select_button.place(x=297, y=310)
        select_button.configure(width=50)
        exit_button = ttk.Button(self.w, text='Exit', command=exit)
        exit_button.place(x=297, y=350)
        exit_button.configure(width=50)

    # Takes value from radio button to determine which function to run
    def select_operation(self, value):
        if value == '1':
            self.add_record()
        elif value == '2':
            self.display_record()
        elif value == '3':
            self.update_record()
        elif value == '4':
            self.delete_record()

    # Function 1 for adding record
    def add_record(self):
        self.w.title("Set Information")
        self.read_data()
        main_label = Label(self.w, text='Patient Record System: Add Record')
        main_label.place(x=135, y=60)
        main_label.configure(font=("Times", 32))
        id_label = Label(self.w, text='ID: ', width=5)
        id_label.place(x=300, y=160)
        id_label.configure(font=("Times", 15))
        id_entry = tk.Entry(self.w, width=25)
        id_entry.configure(font=("Times", 15))
        id_entry.place(x=385, y=160)
        name_label = Label(self.w, text='Name: ')
        name_label.place(x=300, y=205)
        name_label.configure(font=("Times", 15))
        name_box = tk.Entry(self.w, width=25)
        name_box.configure(font=("Times", 15))
        name_box.place(x=385, y=205)
        room_label = Label(self.w, text='Room: ')
        room_label.place(x=300, y=250)
        room_label.configure(font=("Times", 15))
        room_entry = tk.Entry(self.w, width=25)
        room_entry.configure(font=("Times", 15))
        room_entry.place(x=385, y=250)

        def save(id, name, room):
            if self.ID_isDupe(id):
                messagebox.showerror('Error', 'Patient Record already exists')
            elif id.isnumeric() == False:
                messagebox.showerror('Error', 'Numeric ID only')
            elif name == '' or name.isnumeric() or name.strip() == '':
                messagebox.showerror('Error', 'Error: PLease input valid name')
            elif self.Room_isDupe(room):
                messagebox.showerror('Error', 'Room already occupied')
            elif room == '' or room.isnumeric() == False:
                messagebox.showerror('Error', 'Error: PLease input valid number')
            else:
                messagebox.showinfo("Success!", "Successfully added!")
                main_label.destroy()
                id_label.destroy()
                id_entry.destroy()
                name_label.destroy()
                name_box.destroy()
                room_label.destroy()
                room_entry.destroy()
                add_button.destroy()
                cancel_button.destroy()
                self.a_ID(id)
                name1 = name.replace(" ", "")
                self.a_name(name1)
                self.a_room(room)
                self.a_add()
                self.update_file()
                self.radio_menu()

        def cancel():
            main_label.destroy()
            id_label.destroy()
            id_entry.destroy()
            name_label.destroy()
            name_box.destroy()
            room_label.destroy()
            room_entry.destroy()
            add_button.destroy()
            cancel_button.destroy()
            self.radio_menu()

        add_button = ttk.Button(self.w, text='Save', command=lambda: save(id_entry.get(), name_box.get(), room_entry.get()))
        add_button.place(x=395, y=300)
        cancel_button = ttk.Button(self.w, text='Back', command=cancel)
        cancel_button.place(x=495, y=300)

    # Function for displaying all records
    def display_record(self):
        self.read_data()
        self.w.title("Display Patients:")
        count = 0
        display = 'PATIENT ID\t\tNAME\t\tROOM NO.\n--------------------------------------------------------------------------'
        while count < self.get_count():
            display = display + self.get_ID(count) + " \t\t" + self.get_name(count) + " \t\t" + self.get_room(
                count) + '\n'
            count = count + 1
        textbox = Text(self.w, height=21, width=74)
        textbox.insert(END, display)
        textbox.place(x=163, y=25)

        def back():
            textbox.destroy()
            back_button.destroy()
            self.radio_menu()

        back_button = ttk.Button(self.w, text='Back', command=back)
        back_button.place(x=415, y=375)

    # Update Records
    def update_record(self):
        self.read_data()
        self.w.title("Edit Information")
        id = askstring('ID', 'Search ID \t\t\t')
        value = int(self.search(id))

        if value != -1 and value != '': # Checks if ID is blank or negative

            main_label = Label(self.w, text='Patient Record System: Update Record')
            main_label.place(x=135, y=60)
            main_label.configure(font=("Times", 32))
            id_label = Label(self.w, text='ID: ', width=5)
            id_label.place(x=300, y=160)
            id_label.configure(font=("Times", 15))
            id_entry = Text(self.w, width=25)
            id_entry.insert(END, self.get_ID(value))
            id_entry.configure(font=("Times", 15), height=1)
            id_entry.place(x=385, y=160)
            name_label = Label(self.w, text='Name: ')
            name_label.place(x=300, y=205)
            name_label.configure(font=("Times", 15))
            name_box = tk.Entry(self.w, width=25)
            name_box.configure(font=("Times", 15))
            name_box.place(x=385, y=205)
            room_label = Label(self.w, text='Room: ')
            room_label.place(x=300, y=250)
            room_label.configure(font=("Times", 15))
            room_entry = tk.Entry(self.w, width=25)
            room_entry.configure(font=("Times", 15))
            room_entry.place(x=385, y=250)

            def save(name, room):

                if name == '' and name.isnumeric():
                    messagebox.showerror('Error', 'Name can not be numerical')
                elif room == '':
                    messagebox.showerror('Error', 'Enter valid room number')
                elif room.isnumeric() == False:
                    messagebox.showerror('Error', 'Enter valid room number')
                else:
                    messagebox.showinfo("Updated", "Patient Record " + id + " updated")
                    main_label.destroy()
                    id_label.destroy()
                    id_entry.destroy()
                    name_label.destroy()
                    name_box.destroy()
                    room_label.destroy()
                    room_entry.destroy()
                    update_button.destroy()
                    cancel_button.destroy()
                    self.edit_data(name, room, value)
                    self.update_file()
                    self.radio_menu()

            def cancel():
                main_label.destroy()
                id_label.destroy()
                id_entry.destroy()
                name_label.destroy()
                name_box.destroy()
                room_label.destroy()
                room_entry.destroy()
                update_button.destroy()
                cancel_button.destroy()
                self.radio_menu()

            update_button = ttk.Button(self.w, text='Update Record', command=lambda: save(name_box.get(), room_entry.get()))
            update_button.place(x=395, y=300)

            cancel_button = ttk.Button(self.w, text='Back', command=cancel)
            cancel_button.place(x=495, y=300)

        else:
            messagebox.showerror('Error', 'Error: No patient record found')
            self.radio_menu()

    # Function to delete a record
    def delete_record(self):    # Delete row from txt file
        self.w.title("Delete information")
        self.read_data()

        def delete():
            try:
                # Function to ask string from user
                id = askstring('ID', 'Search ID ')
                if self.get_count() == 0 or id == -1 or id == '':
                    messagebox.showerror('Error', 'Patient Record does not exist')
                elif id.isnumeric() == True:
                    result = self.search(id)
                    self.delete_entry(result)
                    self.update_file()
                else:
                    messagebox.showerror('Error', 'Numerical ID only')
            except Exception as e:
                messagebox.showerror('Error', 'Patient Record does not exist')

        def back():
            notice_label.destroy()
            main_label.destroy()
            delete_button.destroy()
            back_button.destroy()
            self.radio_menu()

        main_label = Label(self.w, text='Patient Record System: Delete Record')
        main_label.place(x=135, y=60)
        main_label.configure(font=("Times", 32))

        notice_label = Label(self.w, text='Warning: Record will be permanently removed from the system after deletion')
        notice_label.place(x=205, y=150)
        notice_label.configure(font=("Times", 13))

        delete_button = ttk.Button(self.w, text='Delete Patient Record', command=delete)
        delete_button.place(x=285, y=250)
        delete_button.configure(width=50)

        back_button = ttk.Button(self.w, text='Back', command=back)
        back_button.place(x=285, y=300)
        back_button.configure(width=50)

    # destroys widgets
    def destroy(self):
        self.main_label.destroy()
        self.notice_label.destroy()
        self.username.destroy()
        self.user_input.destroy()
        self.password.destroy()
        self.pass_input.destroy()
        self.login_button.destroy()

    #Function to create argument for login
    def menu(self, user, password):

        if user == 'admin' and password == '12345678':
            messagebox.showinfo("Log in Window", "Welcome, " + user)
            self.destroy()
            self.radio_menu()

        else:
            messagebox.showerror('Error', 'Invalid Credentials')



    # Displays GUI
    def disp(self):
        self.w = Tk()
        self.w.geometry('900x420')
        self.w.title("Kyle Hospital Record System")
        self.w.eval('tk::PlaceWindow . center')
        self.w.configure(background='light blue')
        self.main_label = Label(self.w, text='Kyle Hospital Patient Record System')
        self.main_label.place(x=135, y=60)
        self.main_label.configure(font=("Times", 32))
        self.notice_label = Label(self.w, text='Please Enter Login Credentials')
        self.notice_label.place(x=363, y=175)
        self.notice_label.configure(font=("Times", 10))
        self.username = Label(self.w, text='Username: ', width=13)
        self.username.place(x=299, y=210)
        self.user_input = tk.Entry(self.w, width=30)
        self.user_input.place(x=405, y=210)
        self.password = Label(self.w, text='Password: ', width=13)
        self.password.place(x=299, y=250)
        self.pass_input = tk.Entry(self.w, width=30, show='*')
        self.pass_input.place(x=405, y=250)
        self.login_button = ttk.Button(self.w, text='Login', command=self.login, width=50)
        self.login_button.place(x=284, y=280)
        self.w.mainloop()

    # function run login
    def login(self):
        hospital.menu(self.user_input.get(), self.pass_input.get())

# Main
if __name__ == "__main__":
    hospital = hospital_system()
    hospital.disp()
