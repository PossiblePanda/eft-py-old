class FontValue:
    def __init__(self, font: str):
        self.font = font

    def GetFont(self) -> str:
        """
        Gets the Font's path as a string.

        Returns:
            str: The path to the font.
        """
        return self.font

    def __str__(self) -> str:
        return self.GetFont()
