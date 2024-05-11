import tkinter as tk
from tkinter import messagebox

"""
Application Name: TimeSlotSyn
Author: Philip Lian
Date: 05/11/2024
Desription: This program allows user to make, edit, and delete appoitment schedules.
"""
class AppointmentScheduler(tk.Tk):
    """Main class for the TimeSlotSyn."""

    def __init__(self):
        # Initialize the application
        super().__init__()
        self.title("TimeSlotSyn") # Set the tile of the App
        self.appointments = []  # List to store appointments

        # Welcome screen and introduction
        self.welcomeScreen()

        # Set geometry layout for the window
        self.geometry("600x400")

    def welcomeScreen(self):
        # Display the welcome screen
        
        self.window()

        
        welcomeLabel = tk.Label(self, text="Welcome to the TimeSlotSyn!", font=("Arial", 16))
        welcomeLabel.pack(pady=20)

        introLabel = tk.Label(self, text="This application helps you manage appointments.")
        introLabel.pack(pady=20)

        menuButton = tk.Button(self, text="Menu", command=self.dashboard)
        menuButton.pack(pady=20)

    def dashboard(self):
        # Display the dashboard
        self.window()
        dashboardLabel = tk.Label(self, text="Dashboard", font=("arial", 14))
        dashboardLabel.pack(pady=20)
        
        # Display options for the user
        upcomingLabel = tk.Label(self, text="Options:")
        upcomingLabel.pack()

        # All the buttons for navigation to different funtionalities
        scheduleButton = tk.Button(self, text="Schedule Appointment", command=self.scheduling)
        scheduleButton.pack(pady=20)

        viewCalendarButton = tk.Button(self, text="View Calendar", command=self.calendar)
        viewCalendarButton.pack(pady=20)

        manageClientsButton = tk.Button(self, text="Manage Clients", command=self.clients)
        manageClientsButton.pack(pady=20)

        exitButton = tk.Button(self, text="Exit", command=self.exitApp)
        exitButton.pack(pady=20)

    def exitApp(self):
        # Exit the application
        self.destroy()

    def scheduling(self):
        # Display the appointment scheduling form
        self.window()
        appointmentLabel = tk.Label(self, text="Schedule Appointment", font=("arial", 14))
        appointmentLabel.pack(pady=10)

        nameLabel = tk.Label(self, text="Name:")
        nameLabel.pack()
        self.nameEntry = tk.Entry(self, bg="gray")
        self.nameEntry.pack()

        dobLabel = tk.Label(self, text="Date of Birth (MM/DD/YYYY):")
        dobLabel.pack()
        self.dobEntry = tk.Entry(self, bg="gray")
        self.dobEntry.pack()

        phNumberLabel = tk.Label(self, text="Phone Number:")
        phNumberLabel.pack()
        self.phNumberEntry = tk.Entry(self, bg="gray")
        self.phNumberEntry.pack()

        dateLabel = tk.Label(self, text="Appointment Date (MM/DD/YYYY):")
        dateLabel.pack()
        self.dateEntry = tk.Entry(self, bg="gray")
        self.dateEntry.pack()

        timeLabel = tk.Label(self, text="Appointment Time (HH:MM AM/PM):")
        timeLabel.pack()
        self.timeEntry = tk.Entry(self, bg="gray")
        self.timeEntry.pack()

        self.confirmButton = tk.Button(self, text="Confirm", command=self.confirmation, state="disabled")
        self.confirmButton.pack(pady=10)

        backButton = tk.Button(self, text="Back to Dashboard", command=self.dashboard)
        backButton.pack(pady=10)

        # Enable confirm button only when all fields have input
        self.nameEntry.bind("<KeyRelease>", self.checkInput)
        self.dobEntry.bind("<KeyRelease>", self.checkInput)
        self.phNumberEntry.bind("<KeyRelease>", self.checkInput)
        self.dateEntry.bind("<KeyRelease>", self.checkInput)
        self.timeEntry.bind("<KeyRelease>", self.checkInput)

    def checkInput(self, event):
        # Enable confirm button only when all fields have input
        if self.nameEntry.get() and self.dobEntry.get() and self.phNumberEntry.get() and self.dateEntry.get() and self.timeEntry.get():
            self.confirmButton.config(state="normal")
        else:
            self.confirmButton.config(state="disabled")

    def confirmation(self):
        # Store the scheduled appointment and display confirmation
        name = self.nameEntry.get()
        dob = self.dobEntry.get()
        phNumber = self.phNumberEntry.get()
        date = self.dateEntry.get()
        time = self.timeEntry.get()

        # Validate input and add appointment to the list
        if not self.validateInput(name, dob, phNumber, date, time):
            return

        #Add appoitments
        self.appointments.append({"Name": name, "DOB": dob, "Phone Number": phNumber, "Date": date, "Time": time})

        # Display confirmation message
        self.window()
        confirmationLabel = tk.Label(self, text="Appointment Scheduled!", font=("arial", 14))
        confirmationLabel.pack(pady=10)

        okButton = tk.Button(self, text="OK", command=self.dashboard)
        okButton.pack(pady=10)
    
    # ALl Validations
    def validateInput(self, name, dob, phNumber, date, time):
        # Validate input fields for letters only
        if not name or not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Please enter a valid name (only letters allowed).")
            return False

        # Validate date of birth
        if not dob or not self.isValidDate(dob):
            messagebox.showerror("Error", "Please enter a valid date of birth (MM/DD/YYYY).")
            return False
        # Validete phone number
        if not phNumber or not self.isValidPhoneNumber(phNumber):
            messagebox.showerror("Error", "Please enter a valid phone number.")
            return False
        # Validate the date
        if not date or not self.isValidDate(date):
            messagebox.showerror("Error", "Please enter a valid appointment date (MM/DD/YYYY).")
            return False
        #Validate the time
        if not time or not self.isValidTime(time):
            messagebox.showerror("Error", "Please enter a valid appointment time (HH:MM AM/PM).")
            return False

        return True

    # Helper methods for input validation
    def isValidDate(self, date):
        # Validate date format (MM/DD/YYYY)
        try:
            mm, dd, yyyy = map(int, date.split('/'))
            if mm < 1 or mm > 12 or dd < 1 or dd > 31 or yyyy < 1900:
                return False
        except ValueError:
            return False
        return True

    def isValidPhoneNumber(self, phoneNumber):
        # Validate phone number format (numeric characters only)
        return phoneNumber.isdigit() and len(phoneNumber) == 10

    def isValidTime(self, time):
        # Validate time format (HH:MM AM/PM)
        try:
            hhmm, ampm = time.split()
            hh, mm = map(int, hhmm.split(':'))
            if hh < 1 or hh > 12 or mm < 0 or mm > 59 or (ampm != 'AM' and ampm != 'PM'):
                return False
        except ValueError:
            return False
        return True

    def calendar(self):
        # Display the calendar view
        self.window()
        calendarLabel = tk.Label(self, text="View Calendar", font=("arial", 14))
        calendarLabel.pack(pady=10)

        # Display headers
        headers = ["Name", "DOB", "Phone Number", "Date", "Time"]
        headerLabel = tk.Label(self, text=" - ".join(headers))
        headerLabel.pack()

        # Display scheduled appointments with corresponding information
        for appointment in self.appointments:
            infoLabel = tk.Label(self, text=f"{appointment['Name']} - {appointment['DOB']} - {appointment['Phone Number']} - {appointment['Date']} - {appointment['Time']}")
            infoLabel.pack()

        backButton = tk.Button(self, text="Back to Dashboard", command=self.dashboard)
        backButton.pack(pady=10)

    def clients(self):
        # Display the client management interface
        self.window()
        clientsLabel = tk.Label(self, text="Manage Clients", font=("arial", 14))
        clientsLabel.pack(pady=10)

        # Display a list of all existing clients with options to edit or delete each one
        for index, appointment in enumerate(self.appointments):
            clientFrame = tk.Frame(self)
            clientFrame.pack(pady=5)

            nameLabel = tk.Label(clientFrame, text=f"Name: {appointment['Name']}")
            nameLabel.grid(row=0, column=0, padx=5, pady=2, sticky="w")

            dobLabel = tk.Label(clientFrame, text=f"DOB: {appointment['DOB']}")
            dobLabel.grid(row=0, column=1, padx=5, pady=2, sticky="w")

            phNumberLabel = tk.Label(clientFrame, text=f"Phone Number: {appointment['Phone Number']}")
            phNumberLabel.grid(row=0, column=2, padx=5, pady=2, sticky="w")

            dateLabel = tk.Label(clientFrame, text=f"Appointment Date: {appointment['Date']}")
            dateLabel.grid(row=1, column=0, padx=5, pady=2, sticky="w")

            timeLabel = tk.Label(clientFrame, text=f"Appointment Time: {appointment['Time']}")
            timeLabel.grid(row=1, column=1, padx=5, pady=2, sticky="w")

            editButton = tk.Button(clientFrame, text="Edit", command=lambda idx=index: self.editClient(idx))
            editButton.grid(row=1, column=2, padx=5, pady=2)

            deleteButton = tk.Button(clientFrame, text="Delete", command=lambda idx=index: self.deleteClient(idx))
            deleteButton.grid(row=1, column=3, padx=5, pady=2)

        backButton = tk.Button(self, text="Back to Dashboard", command=self.dashboard)
        backButton.pack(pady=10)

    def editClient(self, index):
        # Display the editing interface for a selected client
        appointment = self.appointments[index]
        self.window()
        editLabel = tk.Label(self, text="Edit Client", font=("arial", 14))
        editLabel.pack(pady=10)

        nameLabel = tk.Label(self, text="Name:")
        nameLabel.pack()
        self.nameEntry = tk.Entry(self)
        self.nameEntry.insert(0, appointment['Name'])
        self.nameEntry.pack()

        dobLabel = tk.Label(self, text="Date of Birth (MM/DD/YYYY):")
        dobLabel.pack()
        self.dobEntry = tk.Entry(self)
        self.dobEntry.insert(0, appointment['DOB'])
        self.dobEntry.pack()

        phNumberLabel = tk.Label(self, text="Phone Number:")
        phNumberLabel.pack()
        self.phNumberEntry = tk.Entry(self)
        self.phNumberEntry.insert(0, appointment['Phone Number'])
        self.phNumberEntry.pack()

        dateLabel = tk.Label(self, text="Appointment Date (MM/DD/YYYY):")
        dateLabel.pack()
        self.dateEntry = tk.Entry(self)
        self.dateEntry.insert(0, appointment['Date'])
        self.dateEntry.pack()

        timeLabel = tk.Label(self, text="Appointment Time (HH:MM AM/PM):")
        timeLabel.pack()
        self.timeEntry = tk.Entry(self)
        self.timeEntry.insert(0, appointment['Time'])
        self.timeEntry.pack()

        saveButton = tk.Button(self, text="Save Changes", command=lambda: self.saveChanges(index))
        saveButton.pack(pady=10)

    def saveChanges(self, index):
        # Save changes made to the client's information
        name = self.nameEntry.get()
        dob = self.dobEntry.get()
        phNumber = self.phNumberEntry.get()
        date = self.dateEntry.get()
        time = self.timeEntry.get()
        
        # Validate the iput
        if not self.validateInput(name, dob, phNumber, date, time):
            return
        # Update client infomation in the list
        self.appointments[index] = {
            "Name": name,
            "DOB": dob,
            "Phone Number": phNumber,
            "Date": date,
            "Time": time
        }
        messagebox.showinfo("Success", "Changes saved successfully.")
        self.clients()

    def deleteClient(self, index):
        # Delete a client from the list
        del self.appointments[index]
        messagebox.showinfo("Success", "Client deleted successfully.")
        self.clients()

    def window(self):
        # Clear the screen
        for win in self.winfo_children():
            win.destroy()

def main():
    AppointmentScheduler().mainloop()

if __name__ == "__main__":
    main()
