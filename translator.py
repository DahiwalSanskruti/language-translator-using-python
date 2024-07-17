import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translate_text():
    input_text = input_text_box.get("1.0", tk.END).strip()
    src_lang = src_lang_combobox.get()
    dest_lang = dest_lang_combobox.get()

    if not input_text:
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, "Please enter text to translate.")
        return

    translator = Translator()
    try:
        # Get the language codes from the language names
        src_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(src_lang)]
        dest_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(dest_lang)]

        translated = translator.translate(input_text, src=src_lang_code, dest=dest_lang_code)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translated.text)
    except Exception as e:
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, f"Error: {str(e)}")

# Set up the main application window
root = tk.Tk()
root.title("Translator")

# Create and place input text box
input_text_box = tk.Text(root, height=10, width=50)
input_text_box.pack(pady=10)

# Create and place source language dropdown
src_lang_label = tk.Label(root, text="Source Language")
src_lang_label.pack()
src_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()))
src_lang_combobox.set("english")
src_lang_combobox.pack()

# Create and place destination language dropdown
dest_lang_label = tk.Label(root, text="Destination Language")
dest_lang_label.pack()
dest_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()))
dest_lang_combobox.set("spanish")
dest_lang_combobox.pack()

# Create and place translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Create and place output text box
output_text_box = tk.Text(root, height=10, width=50)
output_text_box.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
