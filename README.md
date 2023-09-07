[![PyPi version](https://badgen.net/pypi/v/EFT-py/)](https://pypi.org/project/EFT-py)

# Easily Formattable Theme - EFT

EFT is a python library that allows developers to easily create themes for their gui applications

You can download EFT by running the following command:
```yml
# Linux/macOS
python3 -m pip install -U eft-py

# Windows
py -3 -m pip install -U eft-py
```

## Why use EFT?

EFT allows the developers, and the users to create themes very easily for GUI applications that have EFT support. It is super easy to implement EFT into your project, and you can customize tons of aspects of your application, such as Colors, Fonts, Images, etc.

## How do I use EFT?

Here's how to get started with using EFT!

### Creating a theme

Creating a theme is simple! You just need to supply the name of the theme, and then any fields that you want!
```eft
- Theme Name

Primary: #fc7b2b : Color
Background: 255,255,255 : Color
MainFont: roboto.ttf : Font
HomeIcon: home.png : Image

FontSize: 16 : Int
Title: My Title : String
```

### Implementing themes
It's super easy to implement themes into your application, with just two lines of code you can grab a color, or any other property from the file!
```py
theme = Theme("my_theme.eft")

Theme.GetColor("Primary").GetHex() # Returns a string containing the hex representation of the color
```
