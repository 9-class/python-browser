from tkinter.ttk import Entry

import webbrowser

def go_to_website():

    webbrowser.open(entry.get())

def back():

    webbrowser.back()

def forward():

    webbrowser.forward()

def refresh():

    webbrowser.refresh()

root = tk.Tk()

root.title("Web Browser")

entry = Entry(root, width=50)

entry.pack(pady=10)

back_button = tk.Button(root, text="Back", command=back)

back_button.pack(side="left", padx=10)

forward_button = tk.Button(root, text="Forward", command=forward)

forward_button.pack(side="left", padx=10)

refresh_button = tk.Button(root, text="Refresh", command=refresh)

refresh_button.pack(side="left", padx=10)

go_button = tk.Button(root, text="Go", command=go_to_website)

go_button.pack(side="left", padx=10)

root.mainloop()

