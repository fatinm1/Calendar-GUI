from tkinter import *
from tkinter import messagebox, simpledialog
import calendar

# Global dictionary to store notes {date: note}
notes = {}

def showCalendar():
    year = int(year_field.get())
    my_calendar = calendar.calendar(year)
    cal_window = Toplevel(new)
    cal_window.title("Calendar")
    cal_window.config(background='grey')
    cal_window.geometry("600x650")
    Label(cal_window, text=my_calendar, font="Consolas 10", bg='light grey').pack()

    # Additional functionality to display notes
    def checkNote():
        date = simpledialog.askstring("Check Note", "Enter date (dd/mm) to check note:")
        note = notes.get(f"{date}/{year}", "No note for this date.")
        messagebox.showinfo("Note", note)

    Button(cal_window, text="Check Note", command=checkNote).pack()

def addNote():
    note_window = Toplevel(new)
    note_window.title("Add Note")
    note_window.config(background='grey')
    note_window.geometry("300x200")
    Label(note_window, text="Date (dd/mm):", bg='dark grey').pack()
    date_entry = Entry(note_window)
    date_entry.pack()
    Label(note_window, text="Note:", bg='dark grey').pack()
    note_entry = Entry(note_window)
    note_entry.pack()
    Button(note_window, text="Save Note", command=lambda: saveNote(date_entry.get(), note_entry.get(), note_window)).pack()

def saveNote(date, note, window):
    # Save the note in the global dictionary
    year = year_field.get()
    notes[f"{date}/{year}"] = note
    messagebox.showinfo("Note Saved", f"Note for {date}/{year} saved.")
    window.destroy()

if __name__ == '__main__':
    new = Tk()
    new.title("Calendar and Notes")
    new.config(background='grey')
    new.geometry("250x180")
    
    Label(new, text="Calendar and Notes", bg='grey', font=("times", 20, "bold")).pack()
    Label(new, text="Enter year", bg='dark grey').pack()
    year_field = Entry(new)
    year_field.pack()
    Button(new, text='Show Calendar', fg='Black', bg='Blue', command=showCalendar).pack()
    Button(new, text='Add Note', fg='Black', bg='Green', command=addNote).pack()
    Button(new, text="Exit", bg="red", fg="white", command=new.quit).pack()

    new.mainloop()
