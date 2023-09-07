from EFT import Color
from EFT import Font
from EFT import Image


def _GetFileContents(path: str) -> list[str]:
    """
    Gets the title of the theme

    Returns:
        str: The title of the theme
    """
    with open(path) as f:
        content_list = [line.rstrip() for line in f]
    return content_list


def GetFieldFromLine(line_number: int, path: str):
    """
    Gets a field object from a line

    Args:
        line_number ()

    Returns:
        Field: The field that was created
        :param line_number:
        :param path:
    """

    lines = _GetFileContents(path)
    line = lines[line_number]
    if line.startswith("- "):
        value = line.split(' ')[1]
    else:
        value = line.split(' ')[1]
    name = line.split(':')[0]
    field_type = line.split(':', 2)[2].strip(" ")

    match field_type:
        case "Color":
            field = ColorField(name, value, line_number)
        case "Font":
            field = FontField(name, value, line_number)
        case "Image":
            field = ImageField(name, value, line_number)
        case "Int":
            field = IntField(name, value, line_number)
        case "String":
            field = StringField(name, value, line_number)
        case _:
            raise Exception("Unknown field type, current supported types include Color, Font, Image, Int, String")

    return field


def _IsColorField(line_number: int, path: str):
    lines = _GetFileContents(path)
    return lines[line_number].endswith(": Color")


def _IsFontField(line_number: int, path: str):
    lines = _GetFileContents(path)
    return lines[line_number].endswith(": Font")


def _IsIntField(line_number: int, path: str):
    lines = _GetFileContents(path)
    return lines[line_number].endswith(": Int")


def _IsStringField(line_number: int, path: str):
    lines = _GetFileContents(path)
    return lines[line_number].endswith(": String")


def _IsImageField(line_number: int, path: str):
    lines = _GetFileContents(path)
    return lines[line_number].endswith(": Image")


class Field:
    def __init__(self, name, field_type, line_number):
        self.name = name
        self.field_type = field_type
        self.line_number = line_number

    def GetFieldName(self) -> str:
        """
        Returns the name of the field

        Returns:
            str: The name of the field
        """
        return self.name

    def GetLineLumber(self) -> int:
        """
        Returns the Line in the file that the field is in

        Returns:
            int: The Line of the field
        """
        return self.line_number


class ColorField(Field):
    def __init__(self, name, value, line_number):
        self.value = value
        super().__init__(name, "Color", line_number)

    def GetColor(self) -> str:
        """
        Returns the color of the field

        Returns:
            Color: The color of the field
        """

        return self.value

    def GetFieldName(self) -> str:
        """
        Returns the name of the field

        Returns:
            str: The name of the field
        """
        return self.name


class FontField(Field):
    def __init__(self, name, value, line_number):
        self.value = value
        super().__init__(name, "Font", line_number)

    def GetFont(self) -> str:
        """
        Returns the font in the field

        Returns:
            Font: The font in the field
        """

        return self.value

    def GetFieldName(self) -> str:
        """
        Returns the name of the field

        Returns:
            str: The name of the field
        """
        return self.name

    def GetFieldType(self) -> str:
        """
        Returns the Type of the field

        Returns:
            str: The Type of the field
        """
        return self.value

    def GetLineLumber(self) -> int:
        """
        Returns the Line in the file that the field is in

        Returns:
            int: The Line of the field
        """
        return self.line_number

    def __str__(self):
        return "{}:{}:{} | {}".format(self.name, self.value, self.field_type, self.line_number)


class ImageField(Field):
    def __init__(self, name, value, line_number):
        self.value = value
        super().__init__(name, "Image", line_number)

    def GetImage(self) -> str:
        """
        Returns the image in the field

        Returns:
            Image: The value in the field
        """

        return self.value

    def GetFieldName(self) -> str:
        """
        Returns the name of the field

        Returns:
            str: The name of the field
        """
        return self.name

    def GetFieldType(self) -> str:
        """
        Returns the Type of the field

        Returns:
            str: The Type of the field
        """
        return self.value

    def GetLineLumber(self) -> int:
        """
        Returns the Line in the file that the field is in

        Returns:
            int: The Line of the field
        """
        return self.line_number

    def __str__(self):
        return "{}:{}:{} | {}".format(self.name, self.value, self.field_type, self.line_number)


