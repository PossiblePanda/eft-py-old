import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from EFT import *
from PIL import Image

# theme

theme = Theme("test_theme.eft")

# window
window = ctk.CTk()
window.title('customtkinter app')
window.geometry('600x400')
window.configure(fg_color=theme.GetColor("Background").GetHex())

# widgets
string_var = ctk.StringVar(value='Primary Color - ' + theme.GetColor("Primary").GetHex())
label = ctk.CTkLabel(
    window,
    text='Primary Color',
    fg_color=theme.GetColor("Primary").GetHex(),
    text_color=('black', 'white'),
    corner_radius=10,
    font=(theme.GetFont("MainFont").GetFont(), theme.GetInt("FontSize")),
    textvariable=string_var)
label.pack()

home_image = ctk.CTkImage(light_image=Image.open(theme.GetImage("HomeIcon").GetImage()),
                                  size=(30, 30))

home_label = ctk.CTkLabel(window, image=home_image, text="")

home_label.pack()

# run
window.mainloop()
