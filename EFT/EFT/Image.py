class ImageValue:
    def __init__(self, image: str):
        self.image = image

    def GetImage(self) -> str:
        """
        Gets the Image's path as a string.

        Returns:
            str: The path to the image.
        """
        return self.image

    def __str__(self) -> str:
        return self.GetImage()