class IntField(Field):
    def __init__(self, name, value, line_number):
        self.value = value
        super().__init__(name, "Int", line_number)

    def GetInt(self) -> int:
        """
        Returns the int in the field

        Returns:
            Int: The value in the field
        """

        return self.value

    def GetFieldName(self) -> str:
        """
        Returns the name of the field

        Returns:
            str: The name of the field
        """
        return self.name

    def GetFieldType(self) -> str:
        """
        Returns the Type of the field

        Returns:
            str: The Type of the field
        """
        return self.value

    def GetLineLumber(self) -> int:
        """
        Returns the Line in the file that the field is in

        Returns:
            int: The Line of the field
        """
        return self.line_number

    def __str__(self):
        return "{}:{}:{} | {}".format(self.name, self.value, self.field_type, self.line_number)


class StringField(Field):
    def __init__(self, name, value, line_number):
        self.value = value
        super().__init__(name, "String", line_number)

    def GetString(self) -> str:
        """
        Returns the string in the field

        Returns:
            String: The value in the field
        """

        return self.value

    def GetFieldName(self) -> str:
        """
        Returns the name of the field

        Returns:
            str: The name of the field
        """
        return self.name

    def GetFieldType(self) -> str:
        """
        Returns the Type of the field

        Returns:
            str: The Type of the field
        """
        return self.value

    def GetLineLumber(self) -> int:
        """
        Returns the Line in the file that the field is in

        Returns:
            int: The Line of the field
        """
        return self.line_number

    def __str__(self):
        return "{}:{}:{} | {}".format(self.name, self.value, self.field_type, self.line_number)


class Theme:
    def __init__(self, path):
        self.path = path
        self.lines = _GetFileContents(path)

    def GetTitle(self) -> str:
        """
        Gets the title of the theme

        Returns:
            str: The title of the theme
        """
        for i in range(len(self.lines)):
            if self.lines[i].startswith("-") and i == 0:
                if self.lines[i].startswith("- "):
                    return self.lines[i][2:]
                if self.lines[i].startswith("-"):
                    return self.lines[i][1:]

    def GetLines(self) -> list:
        """
        Gets a list of all the lines inside the theme file

        Returns:
            list[str]: A list of lines in the theme's file.
        """
        return _GetFileContents(self.path)

    def GetColor(self, key: str) -> Color.ColorValue:
        """
        Gets the color from the name of a color in the file.

        Returns:
            ColorValue: The color in hex format in the theme
        """
        for i in range(len(_GetFileContents(self.path))):
            if _IsColorField(i + 1, self.path):
                field = GetFieldFromLine(i + 1, self.path)
                if field.GetFieldName() == key:
                    color = Color.ColorValue(field.GetColor())
                    return color

    def GetFont(self, key: str) -> Font.FontValue:
        """
        Gets the font from the name of a font in the file.

        Returns:
            FontValue: The font in the theme
        """
        for i in range(len(_GetFileContents(self.path))):
            if _IsFontField(i + 1, self.path):
                field = GetFieldFromLine(i + 1, self.path)
                if field.GetFieldName() == key:
                    font = Font.FontValue(field.GetFont())
                    return font

    def GetImage(self, key: str) -> Image.ImageValue:
        """
        Gets the image from the name of an image in the file.

        Returns:
            ImageValue: The image in the theme
        """
        for i in range(len(_GetFileContents(self.path))):
            if _IsImageField(i + 1, self.path):
                field = GetFieldFromLine(i + 1, self.path)
                if field.GetFieldName() == key:
                    image = Image.ImageValue(field.GetImage())
                    return image

    def GetInt(self, key: str) -> int:
        """
        Gets the int from the name of an int field in the file.

        Returns:
            int: The image in the theme
        """
        for i in range(len(_GetFileContents(self.path))):
            if _IsIntField(i + 1, self.path):
                field = GetFieldFromLine(i + 1, self.path)
                if field.GetFieldName() == key:
                    return int(field.GetInt())

    def GetString(self, key: str) -> str:
        """
        Gets the String from the name of an int field in the file.

        Returns:
            str: The image in the theme
        """
        for i in range(len(_GetFileContents(self.path))):
            if _IsImageField(i + 1, self.path):
                field = GetFieldFromLine(i + 1, self.path)
                if field.GetFieldName() == key:
                    return str(field.GetString())
