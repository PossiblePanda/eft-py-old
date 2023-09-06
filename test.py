import EFT

Theme = EFT.Theme("test_theme.eft")

print(Theme.GetTitle())

print(Theme.GetColor("Secondary").GetRGB())
