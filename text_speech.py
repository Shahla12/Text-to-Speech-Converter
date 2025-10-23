import tkinter as tk            # Python’s built-in library for making GUI windows.
import pyttsx3              # A text-to-speech conversion library in Python working offline.


engine = pyttsx3.init()              #start the pyttsx3 engine
engine.setProperty('rate', 130)  # default ~200

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  #  # 0 = male, 1 = female (varies by system)


# Create the main window
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry('600x300')
root.resizable(False, False)
root.configure(bg="#819A91")
try:
    root.iconbitmap(r"C:\Text to Speech Converter\icon.ico")
  # Set the window icon (make sure you have an 'icon.ico' file in the same directory)
except:
    pass

# Placeholder text
placeholder = "Enter the text"


entry = tk.Text(        # multi-line text box
    root,
      height=10,         # number of text lines
        width=60,       # number of characters per line
        font=("Arial", 10),
        fg="grey",      # Placeholder text color
        )
entry.pack(pady=10)             #Adds spacing around it.

entry.insert('1.0', placeholder)  # Insert placeholder text at the beginning


# Function to convert text to speech
def speak_text():
    text = entry.get('1.0','end-1c')  # Get text from the text box( "1.0" → start from line 1, character 0. "end-1c" → up to the end minus 1 character to avoid capturing the newline character)
    if text.strip() and text != placeholder:  # Check if the text is not empty and ignore placeholder
        engine.say(text)            #Sends text to speech engine.
        engine.runAndWait()     # play the text


# When clicked, remove placeholder
def on_click(event):
    if entry.get("1.0", "end-1c") == placeholder:       # gets all the text from the text box.
        entry.delete("1.0", "end")          # delete all text from the text box.
        entry.config(fg="black")            #Sets the text color to black, At first, placeholder is shown in grey.Once the user starts typing, it switches to normal typing color.


# Create a button to trigger the speech conversion
speak_button = tk.Button(root, text='Speak', command= speak_text, bg="#0E240F", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=5)
speak_button.pack(pady=10)


# When the text box gets focus, remove placeholder if present
def on_focus_in(event):
    if entry.get("1.0", "end-1c") == placeholder:
        entry.delete("1.0", "end")
        entry.config(fg="black")



# When focus leaves, restore placeholder if empty
def on_focus_out(event):
    new = root.focus_get()
    if new == speak_button:
        # focus moved to speak button — don't reinsert placeholder (so speak_text sees the typed text)
        return
    if not entry.get("1.0", "end-1c").strip():
        entry.insert("1.0", placeholder)
        entry.config(fg="grey")



entry.bind("<FocusOut>", on_focus_out)          #restore placeholder
entry.bind("<FocusIn>", on_focus_in)       #remove placeholder

  

# Start the Tkinter event loop
root.mainloop()





