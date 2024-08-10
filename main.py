import webbrowser
import tkinter as tk

websites_terpercaya = [
    'reddit.com',
    'stockoverflow.com',
    'medium.com',
    'github.com',
    'stackexchange.com',
]

url = "https://www.google.com/search?q="

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def create_filter():
    filter = '('
    for index, website in enumerate(websites_terpercaya):
        filter += 'site:' + website
        if index == len(websites_terpercaya) - 1:
            filter += ')'
        else:
            filter += ' OR '
    return filter

def create_url(query):
    final_url = url + query + create_filter()
    webbrowser.get(chrome_path).open(final_url)

def search():
    query = entry.get()
    if len(query.strip()) == 0:
        error_label.config(text='Error: Please enter a valid search query')
    else:
        create_url(query)

# Create the GUI window
window = tk.Tk()
window.title("Search App")

# Create the search box
entry = tk.Entry(window, font=("Arial", 16), width=50)
entry.pack(pady=20)

# Create the search button
button = tk.Button(window, text="Search", font=("Arial", 16), command=search)
button.pack()

# Create the error label
error_label = tk.Label(window, font=("Arial", 14), fg='red')
error_label.pack(pady=20)

# Start the GUI main loop
window.mainloop()
