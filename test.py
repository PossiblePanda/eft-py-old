from EFT.EFT import *
theme = Theme("Examples/Simple GUI/test_theme.eft")

print(theme.GetTitle())

print(theme.GetColor("Primary"))
print(theme.GetColor("Background"))
print(theme.GetFont("MainFont"))
print(theme.GetImage("HomeIcon"))
print(theme.GetInt("FontSize"))
