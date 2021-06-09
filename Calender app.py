import tkinter as tk

root = tk.Tk()
root.title("Calender by @codassassin")
root.iconbitmap('icon.ico')
root.geometry("1100x1000")

Label1 = tk.Label(root, text="Enter the Year: ", font=("times", 15, 'bold'))
Label1.place(relx=0.08, rely=0.01)

e = tk.Entry(root, width=15)
e.place(relx=0.3, rely=0.015)

frame = tk.Frame(root, bg='gray')
frame.place(relwidth=0.98, relheight=0.92, relx=0.005, rely=0.05)


def numberOfDays(monthNumber, year):
    if monthNumber == 1:
        if year < 1752:
            if year % 4 == 0:
                return 29
            else:
                return 28
        else:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                return 29
            else:
                return 28

    elif monthNumber == 0 or monthNumber == 2 or monthNumber == 4 or monthNumber == 6 or monthNumber == 7 or monthNumber == 9 or monthNumber == 11:
        return 31
    else:
        return 30


def dayNumber(year):
    d = 1
    m = 13
    y = year - 1
    k = y % 100
    j = y // 100
    if year <= 1752:
        h = d + 13 * (m + 1) // 5 + k + k // 4 + 5 + 6 * j
    else:
        h = d + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7
    if h == 0:
        return 6
    else:
        return h-1


def getMonthName(monthNumber):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return months[monthNumber]


def getDayName(day_number):
    day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return day[day_number]


def printCalendar():
    year = int(e.get())
    current = dayNumber(year)

    currRow = 0

    for i in range(0, 12, 3):
        currColm = 0
        for m in range(3):
            prevRow = currRow
            prevColm = currColm
            days = numberOfDays(i + m, year)
            tk.Label(frame, text="   -------------------------" + getMonthName(i + m) + "-------------------------",
                     bg="gray").grid(row=currRow,
                                     column=currColm,
                                     columnspan=14)

            currRow += 1
            for f in range(0, 7):
                tk.Label(frame, text="   ", bg="gray").grid(row=currRow, column=currColm)
                currColm += 1
                tk.Label(frame, text=getDayName(f), bg="gray").grid(row=currRow, column=currColm)
                currColm += 1

            currColm = prevColm
            currRow += 1
            c = 0
            for k in range(0, int(current)):
                tk.Label(frame, text="   ", bg="gray").grid(row=currRow, column=currColm)
                currColm += 1
                tk.Label(frame, text="   ", bg="gray").grid(row=currRow, column=currColm)
                currColm += 1
                c += 1

            for j in range(0, days):
                if year == 1752 and i+m == 8:
                    if j in range(2, 13):
                        continue
                tk.Label(frame, text="   ", bg="gray").grid(row=currRow, column=currColm)
                currColm += 1
                tk.Label(frame, text=j + 1, bg="gray").grid(row=currRow, column=currColm)
                currColm += 1
                c += 1
                if c > 6:
                    c = 0
                    currColm = prevColm
                    currRow += 1

            current = c
            if m < 2:
                currRow = prevRow
                currColm = prevColm + 25

        # tk.Label(frame, text="\n").pack()
        currRow = prevRow + 40
    return


button_1 = tk.Button(root, text="Click to Search the Year", command=printCalendar)
button_1.place(relx=0.45, rely=0.01)

root.mainloop()
