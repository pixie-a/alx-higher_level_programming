#!/usr/bin/python3
"""Class to define a square.
size(private attribute)."""


class Square:
    """Define square."""
    def __init__(self, size):
        """Constructor.
        Args:
            size: length of side of the square.
        """
        self.__size = size
