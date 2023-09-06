import re


class ColorField:
    def __init__(self, color: str):
        hex_pattern = r"#(?:[A-Fa-f0-9]{3}){1,2}\b"
        rgb_pattern = r"^(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(?:,\s?(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])){2}$"
        if re.match(hex_pattern, color):
            self.hex = color
            h = color.lstrip('#')
            self.rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        elif re.match(rgb_pattern, color):
            self.rgb = [int(x) for x in color.split(",")]
            self.hex = '#{:02x}{:02x}{:02x}'.format(self.rgb[0], self.rgb[1], self.rgb[2])
        else:
            raise Exception(f"Invalid color: {color}")

    def GetHex(self) -> str:
        """
        Gets the Hex Color Code from the color.

        Returns:
            str: The color in hex format.
        """
        return self.hex

    def GetRGB(self) -> list[int]:
        """
        Gets the RGB from the color.

        Returns:
            list[int]: The color in RGB format.
        """
        return self.rgb
