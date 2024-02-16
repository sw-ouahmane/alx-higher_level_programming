#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            id (int): The identity of the new Rectangle.
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Trace out the Rectangle using the `#` character."""
        if not self.width or not self.height:
            print("")
            return

        print("\n" * self.y, end="")
        for h in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print("")

    def __str__(self):
        """Override the __str__ method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes.
        Args:
            *args (ints): attribute values to update.
            **kwargs (dict): New key/value pairs of attributes.
        """

        if args and len(args):
            switch = {1: "width", 2: "height", 3: "x", 4: "y"}
            a = 0
            for arg in args:
                if not a:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg

                if a in switch:
                    setattr(self, switch[a], arg)
                a += 1

        elif kwargs and len(kwargs) != 0:
            switch = {"width": "width", "height": "height", "x": "x", "y": "y"}
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v

                if k in switch:
                    setattr(self, switch[k], v)

    def to_dictionary(self):
        """Return the  representation of a Rectangle as a dict."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
