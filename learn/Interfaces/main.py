"""
Implementing an interface in Python
"""

# an interface acts as a blueprint for designing classes. Like classes, interfaces define method.
# Unlike classes, these methods are abstract
# An abstract method is one that the interface simply defines. It doesn't implement methods.
# This is done by classes, which then implement the interface and give concrete meaning to the
# interface's abstract methods.


# Informal interfaces

# InformalInterface class defines 2 methods but bot implemented.
class InformalInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass


# To use interface, you must create a concrete class.
# A concrete class is a subclass of the interface that provides an implementation of the
# interface's methods.

# The concrete implementation of InformalInterface now allows you to extract text from PDF files
class PdfParser(InformalInterface):
    """Extract text from PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Overrides InformalInterface.extract_text()"""
        pass


class EmailParser(InformalInterface):
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_name: str) -> dict:
        """
        A method defined only in EmailParser.
        Does not override InformalInterface.extract_text()
        """
        pass


# So far, we've defined two concrete implementation of the InformalInterface.
